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

void boucle( int deb, int fin, int inc, void (*f)( int ) )
 {
  int bits ;
  for ( bits = deb ; bits <= fin ; bits += inc )
   { f(bits) ; }
  std::cout<<std::endl ;
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
  std::cout.setf(std::ios::fixed,std::ios::floatfield) ;  
  std::cout
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
  std::cout.setf(std::ios::fixed,std::ios::floatfield) ;  
  std::cout
    <<std::setw(2)<<std::right<<bits<<" bits : "
    <<std::setw(4)<<std::left<<exact<<" ~ "
    <<std::setw(4)<<std::left<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

void teste_065( int bits )
 { teste_approxime(bits,0.65) ; }

void teste_035( int bits )
 { teste_approxime(bits,0.35) ; }

void teste_065_3515_035_4832( int bits )
 { teste_somme(bits,0.65,3515,0.35,4832) ; }

int nb_teste_rand_coefs {} ;

void teste_rand_coefs( int bits )
 {
  double * values = new_rand_coefs(nb_teste_rand_coefs) ; 
  int i ;
  for ( i=0 ; i<nb_teste_rand_coefs ; i++ )
   { teste_approxime(bits,values[i]) ; }
  std::cout<<std::endl ;
  delete [] values ;
 }


//==============================================
// fonction principale
//==============================================


#include <cstdlib>  // for atoi

int main( int argc, char *argv[] )
 {
  if (argc<2) echec(1,"argument manquant sur la ligne de commande") ;
  nb_teste_rand_coefs = atoi(argv[1]) ;
  
  std::cout<<std::endl ;
  
  boucle(2,8,2,teste_065) ;
  boucle(2,8,2,teste_035) ;
  boucle(1,8,1,teste_065_3515_035_4832) ;
  boucle(1,8,1,teste_rand_coefs) ;
  
  return 0 ;
 }

