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

class RandTesteur
 {
  public :
    RandTesteur( int nb, int resolution, int width )
     : nb_{nb}, num_{new_rand_coefs(nb)}, 
       exact_{new double [nb]}, approx_{new double [nb]},
       resolution_{resolution}, width_{width}
     {}
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual void execute( int bits ) =0 ;
    virtual ~RandTesteur()
     { delete [] num_ ; delete [] exact_ ; delete [] approx_ ; }
  protected : 
    int nb_ ;
    double * num_, * exact_, * approx_ ;
    void erreur( int bits )
     {
      double exacts {}, approxs {}, erreurs {} ;
      for ( int i=0 ; i<nb_ ; ++i )
       {
        exacts += exact_[i] ; approxs += approx_[i] ;
        erreurs += fabs(exact_[i]-approx_[i])/exact_[i] ;
       }
      exacts /= nb_ ; approxs /= nb_ ; erreurs /= nb_ ;
      erreurs *= resolution_ ;
      std::cout
        <<bits<<" bits : "
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
    void acquiere( RandTesteur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<RandTesteur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<Pointeur<RandTesteur>> testeurs_ ;
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
class TesteurCoefs : public RandTesteur
 {
  public :
    TesteurCoefs( int nb, int resolution )
     : RandTesteur(nb,resolution,8) {}
    virtual void execute( int bits )
     {
      Coef<U> c(bits) ;
      for ( int i=0 ; i<nb_ ; ++i )
       {
        c = num_[i] ;
        exact_[i] = num_[i] ;
        approx_[i] = arrondi(c,6) ;
       }
      erreur(bits) ;
     }
 } ;

template<typename U>
class TesteurSommes : public RandTesteur
 {
  public :
    TesteurSommes( int nb, int resolution )
     : RandTesteur(nb,resolution,7) {}
    virtual void execute( int bits )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      for ( int i=0 ; i<nb_ ; ++i )
       {
        coef1 = num_[i] ; coef2 = (1-num_[i]) ;
        exact_[i] = 200. ;
        approx_[i] = arrondi(coef1*U(exact_[i]) + coef2*U(exact_[i]),3) ;
       }
      erreur(bits) ;
     }
 } ;


//==============================================
// fonction principale
//==============================================


int main()
 {
  Testeurs ts ;
  ts.acquiere(new TesteurCoefs<unsigned char>(1000,1000)) ;
  ts.acquiere(new TesteurSommes<unsigned char>(1000,1000)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
