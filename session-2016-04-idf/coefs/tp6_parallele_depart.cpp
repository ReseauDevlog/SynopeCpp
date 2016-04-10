
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
  static std::uniform_real_distribution<> dis(0.01, 1.0);
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
    
    struct ResultatTest
     {
      double exact;
      double approx;
     };

    void erreur( int bits,
                 std::vector<ResultatTest> resultats,
                 int width ) ;

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


void Testeur::erreur( int bits,
                      std::vector<ResultatTest> resultats,
                      int width  )
 {
  const size_t nb_valeurs = resultats.size();
  double err_moyenne = 0;
  
  for ( auto & resultat : resultats )
   {
    double exact = resultat.exact;
    double approx = resultat.approx;
    
    if (exact == 0.0) { throw EchecDivisionParZero() ; }
    double err = resolution_*(exact-approx)/exact;
    if (err<0) err = -err ;
    if (err>resolution_) err = resolution_ ;
    
    err_moyenne += err;
   }
  
  err_moyenne /= nb_valeurs;
  int err_finale = arrondi(err_moyenne);
  
  std::cout << bits << " bits : " << err_finale <<"/" << resolution_ << std::endl ;
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
class TesteurCoefs : public Testeur
 {
  public :
  
    TesteurCoefs( int resolution, int nombre_iterations )
     : Testeur(resolution), iterations_(nombre_iterations)
     {}

    virtual void execute( int bits )
     {
      teste(bits) ;
     }
  
  private :
  
    int iterations_;
  
    void teste( int bits )
     {
      Coef<U> c(bits) ;
      std::vector<Testeur::ResultatTest> resultats;
      resultats.reserve(iterations_);
      
      for ( int i = 0 ; i < iterations_ ; ++i )
       {
        double coef = generer_coef();
        c = coef ;
        resultats.push_back({coef, c});
       }
       
      erreur(bits, resultats, 8);
     }
 } ;


template< typename U >
class TesteurSommes : public Testeur
 {
  public :

    TesteurSommes( int resolution, int nombre_iterations )
     : Testeur(resolution), iterations_(nombre_iterations)
     {}

    virtual void execute( int bits )
     {
      static const U entier_test = 10000;
      teste(bits, entier_test) ;
     }

  private :
  
    int iterations_;
  
    void teste( int bits, U e )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      std::vector<Testeur::ResultatTest> resultats;
      resultats.reserve(iterations_);
      
      for ( int i = 0 ; i < iterations_ ; ++i )
       {
        double c1 = generer_coef();
        double c2 = 1.0-c1;
        
        int exact = arrondi(c1*e+c2*e) ;
        
        coef1 = c1 ;
        coef2 = c2 ;
        int approx = coef1*e + coef2*e ;
        
        resultats.push_back({double(exact), double(approx)});
       }
      
      erreur(bits, resultats, 7) ;
     }
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    TesteurCoefs<unsigned short> tc(10000, 10000000) ;
    TesteurSommes<unsigned short> ts(10000, 10000000) ;
    
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

