
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

int fois_puissance_de_deux( int nombre, int exposant )
 {
  if (nombre<0)
   { throw Echec(1,"cas imprevu") ; }
  if ((exposant<=-int(sizeof(int)<<3))||(exposant>=int(sizeof(int)<<3)))
   { throw Echec(1,"exposant trop grand") ; }
  if (exposant<0)
   { return (nombre>>-exposant) ; }
  if (nombre>int(((unsigned int)(-1))>>exposant>>1))
   { throw Echec(1,"overflow") ; }
  return (nombre<<exposant) ; 
 }

int arrondi( double d )
 {
  if (d>0) { return int(d+.5) ; }
  else { return int(d-.5) ; }
 }

int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }


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
    << bits << " bits : " << exact << " ~ "
    << std::setw(width) << approx
    << " ("<<err<<"/" << resolution_ << ")"
    << std::endl ;
 }

class Testeurs
 {
  public :
  
    class EchecTropDeTesteurs : public Echec
     { public : EchecTropDeTesteurs() : Echec(2,"trop de testeurs") {} } ;
    
    class EchecIndiceIncorrect : public Echec
     { public : EchecIndiceIncorrect() : Echec(3,"indice de testeur incorrect") {} } ;
    
    Testeurs( unsigned int max )
     : max__{max}, indice__{}, testeurs__{new Testeur * [max__]}
     {
      for ( unsigned i=0 ; i<max__ ; ++i )
       { testeurs__[i] = 0 ; }
     }
     
    void acquiere( Testeur * t )
     {
      if (indice__==max__) { throw EchecTropDeTesteurs() ; }
      testeurs__[indice__] = t ;
      indice__++ ;
     }
     
    unsigned int nb_testeurs() const
     { return indice__ ; }
     
    Testeur * operator[]( unsigned i ) const
     {
      if (i>=indice__) { throw EchecIndiceIncorrect() ; }
      return testeurs__[i] ;
     }
     
    ~Testeurs()
     {
      for ( unsigned i=0 ; i<max__ ; ++i )
       { delete testeurs__[i] ; }
      delete [] testeurs__ ;
     }
     
  private :
  
    unsigned int max__ ;
    unsigned int indice__ ;
    Testeur * * testeurs__ ;
 } ;
	
void boucle( int deb, int fin, int inc, const Testeurs & ts )
 {
  unsigned int i ;
  for ( i=0 ; i<ts.nb_testeurs() ; ++i )
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

class Coef
 {
  public :
  
    explicit Coef( unsigned int bits ) ;
    unsigned int lit_bits() const ;
    void operator=( double valeur ) ;
    operator double() const ;
    int operator*( int arg ) const ;
    int numerateur() const ;
    int exposant() const ;

  private :
  
    unsigned const int bits_ ;
    int numerateur_ ;
    int exposant_ ;
 } ;

std::ostream & operator<<( std::ostream & os, Coef const & c )
{ return (os<<c.numerateur()<<"/2^"<<c.exposant()) ; }

Coef::Coef( unsigned int bits )
 : bits_{bits}, numerateur_{0}, exposant_{0}
 {}
 
unsigned int Coef::lit_bits() const
 { return bits_ ; }

void Coef::operator=( double valeur )
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

Coef::operator double() const
 {
  if (exposant_<0) { throw Echec(5,"exposant negatif") ; }
  return (double(numerateur_)/fois_puissance_de_deux(1,exposant_)) ;
 }

int Coef::operator*( int arg ) const
 { return fois_puissance_de_deux(numerateur_*arg,-exposant_) ; }
 
int Coef::numerateur() const
 { return numerateur_ ; }
 
int Coef::exposant() const
 { return exposant_ ; }


//==============================================
// Testeurs dedies a Coef
//==============================================

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
      Coef c(bits) ;
      c = valeur ;
      erreur(bits,valeur,c,8) ;
     }
 } ;


class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void operator()( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      Coef coef1(bits), coef2(bits) ;
      int exact, approx ;
      exact = (int)(c1*e1+c2*e2) ;
      coef1 = c1 ;
      coef2 = c2 ;
      approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx,4) ;
     }
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts(5) ;
    ts.acquiere(new TesteurCoef(1000000)) ;
    ts.acquiere(new TesteurSomme(1000000)) ;
    boucle(4,16,4,ts) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }


