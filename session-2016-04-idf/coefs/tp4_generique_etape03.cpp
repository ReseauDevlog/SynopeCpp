// -*- coding: utf-8 -*-

//==============================================
// utilitaires
//==============================================

#include <iostream>
#include <iomanip>
#include <string>

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
  if (exposant>0) { nombre <<= exposant ; }
  else  { nombre >>= -exposant ; }
  return nombre ;
 }

double arrondi( double d, unsigned precision =0 )
 {
  double mult {1.} ;
  while (precision-->0) mult *= 10. ;
  if (d>0) { return int(d*mult+.5)/mult ; }
  else { return int(d*mult-.5)/mult ; }
 }

int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }


//==============================================
// framework general de test
//==============================================

class Testeur
 {
 
  public :
  
    class EchecDivisionParZero : public Echec
     { public : EchecDivisionParZero() : Echec(1,"division par 0") {} } ;
  
    Testeur( int resolution ) : resolution_(resolution) {}
    virtual void operator()( int bits ) =0 ;
    virtual ~Testeur() = default ;
    
  protected :
  
    void erreur( int bits, double exact, double approx )
     {
      if (exact==0) { throw EchecDivisionParZero() ; }
      int erreur = arrondi(resolution_*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/"<<resolution_<<")" ;
     }

  private :
  
    int const resolution_ ;

 } ;

class Testeurs
 {
  public :
  
    class EchecTropDeTesteurs : public Echec
     { public : EchecTropDeTesteurs() : Echec(2,"trop de testeurs") {} } ;
    
    class EchecIndiceIncorrect : public Echec
     { public : EchecIndiceIncorrect() : Echec(3,"indice de testeur incorrect") {} } ;
    
    Testeurs( int max )
     : max__{max}, indice__{}, testeurs__{new Testeur * [max__]}
     {}
     
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
  
    int max__ ;
    int indice__ ;
    Testeur * * testeurs__ ;
 } ;
    
void boucle( int deb, int fin, int inc, const Testeurs & ts )
 {
  for ( int i=0 ; i<ts.nb_testeurs() ; ++i )
   {
    try
     {
      Testeur & t = *ts[i] ;
      std::cout<<std::endl ;
      for ( int bits = deb ; bits <= fin ; bits = bits + inc )
       { t(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }


//==============================================
// calculs
//==============================================

template<typename U>
class Coef
 {
  public :
  
    Coef( int bits )
     : bits_(bits), numerateur_{}, exposant_{}
     {}
    int lit_bits() const
     { return bits_ ; }
    void operator=( double valeur )
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
    operator double() const
      {
      if (exposant_<0) { throw Echec(4,"exposant negatif") ; }
       return (double(numerateur_)/fois_puissance_de_deux(1,exposant_)) ;
      }
    U operator*( U arg ) const
     { return fois_puissance_de_deux(numerateur_*arg,-exposant_) ; }
   
    std::string texte() const
     { return std::to_string(numerateur_)+"/2^"+std::to_string(exposant_) ; }

  private :
  
    int const bits_ ;
    U numerateur_ ;
    int exposant_ ;
 } ;

template<typename U>
std::ostream & operator<<( std::ostream & os, Coef<U> const & c )
 { return (os<<c.texte()) ; }


//==============================================
// tests
//==============================================

class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef<int> c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c,6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.35) ; }
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
      U exact = arrondi(c1*e1+c2*e2) ;
      Coef<U> coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      U approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
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
    Testeurs ts(5) ;
    ts.acquiere(new TesteurCoef065(1000000)) ;
    ts.acquiere(new TesteurCoef035(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<unsigned short>(1000000)) ;
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
 
