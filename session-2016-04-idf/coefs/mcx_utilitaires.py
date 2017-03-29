# -*- coding: utf-8 -*-

HEADER = """
//==============================================
// utilitaires
//==============================================
"""

simple = HEADER + """
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

compacte = HEADER + """
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

const = HEADER + """
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


exception = HEADER + """
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

constexpr = HEADER + """
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

traits = HEADER + """
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


#==============================================
# TP BIBLIO
#==============================================

common = """
#include <iostream>
#include <iomanip>
#include <string>
#include <memory>
#include <random>

// émule la fonction std::make_unique qui apparait en C++14
namespace std
 {
  template<typename T, typename... Args>
  std::unique_ptr<T> make_unique(Args&&... args)
   { return std::unique_ptr<T>(new T(std::forward<Args>(args)...)) ; }
 }

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
"""

biblio = HEADER + common + """
// crée sur le tas un tableau dynamique de coefficients
double * new_rand_coefs( int taille )
 {
  std::random_device rd ;
  std::mt19937 gen(rd()) ;
  std::uniform_real_distribution<> dis(0,1) ;
  
  double * res = new double [taille] ;
  for ( int i=0 ; i<taille ; i++ )
   { res[i] = dis(gen) ; }
  return res ;
 }

"""

pointeur = biblio + """
template<typename Valeur>
class Pointeur
 {
  public :
    Pointeur( Valeur * val ) : val_{val} {}
    Valeur & operator*() const { return *val_ ; } 
    Valeur * operator->() const { return val_ ; } 
    ~Pointeur() { delete val_ ; }
  private :
    Valeur * val_ ;
 } ;
 
"""

pointeur_bavard = biblio + """
template<typename Valeur>
class Pointeur
 {
  public :
    Pointeur( Valeur * val ) : val_{val}
     { std::cout<<"(pointeur : construit "<<this<<"->"<<val_<<")"<<std::endl ; }
    Pointeur( Pointeur const & ptr ) : val_{ptr.val_}
     { std::cout<<"(pointeur : copie "<<(&ptr)<<"->"<<val_<<" vers "<<this<<"->"<<val_<<")"<<std::endl ; }
    void operator=( Pointeur const & ptr )
     {
      val_ = ptr.val_ ;
      std::cout<<"(pointeur : affecte "<<(&ptr)<<"->"<<val_<<" vers "<<this<<"->"<<val_<<")"<<std::endl ;
     }
    Valeur & operator*() const
     { std::cout<<"(pointeur : accede "<<this<<"->"<<val_<<")"<<std::endl ; return *val_ ; } 
    Valeur * operator->() const 
     { std::cout<<"(pointeur : accede "<<this<<"->"<<val_<<")"<<std::endl ; return val_ ; } 
    Valeur * get() const
     { return val_ ; } 
    ~Pointeur()
     {  std::cout<<"(pointeur : detruit "<<this<<"->"<<val_<<")"<<std::endl ; /*delete val_*/ ; }
  private :
    Valeur * val_ ;
 } ;
 
"""

auto_pointeur = biblio + """
template<typename Valeur>
class Pointeur
 {
  public :
    Pointeur( Valeur * val ) : val_{val} {}
    Pointeur( Pointeur const & ptr ) = delete ;
    void operator=( Pointeur const & ptr ) = delete ;
    Pointeur( Pointeur && ptr ) : val_{ptr.val_} { ptr.val_ = nullptr ; }
    void operator=( Pointeur && ptr ) { val_ = ptr.val_ ; ptr.val_ = nullptr ; }
    Valeur & operator*() const { return *val_ ; } 
    Valeur * operator->() const { return val_ ; } 
    ~Pointeur() { delete val_ ; }
  private :
    Valeur * val_ ;
 } ;
 
"""

auto_pointeur_bavard = biblio + """
template<typename Valeur>
class Pointeur
 {
  public :
    Pointeur( Valeur * val ) : val_{val}
     { std::cout<<"(pointeur : construit "<<this<<"->"<<val_<<")"<<std::endl ; }
    Pointeur( Pointeur const & ptr ) = delete ;
    void operator=( Pointeur const & ptr ) = delete ;
    Pointeur( Pointeur && ptr ) : val_{ptr.val_}
     {
      ptr.val_ = nullptr ;
      std::cout<<"(pointeur : deplace "<<(&ptr)<<"->"<<val_<<" vers "<<this<<"->"<<val_<<")"<<std::endl ;
     }
    void operator=( Pointeur && ptr )
     {
      val_ = ptr.val_ ; ptr.val_ = nullptr ;
      std::cout<<"(pointeur : deplace "<<(&ptr)<<"->"<<val_<<" vers "<<this<<"->"<<val_<<")"<<std::endl ;
     }
    Valeur & operator*() const
     { std::cout<<"(pointeur : accede "<<this<<"->"<<val_<<")"<<std::endl ; return *val_ ; } 
    Valeur * operator->() const 
     { std::cout<<"(pointeur : accede "<<this<<"->"<<val_<<")"<<std::endl ; return val_ ; } 
    Valeur * get() const
     { return val_ ; } 
    ~Pointeur()
     {  std::cout<<"(pointeur : detruit "<<this<<"->"<<val_<<")"<<std::endl ; /*delete val_*/ ; }
  private :
    Valeur * val_ ;
 } ;
 
"""


#==============================================
# TP PARALLELE
#==============================================

parallele = HEADER + common + """
class RandCoefs
 {
  public :
    RandCoefs() : rd_{}, gen_{rd_()}, dis_(0,1) {}
    double operator()()
     { return dis_(gen_) ; }
  private :
    std::random_device rd_ ;
    std::mt19937 gen_ ;
    std::uniform_real_distribution<> dis_ ;
 } ;


"""

