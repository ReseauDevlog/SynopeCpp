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
     { return double(numerateur_)/fois_puissance_de_deux(1,exposant_) ; }
    
    int multiplie( int e )
     { return fois_puissance_de_deux(numerateur_*e,-exposant_) ; }
    
    int numerateur() { return numerateur_ ; }
    int exposant() { return exposant_ ; }

  private :
  
    int bits_ ;
    int numerateur_ ;
    int exposant_ ;
    
 } ;


//==============================================
// tests
//==============================================

class TesteurCoef
 {
  public :
  
    void execute( int bits )
     {
      c_.init(bits) ;
      teste(0.65) ;
      teste(0.35) ;
     }

  private :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      int erreur = arrondi(100*(valeur-approximation)/valeur) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<c_.lit_bits()<<" bits : "
        <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
        <<" ("<<erreur<<"/100)"
        <<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"
        <<std::endl ;
     }
    
    Coef c_ ;

 } ;
 
class TesteurSomme
 {
  public :
    void execute( int bits )
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
      int erreur = arrondi(1000*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<c1_.lit_bits()<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/1000)"<<std::endl ;
     }
    Coef c1_ ;
    Coef c2_ ;
 } ;


//==============================================
// fonction principale
//==============================================


int main()
 {
  int bits ;

  std::cout<<std::endl ;
  TesteurCoef tc ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { tc.execute(bits) ; }

  std::cout<<std::endl ;
  TesteurSomme ts ;
  for ( bits = 1 ; bits <= 8 ; bits = bits + 1 )
   { ts.execute(bits) ; }

  std::cout<<std::endl ;
  return 0 ;
 }
 
