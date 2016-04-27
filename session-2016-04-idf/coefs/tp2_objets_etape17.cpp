// -*- coding: utf-8 -*-

//==============================================
// utilitaires
//==============================================

#include <iostream>
#include <iomanip>
#include <string>

void echec( unsigned int code, std::string commentaire )
 {
  std::cout<<"[ERREUR "<<code<<" : "<<commentaire<<"]"<<std::endl ;
  exit(code) ;
 }

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
    void init( int resolution ) { resolution_ = resolution ; }
    virtual void execute( int bits ) = 0 ;
    virtual ~Testeur() {} ;
  protected :
    void erreur( int bits, double exact, double approx )
     {
      int erreur = arrondi(resolution_*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/"<<resolution_<<")" ;
     } 
  private :
    int resolution_ ;
 } ;

class Boucle
 {
  public :
    void init( int taille )
     {
      taille_ = taille ;
      indice_ = 0 ;
      testeurs_ = new Testeur * [taille_] ;
     }
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { echec(10,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    void execute( int debut, int fin, int inc )
     {
      for ( int i=0; i<indice_ ; i++ )
       {
        std::cout<<std::endl ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { testeurs_[i]->execute(bits) ; }
       }
     }
    void finalise()
     {
      for ( int i=0; i<indice_ ; i++ )
       { delete testeurs_[i] ; }
      delete [] testeurs_ ;
     }
    
  private :
  
    int taille_ ;
    int indice_ ;
    Testeur * * testeurs_ ;
    
 } ;
 

//==============================================
// calculs
//==============================================

class Coef
 {
  public :
  
    void init( int bits )
     { bits_ = bits ; }
    
    int lit_bits()
     { return bits_ ; }
    
    // transformation d'un double en Coef
    void approxime( double valeur )
     {
      numerateur_ = exposant_ = 0 ;
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
     { return double(numerateur_)/fois_puissance_de_deux(1,exposant_) ; }
    
    int multiplie( int e )
     { return fois_puissance_de_deux(numerateur_*e,-exposant_) ; }
    
    std::string texte()
     { return std::to_string(numerateur_)+"/2^"+std::to_string(exposant_) ; }

  private :
  
    int bits_ ;
    int numerateur_ ;
    int exposant_ ;
    
 } ;


//==============================================
// tests
//==============================================

class TesteurCoef : public Testeur
 {
  protected :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      erreur(c_.lit_bits(),valeur,approximation) ;
      std::cout<<" ("<<c_.texte()<<")"<<std::endl ;
     }
    
    Coef c_ ;
 } ;
 
class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) { init(resolution) ; }
    virtual void execute( int bits ) { c_.init(bits) ; teste(0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) { init(resolution) ; }
    virtual void execute( int bits ) { c_.init(bits) ; teste(0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :
    TesteurSomme( int resolution )
     { init(resolution) ; }
    virtual void execute( int bits )
     {
      c1_.init(bits) ;
      c2_.init(bits) ;
      teste(0.65,3515,0.35,4832) ;
     }
  private :
    void teste( double c1, int e1, double c2, int e2 )
     {
      c1_.approxime(c1) ;
      c2_.approxime(c2) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      approx = c1_.multiplie(e1) + c2_.multiplie(e2) ;
      erreur(c1_.lit_bits(),exact,approx) ;
      std::cout<<std::endl ;
     }
    Coef c1_ ;
    Coef c2_ ;
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  Boucle boucle ;
  boucle.init(3) ;
  boucle.acquiere(new TesteurCoef065(1000000)) ;
  boucle.acquiere(new TesteurCoef035(1000000)) ;
  boucle.acquiere(new TesteurSomme(1000000)) ;
  boucle.execute(4,16,4) ;
  boucle.finalise() ;
  std::cout << std::endl ;
  return 0 ;
 }
 
