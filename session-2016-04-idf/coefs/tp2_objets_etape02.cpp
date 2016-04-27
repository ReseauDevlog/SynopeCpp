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
    int numerateur_ ;
    int exposant_ ;
 } ;

Coef approxime( int bits, double valeur )
 {
  Coef coef ;
  coef.numerateur_ = coef.exposant_ = 0 ;
  if (valeur==0) { return coef ; }
  double min = (entier_max(bits)+0.5)/2 ;
  while (valeur<min)
   {
    coef.exposant_ = coef.exposant_ + 1 ;
    valeur = valeur * 2 ;
   }
  coef.numerateur_ = arrondi(valeur) ;
  return coef ;
 }

int multiplie( int bits, double c, int e )
 {
  Coef coef = approxime(bits,c) ;
  return fois_puissance_de_deux(coef.numerateur_*e,-coef.exposant_) ;
 }


//==============================================
// tests
//==============================================

void teste_approxime( int bits, double valeur )
 {
  int erreur ;
  Coef coef = approxime(bits,valeur) ;
  double approximation = double(coef.numerateur_)/fois_puissance_de_deux(1,coef.exposant_) ;
  erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
    <<" ("<<erreur<<"/100)"
    <<" ("<<coef.numerateur_<<"/2^"<<coef.exposant_<<")"
    <<std::endl ;
 }

void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  int exact, approx, erreur ;
  exact = arrondi(c1*e1+c2*e2) ;
  approx = multiplie(bits,c1,e1) + multiplie(bits,c2,e2) ;
  erreur = arrondi(1000*double(exact-approx)/exact) ;
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

