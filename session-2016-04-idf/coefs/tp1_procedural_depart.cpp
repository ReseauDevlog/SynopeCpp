

#include <iostream>
#include <string>
#include <cstdlib>


//==============================================
// utilitaires
//==============================================

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
unsigned fois_puissance_de_deux( unsigned nombre, int exposant )
 {
  while (exposant>0)
   { nombre *= 2 ; exposant -= 1 ; }
  while (exposant<0)
   { nombre /= 2 ; exposant += 1 ; }
  return nombre ; 
 }

// entier maximum représentable avec "nombre_bits" bits
unsigned entier_max( unsigned int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }


//==============================================
// fonction principale
//==============================================

int main()
 {
  // tests sur arrondi()
  if (arrondi(-0.75)!=-1) echec(1,"arrondi(-0.75)!=-1") ;
  if (arrondi(-0.25)!=0) echec(1,"arrondi(-0.25)!=0") ;
  if (arrondi(+0.25)!=0) echec(1,"arrondi(0.25)!=0") ;
  if (arrondi(+0.75)!=1) echec(1,"arrondi(0.75)!=1") ;

  // tests sur fois_puissance_de_deux()
  if (fois_puissance_de_deux(1,3)!=8) echec(2,"fois_puissance_de_deux(1,3)!=8") ;
  if (fois_puissance_de_deux(3,2)!=12) echec(2,"fois_puissance_de_deux3,2)!=12") ;
  if (fois_puissance_de_deux(10,-1)!=5) echec(2,"fois_puissance_de_deux(10,-1)!=5") ;
     std::cout << "MAX " << entier_max(32) <<std::endl ;

  // tests sur entier_max()
  if (entier_max(8)!=255) echec(3,"entier_max(8)!=255") ;
  if (entier_max(16)!=65535) echec(3,"entier_max(16)!=65535") ;
  if (entier_max(32)!=255) echec(3,"entier_max(32)!=255") ;
  
  // approximation de 0.65 par num1/2^1
  int num1 = arrondi(0.65*fois_puissance_de_deux(1,1))  ;
  std::cout << "0.65 ~ " << num1 << "/2^1 (" << num1/2. << ")" <<std::endl ;
  
  // approximation de 0.65 par num2/2^2
  int num2 = arrondi(0.65*fois_puissance_de_deux(1,2))  ;
  std::cout << "0.65 ~ " << num2 << "/2^2 (" << num2/4. << ")" <<std::endl ;
  
  // approximation de 0.65 par num3/2^3
  int num3 = arrondi(0.65*fois_puissance_de_deux(1,3))  ;
  std::cout << "0.65 ~ " << num3 << "/2^3 (" << num3/8. << ")" <<std::endl ;
  
  std::cout << std::endl ;
  
  // calcul de 0.65*3515 en utilisant les approximations
  // de 0.65 ci-dessus, et des calculs à bases d'entiers,
  // via la fonction fois_puissance_de_deux().
  std::cout << "0.65*3515 ~ " << fois_puissance_de_deux(num1*3515,-1) << std::endl ;
  std::cout << "0.65*3515 ~ " << fois_puissance_de_deux(num2*3515,-2) << std::endl ;
  std::cout << "0.65*3515 ~ " << fois_puissance_de_deux(num3*3515,-3) << std::endl ;
     
  // calcul de 0.65*3515 en utilisant des flottants
  std::cout << "0.65*3515 = " << arrondi(0.65*3515) << std::endl ;
 
  std::cout << std::endl ;
  
  return 0 ;
 }
