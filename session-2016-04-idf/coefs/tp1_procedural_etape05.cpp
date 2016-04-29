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

// arrondi
int arrondi( double d )
 {
  if (d>0) { return int(d+.5) ; }
  else { return int(d-.5) ; }
 }

// multiplie "nombre" par 2 puissance "exposant"
int fois_puissance_de_deux( int nombre, int exposant )
 {
  while (exposant>0)
   { nombre *= 2 ; exposant -= 1 ; }
  while (exposant<0)
   { nombre /= 2 ; exposant += 1 ; }
  return nombre ;
 }

// entier maximum représentable avec "nombre_bits" bits
int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }


//==============================================
// calculs
//==============================================

void approxime( int bits, double valeur )
 {
  int max = entier_max(bits) ;
  int exposant {}, num ;
  do
   {
    exposant = exposant + 1 ;
    num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
   } while (num<=max) ;
  exposant = exposant - 1 ;
  num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
  std::cout
    << bits << " bits : "
    << valeur << " ~ " << std::setw(3) << num << "/2^" << exposant
    << " = " << double(num)/fois_puissance_de_deux(1,exposant)
    << std::endl ;
 }


//==============================================
// fonction principale
//==============================================


int main()
 {
  int bits ;

  std::cout<<std::endl ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { approxime(bits,0.65) ; }

  std::cout<<std::endl ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { approxime(bits,0.35) ; }

  std::cout<<std::endl ;
  return 0 ;
 }

