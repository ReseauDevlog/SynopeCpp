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
    Testeur( int resolution ) : resolution_{resolution} {}
    virtual void execute( int bits ) = 0 ;
    virtual ~Testeur() {} ;
  protected :
    void erreur( int bits, double exact, double approx )
     {
      if (exact==0) { throw Echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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
    Testeurs( int taille )
     : taille_{taille}, indice_{0}, testeurs_{new Testeur * [taille]}
     {}
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { throw Echec(2,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    int nb_elements() { return indice_ ; }
    Testeur * element( int indice )
     {
      if ((indice<0)||(indice>=indice_))
       { throw Echec(3,"indice de testeur incorrect") ; }
      return testeurs_[indice] ;
     }
    ~Testeurs()
     {
      for ( int i=0; i<indice_ ; i++ )
       { delete testeurs_[i] ; }
      delete [] testeurs_ ;
     }
  private :
    int const taille_ ;
    int indice_ ;
    Testeur * * testeurs_ ;
    
 } ;


void boucle( int debut, int fin, int inc, Testeurs & ts )
 {
  int nb = ts.nb_elements() ;
  for ( int i=0; i<nb ; i++ )
   {
    try
     {
      std::cout<<std::endl ;
      for ( int bits = debut ; bits <= fin ; bits = bits + inc )
       { ts.element(i)->execute(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }
 

//==============================================
// calculs
//==============================================

class Coef
 {
  public :
  
    Coef( int bits )
     : bits_{bits}, numerateur_{}, exposant_{}
     {}

    int lit_bits()
     { return bits_ ; }
    
    // transformation d'un double en Coef
    void approxime( double valeur )
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
    
    // transformation d'un Coef en double
    double approximation()
     {
      if (exposant_<0) { throw Echec(4,"exposant negatif") ; }
      return double(numerateur_)/fois_puissance_de_deux(1,exposant_) ;
     }
    
    int operator*( int e )
     { return fois_puissance_de_deux(numerateur_*e,-exposant_) ; }
    
    int numerateur() const { return numerateur_ ; }
    int exposant() const { return exposant_ ; }

  private :
  
    int const bits_ ;
    int numerateur_ ;
    int exposant_ ;
    
 } ;

void affiche( Coef const & c )
 { std::cout << c.numerateur()<<"/2^"<<c.exposant() ; }


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
      Coef c(bits) ;
      c.approxime(valeur) ;
      erreur(bits,valeur,arrondi(c.approximation(),6)) ;
      std::cout<<" (" ;
      affiche(c) ;
      std::cout<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1.approxime(c1) ;
      coef2.approxime(c2) ;
      int approx = coef1*e1 + coef2*e2 ;
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
 
