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
// fonction principale
//==============================================


int main()
 {
  std::cout<<std::endl ;
  int exposant ;
  for ( exposant = 1 ; exposant <= 8 ; exposant = exposant + 1 )
   {
    int num = arrondi(0.65*fois_puissance_de_deux(1,exposant))  ;
    std::cout << "0.65 ~ " << std::setw(3) << num << "/2^" << exposant << std::endl ;
   }
  std::cout<<std::endl ;
  return 0 ;
 }

