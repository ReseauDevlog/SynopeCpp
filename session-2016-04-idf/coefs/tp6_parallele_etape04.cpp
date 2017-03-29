// -*- coding: utf-8 -*-

//==============================================
// utilitaires
//==============================================

#include <iostream>
#include <iomanip>
#include <string>
#include <memory>
#include <random>

// émule la fonction std::make_unique qui apparait en C++14
namespace std
 {
  template<typename T, typename... Args>
  std::unique_ptr<T> make_unique(Args&&... args)
   { return std::unique_ptr<T>(new T(std::forward<Args>(args)...)) ; }
 }

double arrondi( double d, unsigned precision =0 )
 {
  double mult {1.} ;
  while (precision-->0) mult *= 10. ;
  if (d>0) { return int(d*mult+.5)/mult ; }
  else { return int(d*mult-.5)/mult ; }
 }

constexpr int fois_puissance_de_deux( int nombre, int exposant )
 { return (exposant>0)?(nombre<<exposant):(nombre>>(-exposant)) ; }

constexpr int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }

class RandCoefs
 {
  public :
    RandCoefs() : rd_{}, gen_{rd_()}, dis_(0,1) {}
    double operator()()
     { return dis_(gen_) ; }
  private :
    std::random_device rd_ ;
    std::mt19937 gen_ ;
    std::uniform_real_distribution<> dis_ ;
 } ;



//==============================================
// framework general de test
//==============================================

#include <array>
#include <map>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      for ( double & coef : coefs_ )
       { coef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      double exact, approx ;
      Resultat & res = resultats_[bits] ;
      for ( double coef : coefs_ )
       {
        execute(bits,coef,exact,approx) ;
        res.exacts +=exact ; res.approxs += approx ;
        res.erreurs += fabs(exact-approx)/exact ;
       }
      res.exacts /= SIZE ; res.approxs /= SIZE ; res.erreurs /= SIZE ;
      res.erreurs *= resolution_ ;
     }
     
    void affiche()
     {
      std::cout<<std::endl ;
      for ( auto res : resultats_ )
       {
        std::cout
          <<res.first<<" bits : "
          <<std::left<<res.second.exacts<<" ~ "
          <<std::setw(width_)<<res.second.approxs
          <<" ("<<arrondi(res.second.erreurs)<<"/"<<resolution_<<")"
          <<std::endl ;
       }
     }
     
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    struct Resultat
     {
      Resultat() : exacts {0}, approxs {0}, erreurs {0} {}
      double exacts, approxs, erreurs ;
     } ;
    
    std::array<double,SIZE> coefs_ ;
    std::map<int,Resultat> resultats_ ;
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;


#include <thread>

template<typename Testeurs>
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  std::vector<std::thread> threads ;
  for ( auto & testeur : ts )
   {
    threads.push_back(std::thread(
      [deb,fin,inc,&testeur]()
       {
        for ( int bits = deb ; bits <= fin ; bits = bits + inc )
         { testeur->execute(bits) ; }
       })) ;
   }
  for ( auto & thr : threads )
   { thr.join() ; }
  for ( auto & testeur : ts )
   { testeur->affiche() ; }
 }


//==============================================
// calculs
//==============================================

template<typename U>
class Coef
 {
  public :
    Coef( int bits ) : bits_(bits), numerateur_{}, exposant_{} {}  
    int lit_bits() const { return bits_ ; }
    void operator=( double valeur )
      {
       numerateur_ = exposant_ = 0 ;
       if (valeur==0) { return ; }
       double min = (entier_max(bits_)+0.5)/2 ;
       while (valeur<min)
        { exposant_ += 1 ; valeur *= 2 ; }
       numerateur_ = arrondi(valeur) ;
      }   
    operator double() const
      { return (double(numerateur_)/fois_puissance_de_deux(1,exposant_)) ; }
    U operator*( U arg ) const
     { return fois_puissance_de_deux(numerateur_*arg,-exposant_) ; }
  private :
    int const bits_ ;
    U numerateur_ ;
    int exposant_ ;
 } ;


//==============================================
// tests
//==============================================

template<typename U, int SIZE>
class TesteurCoefs : public RandTesteur<SIZE>
 {
  public :
    TesteurCoefs( int resolution )
     : RandTesteur<SIZE>(resolution,8) {}
    virtual void execute( int bits, double coef, double & exact, double & approx )
     {
      Coef<U> c(bits) ;
      c = coef ;
      exact =coef ;
      approx = arrondi(c,6) ;
     }
 } ;

template<typename U, int SIZE>
class TesteurSommes : public RandTesteur<SIZE>
 {
  public :
    TesteurSommes( int resolution )
     : RandTesteur<SIZE>(resolution,7) {}
    virtual void execute( int bits, double coef, double & exact, double & approx )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      coef1 = coef ; coef2 = (1-coef) ;
      exact = 200. ;
      approx = arrondi(coef1*U(exact) + coef2*U(exact),3) ;
     }
 } ;


//==============================================
// fonction principale
//==============================================


#include <chrono>

int main()
 {
  using namespace std ;
  using namespace chrono ;
  
  auto debut = steady_clock::now() ;

  constexpr int SIZE = 1000000 ;
  vector<unique_ptr<RandTesteur<SIZE>>> ts ;
  ts.push_back(make_unique<TesteurCoefs<unsigned char,SIZE>>(1000)) ;
  ts.push_back(make_unique<TesteurSommes<unsigned char,SIZE>>(1000)) ;
  boucle(1,8,1,ts) ;
  
  auto fin = steady_clock::now() ;
  auto temps = duration_cast<milliseconds>(fin - debut) ;
  
  std::cout<<"\ntemps ecoule : "<<temps.count()<<" ms\n"<<std::endl ;
  
  return 0 ;
 }
 
