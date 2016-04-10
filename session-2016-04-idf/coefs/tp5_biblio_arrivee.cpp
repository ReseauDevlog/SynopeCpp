
#include <iostream>
#include <iomanip>
#include <string>


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

template<typename T> constexpr bool avec_signe() { return true ; }
template<> constexpr bool avec_signe<unsigned int>() { return false ; }
template<> constexpr bool avec_signe<unsigned short>() { return false ; }
template<> constexpr bool avec_signe<unsigned char>() { return false ; }

template<typename T>
constexpr int nombre_bits_hors_signe()
 { return avec_signe<T>()?(sizeof(T)*8-1):(sizeof(T)*8) ; }


//==============================================
// framework general de test
//==============================================

class Testeur
 {
  public :
  
    class EchecDivisionParZero ;
  
    Testeur( int resolution ) ;
    virtual void operator()( int bits ) =0 ;
    virtual ~Testeur() {} ;
    
  protected :
  
    void erreur( int bits, double exact, double approx, int width ) ;

  private :
  
    int const resolution_ ;

 } ;

class Testeur::EchecDivisionParZero : public Echec
 { public : EchecDivisionParZero() : Echec(4,"division par 0") {} } ;
    
Testeur::Testeur( int resolution )
 : resolution_(resolution) {}

void Testeur::erreur( int bits, double exact, double approx, int width  )
 {
  if (exact==0) { throw EchecDivisionParZero() ; }
  int err = arrondi(resolution_*(exact-approx)/exact) ;
  if (err<0) err = -err ;
  if (err>resolution_) err = resolution_ ;
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<std::setw(width)<<approx
    << " ("<<err<<"/" << resolution_ << ")" ;
 }

class Testeurs
 {
  public :
  
    class EchecTropDeTesteurs : public Echec
     { public : EchecTropDeTesteurs() : Echec(2,"trop de testeurs") {} } ;
    
    class EchecIndiceIncorrect : public Echec
     { public : EchecIndiceIncorrect() : Echec(3,"indice de testeur incorrect") {} } ;
    
    Testeurs()
     : indice__{}
     {
      static_assert(SIZE>=0,"nombre négatif de testeurs") ;
      for ( unsigned i=0 ; i<SIZE ; ++i )
       { testeurs__[i] = 0 ; }
     }
     
    void acquiere( Testeur * t )
     {
      if (indice__==SIZE) { throw EchecTropDeTesteurs() ; }
      testeurs__[indice__] = t ;
      indice__++ ;
     }
     
    Testeur * operator[]( unsigned i ) const
     {
      if (i>=indice__) { throw EchecIndiceIncorrect() ; }
      return testeurs__[i] ;
     }
     
    ~Testeurs()
     {
      for ( Testeur * t : testeurs__ )
       { delete t ; }
     }
     
  private :
  
    std::vector<Testeur *> testeurs__ ;
 } ;
    
template<signed SIZE>
void boucle( int deb, int fin, int inc, const Testeurs<SIZE> & ts )
 {
  unsigned int i ;
  for ( i=0 ; i<SIZE ; ++i )
   {
    try
     {
      Testeur & t = *ts[i] ;
      std::cout<<std::endl ;
      int bits ;
      for ( bits = deb ; bits <= fin ; bits = bits + inc )
       { t(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }


//==============================================
// Coef
//==============================================

template<typename U>
class Coef
 {
  public :
  
    class EchecTropDeBits : public Echec
     { public : EchecTropDeBits() : Echec(2,"trop de bits pour ce type") {} } ;
     
    explicit Coef( unsigned int bits ) ;
    unsigned int lit_bits() const ;
    void operator=( double valeur ) ;
    operator double() const ;
    U operator*( U arg ) const ;
    U numerateur() const ;
    int exposant() const ;

  private :
  
    unsigned const int bits_ ;
    U numerateur_ ;
    int exposant_ ;
    
    static constexpr unsigned int max_bits__
     = nombre_bits_hors_signe<U>() ;
 } ;


template<typename U>
std::ostream & operator<<( std::ostream & os, Coef<U> const & c )
{ return (os<<c.numerateur()<<"/2^"<<c.exposant()) ; }

template<>
std::ostream & operator<<( std::ostream & os, Coef<unsigned char> const & c )
{ return (os<<int(c.numerateur())<<"/2^"<<int(c.exposant())) ; }

template<typename U>
Coef<U>::Coef( unsigned int bits )
 : bits_{bits}, numerateur_{}, exposant_{}
 { if (bits_>max_bits__) throw EchecTropDeBits() ; }
 
template<typename U>
unsigned int Coef<U>::lit_bits() const
 { return bits_ ; }

template<typename U>
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

template<typename U>
Coef<U>::operator double() const
 {
  if (exposant_<0) { throw Echec(5,"exposant negatif") ; }
  return (double(numerateur_)/fois_puissance_de_deux(1,exposant_)) ;
 }

template<typename U>
U Coef<U>::operator*( U arg ) const
 { return fois_puissance_de_deux(numerateur_*arg,-exposant_) ; }
 
template<typename U>
U Coef<U>::numerateur() const
 { return numerateur_ ; }
 
template<typename U>
int Coef<U>::exposant() const
 { return exposant_ ; }


//==============================================
// Testeurs dedies a Coef
//==============================================

template<typename U>
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

    virtual void operator()( int bits )
     {
      teste(bits,0.65) ;
      teste(bits,0.35) ;
     }
  
  private :
  
    void teste( int bits, double valeur )
     {
      Coef<U> c(bits) ;
      c = valeur ;
      erreur(bits,valeur,c,8) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;


template<typename U>
class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void operator()( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, U e1, double c2, U e2 )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      int exact, approx ;
      exact = (U)(c1*e1+c2*e2) ;
      coef1 = c1 ;
      coef2 = c2 ;
      approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx,4) ;
      std::cout<<std::endl ;
     }
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs<3> ts ;
    ts.acquiere(new TesteurCoef<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    ts.acquiere(new TesteurCoef<short>(1000000)) ;
    boucle(4,16,4,ts) ;
    std::cout<<std::endl ;
    Testeurs<1> ts2 ;
    ts2.acquiere(new TesteurCoef<unsigned char>(1000)) ;
    boucle(1,8,1,ts2) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }


