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

template<int SIZE>
class Testeurs
 {
  public :
  
    class EchecTropDeTesteurs : public Echec
     { public : EchecTropDeTesteurs() : Echec(2,"trop de testeurs") {} } ;
    
    class EchecIndiceIncorrect : public Echec
     { public : EchecIndiceIncorrect() : Echec(3,"indice de testeur incorrect") {} } ;
    
    Testeurs() : indice_{} { static_assert(SIZE>=0,"nombre négatif de testeurs") ; }
     
    void acquiere( Testeur * t )
     {
      if (indice_==SIZE) { throw EchecTropDeTesteurs() ; }
      testeurs_[indice_] = t ;
      indice_++ ;
     }
     
    unsigned int nb_testeurs() const
     { return indice_ ; }
     
    Testeur * operator[]( unsigned i ) const
     {
      if (i>=indice_) { throw EchecIndiceIncorrect() ; }
      return testeurs_[i] ;
     }
     
    ~Testeurs()
     {
      for ( unsigned i=0 ; i<indice_ ; ++i )
       { delete testeurs_[i] ; }
     }
     
  private :
  
    int indice_ ;
    Testeur * testeurs_[SIZE] ;
 } ;
    
template<int SIZE>
void boucle( int deb, int fin, int inc, const Testeurs<SIZE> & ts )
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
   
    U numerateur() const { return numerateur_ ; }
    int exposant() const { return exposant_ ; }

  private :
  
    int const bits_ ;
    U numerateur_ ;
    int exposant_ ;
 } ;


template<typename U>
std::ostream & operator<<( std::ostream & os, Coef<U> const & c )
 { return (os<<c.numerateur()<<"/2^"<<c.exposant()) ; }

template<>
std::ostream & operator<<( std::ostream & os, Coef<unsigned char> const & c )
 { return (os<<int(c.numerateur())<<"/2^"<<c.exposant()) ; }


//==============================================
// tests
//==============================================

template<typename U>
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef<U> c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c,6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

template<typename U>
class TesteurCoef065 : public TesteurCoef<U>
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef<U>(resolution) {}
    virtual void operator()( int bits ) { this->teste(bits,0.65) ; }
 } ;

template<typename U>
class TesteurCoef035 : public TesteurCoef<U>
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef<U>(resolution) {}
    virtual void operator()( int bits ) { this->teste(bits,0.35) ; }
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
    Testeurs<3> ts ;
    ts.acquiere(new TesteurCoef065<int>(1000000)) ;
    ts.acquiere(new TesteurCoef035<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    boucle(4,16,4,ts) ;

    Testeurs<1> ts2 ;
    ts2.acquiere(new TesteurCoef065<unsigned char>(1000)) ;
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
 
