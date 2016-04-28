// -*- coding: utf-8 -*-

//==============================================
// utilitaires
//==============================================

#include <iostream>
#include <iomanip>
#include <string>
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

// crée sur le tas un tableau dynamique de coefficients
double * new_rand_coefs( int taille )
 {
  std::random_device rd ;
  std::mt19937 gen(rd()) ;
  std::uniform_real_distribution<> dis(0,1) ;
  
  double * res = new double [taille] ;
  for ( int i=0 ; i<taille ; i++ )
   { res[i] = dis(gen) ; }
  return res ;
 }


template<typename Valeur>
class Pointeur
 {
  public :
    Pointeur( Valeur * val ) : val_{val} {}
    Pointeur( Pointeur const & ptr ) = delete ;
    void operator=( Pointeur const & ptr ) = delete ;
    Pointeur( Pointeur && ptr ) : val_{ptr.val_} { ptr.val_ = nullptr ; }
    void operator=( Pointeur && ptr ) { val_ = ptr.val_ ; ptr.val_ = nullptr ; }
    Valeur & operator*() const { return *val_ ; } 
    Valeur * operator->() const { return val_ ; } 
    ~Pointeur() { delete val_ ; }
  private :
    Valeur * val_ ;
 } ;
 

//==============================================
// framework general de test
//==============================================

class Testeur
 {
  public :
    Testeur( int resolution, int width )
     : resolution_(resolution), width_(width) {}
    Testeur( Testeur const & ) = delete ;
    Testeur & operator=( Testeur const & ) = delete ;
    virtual void execute( int bits ) =0 ;
    virtual ~Testeur() = default ;
  protected : 
    // recoit des tableaux de valeurs exactes et approximations
    void erreur( int bits, double * exact, double * approx, int nb )
     {
      double exacts {}, approxs {}, erreurs {} ;
      for ( int i=0 ; i<nb ; ++i )
       {
        exacts += exact[i] ;
        approxs += approx[i] ;
        erreurs += fabs(exact[i]-approx[i])/exact[i] ;
       }
      exacts /= nb ;
      approxs /= nb ;
      erreurs *= (resolution_/nb) ;
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
        <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
        <<std::endl ;
     }
  private :
    int const resolution_ ;
    int const width_ ;
 } ;


class Testeurs
 {
  public :
    void acquiere( Testeur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<Testeur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<Pointeur<Testeur>> testeurs_ ;
 } ;
    

void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  for ( int i=0 ; i<ts.nb_elements() ; ++i )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     { ts[i]->execute(bits) ; }
   }
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

template<typename U>
class TesteurRandCoefs : public Testeur
 {
  public :
    TesteurRandCoefs( int resolution, int nbcoefs )
     : Testeur(resolution,8), nbcoefs_{nbcoefs}
     { exact_ = new_rand_coefs(nbcoefs_) ; approx_ = new double [nbcoefs_] ; }
    virtual void execute( int bits )
     {
      Coef<U> c(bits) ;
      for ( int i=0 ; i<nbcoefs_ ; ++i )
       { c = exact_[i] ; approx_[i] = arrondi(c,6) ; }
      erreur(bits,exact_,approx_,nbcoefs_) ;
     }
    virtual ~TesteurRandCoefs()
     { delete [] exact_ ; delete [] approx_ ; }
  private :
    int nbcoefs_ ;
    double * exact_ ;
    double * approx_ ;
 } ;

template<typename U>
class TesteurSomme : public Testeur
 {
  public :
    TesteurSomme( int resolution )
     : Testeur(resolution,3) {}
    virtual void execute( int bits )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      coef1 = 0.65 ; coef2 = 0.35 ;
      double exact = 100 ;
      double approx = coef1*U(exact) + coef2*U(exact) ;
      erreur(bits,&exact,&approx,1) ;
     }
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs ts ;
  ts.acquiere(new TesteurRandCoefs<unsigned char>(1000,1000)) ;
  ts.acquiere(new TesteurSomme<unsigned char>(100)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
