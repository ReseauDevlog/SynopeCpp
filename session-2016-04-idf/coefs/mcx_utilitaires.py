# -*- coding: utf-8 -*-

simple ="""
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

"""

rand_patch =  """#include <random>

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

"""

simple_rand = simple + rand_patch

compacte = """
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

"""

compacte_rand = compacte + rand_patch

const = """
//==============================================
// utilitaires
//==============================================

#include <iostream>
#include <iomanip>
#include <string>

void echec( unsigned int code, std::string const & commentaire )
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

"""


exception = """
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

"""

gen0 = exception

constexpr = """
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

double arrondi( double d, unsigned precision =0 )
 {
  double mult {1.} ;
  while (precision-->0) mult *= 10. ;
  if (d>0) { return int(d*mult+.5)/mult ; }
  else { return int(d*mult-.5)/mult ; }
 }

constexpr int fois_puissance_de_deux( int nombre, int exposant )
 { return (exposant>0)?(nombre<<exposant):(nombre>>(-exposant)) ; }

constexpr int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }

template<typename T>
constexpr int nombre_bits()
 { return sizeof(T)*8 ; }

"""

traits = """
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

double arrondi( double d, unsigned precision =0 )
 {
  double mult {1.} ;
  while (precision-->0) mult *= 10. ;
  if (d>0) { return int(d*mult+.5)/mult ; }
  else { return int(d*mult-.5)/mult ; }
 }

constexpr int fois_puissance_de_deux( int nombre, int exposant )
 { return (exposant>0)?(nombre<<exposant):(nombre>>(-exposant)) ; }

constexpr int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }

template<typename T> constexpr bool avec_signe() { return true ; }
template<> constexpr bool avec_signe<unsigned int>() { return false ; }
template<> constexpr bool avec_signe<unsigned short>() { return false ; }
template<> constexpr bool avec_signe<unsigned char>() { return false ; }

template<typename T>
constexpr int nombre_bits_hors_signe()
 { return avec_signe<T>()?(sizeof(T)*8-1):(sizeof(T)*8) ; }

"""

