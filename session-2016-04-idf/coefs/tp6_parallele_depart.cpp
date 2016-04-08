
#include <iostream>
#include <iomanip>
#include <random>
#include <string>
#include <vector>


//==============================================
// utilitaires
//==============================================

class Echec
 {
  public :
    Echec( unsigned int c, std::string const & comm )
     : code_(c), commentaire_(comm) {}
     
    unsigned int code() const { return code_ ; }
    
    std::string const & commentaire() const { return commentaire_ ; }
    
  private :
    unsigned int code_ ;
	 std::string commentaire_ ;
 } ;


int fois_puissance_de_deux( int nombre, int exposant )
 {
  if (nombre < 0)
   {
    throw Echec(1, "cas imprevu") ;
   }
  else if ( (exposant <= -int(sizeof(int)<<3)) || (exposant >= int(sizeof(int)<<3)) )
   {
    throw Echec(1, "exposant trop grand") ;
   }
  else if (exposant < 0)
   {
    return (nombre >> -exposant) ;
   }
  else if (nombre > (((unsigned int)(-1))>>exposant>>1))
   {
    throw Echec(1, "overflow") ;
   }
  else
   {
    return (nombre<<exposant) ; 
   }
 }


int arrondi( double d )
 {
  if (d > 0)
   {
    return int(d+.5) ;
   }
  else
   {
    return int(d-.5) ;
   }
 }


int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }


double generer_coef()
 {
  static std::random_device rd;
  static std::mt19937 gen(rd());
  static std::uniform_real_distribution<> dis(0,1);
  return dis(gen) ;
 }


//==============================================
// framework general de test
//==============================================

class Testeur
 {
  public :
  
    class EchecDivisionParZero ;
  
    typedef std::vector<Testeur *> Conteneur ;
    typedef Conteneur::iterator Iterateur ;
	
    static Iterateur begin() ;
    static Iterateur end() ;
	 
    Testeur( int resolution ) ;
    virtual void execute( int bits ) = 0 ;
    void erreur( int bits, double exact, double approx, int width ) ;

  private :
  
    static std::vector<Testeur *> testeurs__ ;
    int const resolution_ ;
    
    static void ajouter_test( Testeur * t ) ;

 } ;
 

std::vector<Testeur *> Testeur::testeurs__ ;
	
	
class Testeur::EchecDivisionParZero : public Echec
 { public : EchecDivisionParZero() : Echec(4, "division par 0") {} } ;
 
 
Testeur::Iterateur Testeur::begin()
 { return testeurs__.begin() ; }
  
  
Testeur::Iterateur Testeur::end()
 { return testeurs__.end() ; }
  

Testeur::Testeur( int resolution )
 : resolution_(resolution)
 { ajouter_test(this) ; }


void Testeur::erreur( int bits, double exact, double approx, int width  )
 {
  if (exact==0) { throw EchecDivisionParZero() ; }
  int err = arrondi(resolution_*(exact-approx)/exact) ;
  if (err<0) err = -err ;
  if (err>resolution_) err = resolution_ ;
  
  std::cout
    << bits << " bits : " << exact << " ~ "
    << std::setw(width) << approx
    << " ("<< err <<"/" << resolution_ << ")"
    << std::endl ;
 }
 
void Testeur::ajouter_test( Testeur * t )
 { testeurs__.push_back(t) ; }


void boucle_tests( int deb, int fin, int inc )
 {
  Testeur::Iterateur itr ;
  for ( itr=Testeur::begin() ; itr!=Testeur::end() ; itr++ )
   {
    try
     {
      std::cout<<std::endl ;
      int bits ;
      for ( bits = deb ; bits <= fin ; bits = bits + inc )
       { (*itr)->execute(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }


//==============================================
// Coef
//==============================================

template< typename U >
class Coef
 {
  public :
  
    Coef( unsigned int bits ) ;
    unsigned int lit_bits() const ;
    void operator=( double valeur ) ;
    operator double() const ;
    U operator*( U arg ) const ;
    U numerateur() const ;
    int exposant() const ;

  private :
  
    unsigned int const bits_ ;
    U numerateur_ ;
    int exposant_ ;
 } ;


template< typename U >
std::ostream & operator<<( std::ostream & os, Coef<U> const & c )
 { return (os<<c.numerateur()<<"/2^"<<c.exposant()) ; }


template< typename U >
Coef<U>::Coef( unsigned int bits )
 : bits_(bits), numerateur_(0), exposant_(0)
 {}
 
 
template< typename U >
unsigned int Coef<U>::lit_bits() const
 { return bits_ ; }


template< typename U >
void Coef<U>::operator=( double valeur )
 {
  numerateur_ = exposant_ = 0 ;
  if (valeur==0) { return ; }
  
  double min = (entier_max(bits_)+0.5)/2 ;
  while (valeur<min)
   {
    exposant_ = exposant_ + 1 ;
    valeur = valeur * 2 ;
   }
  numerateur_ = arrondi(valeur) ;
 }


template< typename U >
Coef<U>::operator double() const
 {
  if (exposant_<0) { throw Echec(5,"exposant negatif") ; }
  return (double(numerateur_)/fois_puissance_de_deux(1,exposant_)) ;
 }


template< typename U >
U Coef<U>::operator*( U arg ) const
 { return fois_puissance_de_deux(numerateur_*arg,-exposant_) ; }
 
 
template< typename U >
U Coef<U>::numerateur() const
 { return numerateur_ ; }
 
 
template< typename U >
int Coef<U>::exposant() const
 { return exposant_ ; }


//==============================================
// Testeurs dedies a Coef
//==============================================

template< typename U >
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     {
      static const int nombre_iterations = 10; // TODO : Doit devenir un paramètre du constructeur
      teste(bits, nombre_iterations) ;
     }
  
  private :
  
    void teste( int bits, int iterations )
     {
      Coef<U> c(bits) ;
      
      for ( int i = 0 ; i < iterations ; ++i )
       {
        double valeur = generer_coef();
        c = valeur ;
        
        erreur(bits,valeur,c,8) ; // TODO : Doit être remplacé par un calcul statistique à la fin
       }
     }
 } ;


template< typename U >
class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     {
      static const U entier_test = 100000;
      static const int nombre_iterations = 10; // TODO : Doit devenir un paramètre du constructeur
      teste(bits, entier_test, nombre_iterations) ;
     }

  private :
  
    void teste( int bits, U e, int iterations )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      
      for ( int i = 0 ; i < iterations ; ++i )
       {
        double c1 = generer_coef();
        double c2 = 1.0-c1;
        int exact = arrondi(c1*e+c2*e) ;
        coef1 = c1 ;
        coef2 = c2 ;
        int approx = coef1*e + coef2*e ;
        
        erreur(bits, exact, approx, 7) ; // TODO : Doit être remplacé par un calcul statistique à la fin
       }
     }
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    TesteurCoef<unsigned int> tc(100) ;
    TesteurSomme<unsigned int> ts(1000) ;
    
    boucle_tests(1,8,1) ;
    std::cout<<std::endl ;
    
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
    return e.code() ;
   }
 }

