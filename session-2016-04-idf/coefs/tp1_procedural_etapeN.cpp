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

#include <random>

double * new_rand_coefs( int taille )
 {
  std::random_device rd;
  std::mt19937 gen(rd());
  std::uniform_real_distribution<> dis(0,1);
  
  double * res = new double [taille] ;
  int i ;
  for ( i=0 ; i<taille ; i++ )
   { res[i] = dis(gen) ; }
  return res ;
 }


//==============================================
// framework general de test
//==============================================

std::ostream * sortie {} ;

void boucle( int deb, int fin, int inc, void (*f)( int, int, char *[] ), int argc, char *argv[] )
 {
  int bits ;
  for ( bits = deb ; bits <= fin ; bits += inc )
   { f(bits,argc,argv) ; }
  (*sortie)<<std::endl ;
 }


//==============================================
// calculs
//==============================================

void approxime( int bits, double valeur, int & numerateur, int & exposant )
 {
  numerateur = exposant = 0 ;
  if (valeur==0) { return ; }
  double min = (entier_max(bits)+0.5)/2 ;
  while (valeur<min)
   {
    exposant = exposant + 1 ;
    valeur = valeur * 2 ;
   }
  numerateur = arrondi(valeur) ;
 }

int multiplie( int bits, double c, int e )
 {
  int numerateur, exposant ;
  approxime(bits,c,numerateur,exposant) ;
  return fois_puissance_de_deux(numerateur*e,-exposant) ;
 }


//==============================================
// tests
//==============================================

void teste_approxime( int bits, double valeur )
 {
  int numerateur, exposant, erreur ;
  approxime(bits,valeur,numerateur,exposant) ;
  double approximation = double(numerateur)/fois_puissance_de_deux(1,exposant) ;
  erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  (*sortie).setf(std::ios::fixed,std::ios::floatfield) ;  
  (*sortie)
    <<std::setw(2)<<std::right<<bits<<" bits : "
    <<std::setw(4)<<std::setprecision(2)<<std::left<<valeur<<" ~ "
    <<std::setw(8)<<std::setprecision(6)<<std::left<<approximation
    <<" ("<<erreur<<"/100)"
    <<" ("<<numerateur<<"/2^"<<exposant<<")"
    <<std::endl ;
 }

void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  int exact, approx, erreur ;
  exact = arrondi(c1*e1+c2*e2) ;
  approx = multiplie(bits,c1,e1) + multiplie(bits,c2,e2) ;
  erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  (*sortie).setf(std::ios::fixed,std::ios::floatfield) ;  
  (*sortie)
    <<std::setw(2)<<std::right<<bits<<" bits : "
    <<std::setw(4)<<std::left<<exact<<" ~ "
    <<std::setw(4)<<std::left<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

void teste_065( int bits, int argc, char *argv[] )
 { teste_approxime(bits,0.65) ; }

void teste_035( int bits, int argc, char *argv[] )
 { teste_approxime(bits,0.35) ; }

void teste_065_3515_035_4832( int bits, int argc, char *argv[] )
 { teste_somme(bits,0.65,3515,0.35,4832) ; }

#include <cstdlib>  // for atoi

void teste_rand_coefs( int bits, int argc, char *argv[] )
 {
  int taille = atoi(argv[1]) ;
  double * values = new_rand_coefs(taille) ; 
  int i ;
  for ( i=0 ; i<taille ; i++ )
   { teste_approxime(bits,values[i]) ; }
  (*sortie)<<std::endl ;
  delete [] values ;
 }


//==============================================
// fonction principale
//==============================================

#include <fstream>

int main( int argc, char *argv[] )
 {
  if (argc<3) echec(1,"arguments manquants sur la ligne de commande") ;
 
  std::ofstream fichier(argv[2]) ;
  sortie = &fichier ;
  
  (*sortie)<<std::endl ;
  
  boucle(2,8,2,teste_065,argc,argv) ;
  boucle(2,8,2,teste_035,argc,argv) ;
  boucle(1,8,1,teste_065_3515_035_4832,argc,argv) ;
  boucle(1,8,1,teste_rand_coefs,argc,argv) ;
  
  fichier.close() ;
  
  return 0 ;
 }

