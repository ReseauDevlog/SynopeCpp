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
  
    // transformation d'un double en Coef
    void approxime( int bits, double valeur )
     {
      numerateur_ = exposant_ = 0 ;
      double min = (entier_max(bits)+0.5)/2 ;
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
  
    int numerateur_ ;
    int exposant_ ;
    
 } ;


//==============================================
// tests
//==============================================

void teste_approxime( int bits, double valeur )
 {
  int erreur ;
  Coef coef ;
  coef.approxime(bits,valeur) ;
  double approximation = coef.approximation() ;
  erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
    <<" ("<<erreur<<"/100)"
    <<" ("<<coef.texte()<<")"
    <<std::endl ;
 }

void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  Coef coef1, coef2 ;
  coef1.approxime(bits,c1) ;
  coef2.approxime(bits,c2) ;
  int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
  int exact = arrondi(c1*e1+c2*e2) ;
  int erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }


//==============================================
// fonction principale
//==============================================

int main()
 {
  int bits ;

  std::cout<<std::endl ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { teste_approxime(bits,0.65) ; }

  std::cout<<std::endl ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { teste_approxime(bits,0.35) ; }

  std::cout<<std::endl ;
  for ( bits = 1 ; bits <= 8 ; bits = bits + 1 )
   { teste_somme(bits,0.65,3515,0.35,4832) ; }

  std::cout<<std::endl ;
  return 0 ;
 }

