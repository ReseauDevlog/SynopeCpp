# -*- coding: utf-8 -*-

test_utilitaires = """
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

"""

simple = """
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

"""

classes = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  int bits ;

  std::cout<<std::endl ;
  TesteurCoef065 tc065 ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { tc065.execute(bits) ; }

  std::cout<<std::endl ;
  TesteurCoef035 tc035 ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { tc035.execute(bits) ; }

  std::cout<<std::endl ;
  TesteurSomme ts ;
  for ( bits = 1 ; bits <= 8 ; bits = bits + 1 )
   { ts.execute(bits) ; }

  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

virtual = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Boucle boucle ;
  boucle.init(2) ;
  boucle.acquiere(new TesteurCoef065) ;
  boucle.acquiere(new TesteurCoef035) ;
  boucle.acquiere(new TesteurSomme) ;
  boucle.execute(1000000,4,16,4) ;
  boucle.finalise() ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

constructeurs_et_statiques = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs::init(3) ;
  Testeurs::acquiere(new TesteurCoef065(1000000)) ;
  Testeurs::acquiere(new TesteurCoef035(1000000)) ;
  Testeurs::acquiere(new TesteurSomme(1000000)) ;
  boucle(4,16,4) ;
  Testeurs::finalise() ;
  std::cout<<std::endl ;
  return 0 ;
 }

"""

pfonctions = """
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

"""

