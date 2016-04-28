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

boucle_exposant = """
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

"""

approxime = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  std::cout << std::endl ;
  approxime(0.65) ;
  std::cout << std::endl ;
  approxime(0.35) ;
  std::cout << std::endl ;
  return 0 ;
 }

"""

approxime_max = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  std::cout << std::endl ;
  approxime(15,0.65) ;
  approxime(255,0.65) ;
  std::cout << std::endl ;
  approxime(15,0.35) ;
  approxime(255,0.35) ;
  std::cout << std::endl ;
  return 0 ;
 }

"""

approxime_bits = """
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

"""

teste_approxime = """
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
  return 0 ;
 }

"""

multiplie = """
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
   {
    int exact = arrondi(0.65*3515+0.35*4832) ;
    int approx = multiplie(bits,0.65,3515) + multiplie(bits,0.35,4832) ;
    std::cout << bits << " bits : 0.65*3515+0.35*4832 = " << exact << " ~ " << approx << std::endl ;
   }

  std::cout<<std::endl ;
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

pfonctions = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  std::cout<<std::endl ;
  boucle(2,8,2,teste_065) ;
  boucle(2,8,2,teste_035) ;
  boucle(1,8,1,teste_065_3515_035_4832) ;
  return 0 ;
 }

"""

pfonctions_rand = """
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

"""

pfonctions_ostream = """
//==============================================
// fonction principale
//==============================================

#include <fstream>

int main( int argc, char *argv[] )
 {
  if (argc<3) echec(1,"arguments manquants sur la ligne de commande") ;
  nb_teste_rand_coefs = atoi(argv[1]) ;
  std::ofstream fichier(argv[2]) ;
  sortie = &fichier ;
  
  (*sortie)<<std::endl ;
  
  boucle(2,8,2,teste_065) ;
  boucle(2,8,2,teste_035) ;
  boucle(1,8,1,teste_065_3515_035_4832) ;
  boucle(1,8,1,teste_rand_coefs) ;
  
  fichier.close() ;
  
  return 0 ;
 }

"""

tcoef = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  int bits ;

  std::cout<<std::endl ;
  TesteurCoef tc ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { tc.execute(bits) ; }

  std::cout<<std::endl ;
  for ( bits = 1 ; bits <= 8 ; bits = bits + 1 )
   { teste_somme(bits,0.65,3515,0.35,4832) ; }

  std::cout<<std::endl ;
  return 0 ;
 }

"""

testeurs = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  int bits ;

  std::cout<<std::endl ;
  TesteurCoef tc ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { tc.execute(bits) ; }

  std::cout<<std::endl ;
  TesteurSomme ts ;
  for ( bits = 1 ; bits <= 8 ; bits = bits + 1 )
   { ts.execute(bits) ; }

  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

heritage = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  int bits ;

  std::cout<<std::endl ;
  TesteurCoef065 tc065 ;
  tc065.init(100) ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { tc065.execute(bits) ; }

  std::cout<<std::endl ;
  TesteurCoef035 tc035 ;
  tc035.init(100) ;
  for ( bits = 2 ; bits <= 8 ; bits = bits + 2 )
   { tc035.execute(bits) ; }

  std::cout<<std::endl ;
  TesteurSomme ts ;
  ts.init(1000) ;
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
  TesteurCoef065 tc065 ;
  TesteurCoef035 tc035 ;
  TesteurSomme ts ;
  boucle(tc065,1000000,4,16,4) ;
  boucle(tc035,1000000,4,16,4) ;
  boucle(ts,1000,1,8,1) ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

boucle_foncteur = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  TesteurCoef065 tc065 ;
  TesteurCoef035 tc035 ;
  TesteurSomme ts ;
  Boucle boucle ;
  boucle.execute(tc065,1000000,4,16,4) ;
  boucle.execute(tc035,1000000,4,16,4) ;
  boucle.execute(ts,1000,1,8,1) ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

boucle_conteneur = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  TesteurCoef065 tc065 ;
  TesteurCoef035 tc035 ;
  TesteurSomme ts ;
  Boucle boucle ;
  boucle.copie(0,tc065) ;
  boucle.copie(1,tc035) ;
  boucle.copie(2,ts) ;
  boucle.execute(1000000,4,16,4) ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

conteneur_ptr = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  TesteurCoef065 tc065 ;
  TesteurCoef035 tc035 ;
  TesteurSomme ts ;
  Boucle boucle ;
  boucle.init() ;
  boucle.enregistre(0,&tc065) ;
  boucle.enregistre(1,&tc035) ;
  boucle.enregistre(2,&ts) ;
  boucle.execute(1000000,4,16,4) ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

conteneur_indice = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  TesteurCoef065 tc065 ;
  TesteurCoef035 tc035 ;
  TesteurSomme ts ;
  Boucle boucle ;
  boucle.init() ;
  boucle.enregistre(&tc065) ;
  boucle.enregistre(&tc035) ;
  boucle.enregistre(&ts) ;
  boucle.execute(1000000,4,16,4) ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

conteneur_dyn = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  TesteurCoef065 tc065 ;
  TesteurCoef035 tc035 ;
  TesteurSomme ts ;
  Boucle boucle ;
  boucle.init(3) ;
  boucle.enregistre(&tc065) ;
  boucle.enregistre(&tc035) ;
  boucle.enregistre(&ts) ;
  boucle.execute(1000000,4,16,4) ;
  boucle.finalise() ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

conteneur_owner = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Boucle boucle ;
  boucle.init(3) ;
  boucle.acquiere(new TesteurCoef065) ;
  boucle.acquiere(new TesteurCoef035) ;
  boucle.acquiere(new TesteurSomme) ;
  boucle.execute(1000000,4,16,4) ;
  boucle.finalise() ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

constructeurs_testeurs = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Boucle boucle ;
  boucle.init(3) ;
  boucle.acquiere(new TesteurCoef065(1000000)) ;
  boucle.acquiere(new TesteurCoef035(1000000)) ;
  boucle.acquiere(new TesteurSomme(1000000)) ;
  boucle.execute(4,16,4) ;
  boucle.finalise() ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

constructeurs = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Boucle boucle(3) ;
  boucle.acquiere(new TesteurCoef065(1000000)) ;
  boucle.acquiere(new TesteurCoef035(1000000)) ;
  boucle.acquiere(new TesteurSomme(1000000)) ;
  boucle.execute(4,16,4) ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

conteneur_dedie = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs ts(3) ;
  ts.acquiere(new TesteurCoef065(1000000)) ;
  ts.acquiere(new TesteurCoef035(1000000)) ;
  ts.acquiere(new TesteurSomme(1000000)) ;
  boucle(4,16,4,ts) ;
  std::cout << std::endl ;
  return 0 ;
 }
 
"""

statiques = """
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

catch_check = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts(1) ;
    ts.acquiere(new TesteurCoef065(1000000)) ;
    ts.acquiere(new TesteurCoef035(1000000)) ;
    ts.acquiere(new TesteurSomme(1000000)) ;
    boucle(4,16,4,ts) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

catch = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts(5) ;
    ts.acquiere(new TesteurCoef065(1000000)) ;
    ts.acquiere(new TesteurCoef035(1000000)) ;
    ts.acquiere(new TesteurSomme(1000000)) ;
    boucle(4,16,4,ts) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

gen0 = catch

template = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts(5) ;
    ts.acquiere(new TesteurCoef065<int>(1000000)) ;
    ts.acquiere(new TesteurCoef035<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    boucle(4,16,4,ts) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

shortsomme = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts(5) ;
    ts.acquiere(new TesteurCoef065(1000000)) ;
    ts.acquiere(new TesteurCoef035(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<unsigned short>(1000000)) ;
    boucle(4,16,4,ts) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

shortcoef = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts(5) ;
    ts.acquiere(new TesteurCoef065<int>(1000000)) ;
    ts.acquiere(new TesteurCoef035<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    ts.acquiere(new TesteurCoef065<unsigned short>(1000000)) ;
    ts.acquiere(new TesteurSomme<unsigned short>(1000000)) ;
    boucle(4,16,4,ts) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

uchar = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts(5) ;
    ts.acquiere(new TesteurCoef065<int>(1000000)) ;
    ts.acquiere(new TesteurCoef035<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    ts.acquiere(new TesteurCoef065<unsigned short>(1000000)) ;
    ts.acquiere(new TesteurSomme<unsigned short>(1000000)) ;
    boucle(4,16,4,ts) ;

    Testeurs ts2(1) ;
    ts2.acquiere(new TesteurCoef065<unsigned char>(1000)) ;
    boucle(1,8,1,ts2) ;
    
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

gentesteurs = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs<5> ts ;
    ts.acquiere(new TesteurCoef065<int>(1000000)) ;
    ts.acquiere(new TesteurCoef035<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    ts.acquiere(new TesteurCoef065<unsigned short>(1000000)) ;
    ts.acquiere(new TesteurSomme<unsigned short>(1000000)) ;
    boucle(4,16,4,ts) ;

    Testeurs<1> ts2 ;
    ts2.acquiere(new TesteurCoef065<unsigned char>(1000)) ;
    boucle(1,8,1,ts2) ;
    
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

traits = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs<5> ts ;
    ts.acquiere(new TesteurCoef065<int>(1000000)) ;
    ts.acquiere(new TesteurCoef035<int>(1000000)) ;
    ts.acquiere(new TesteurSomme<int>(1000000)) ;
    ts.acquiere(new TesteurCoef065<short>(1000000)) ;
    ts.acquiere(new TesteurSomme<short>(1000000)) ;
    boucle(4,16,4,ts) ;

    Testeurs<1> ts2 ;
    ts2.acquiere(new TesteurCoef065<unsigned char>(1000)) ;
    boucle(1,8,1,ts2) ;
    
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
	return e.code() ;
   }
 }
 
"""

#=====================================================================
# TP BIBLIO
#=====================================================================

biblio0 = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs<2> ts ;
  ts.acquiere(new TesteurRandCoefs<unsigned char>(1000,1000)) ;
  ts.acquiere(new TesteurSomme<unsigned char>(100)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

vector = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs ts ;
  ts.acquiere(new TesteurRandCoefs<unsigned char>(1000,1000)) ;
  ts.acquiere(new TesteurSomme<unsigned char>(100)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

vector_bavard = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  std::cout<<"===== Debut"<<std::endl ;
  Testeurs ts ;
  std::cout<<"===== TesteurRandCoefs"<<std::endl ;
  ts.acquiere(new TesteurRandCoefs<unsigned char>(1000,1000)) ;
  std::cout<<"===== TesteurSomme"<<std::endl ;
  ts.acquiere(new TesteurSomme<unsigned char>(100)) ;
  std::cout<<"===== Boucle"<<std::endl ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  std::cout<<"===== Fin"<<std::endl ;
  return 0 ;
 }
 
"""

shared = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs ts ;
  ts.acquiere(std::make_shared<TesteurRandCoefs<unsigned char>>(1000,1000)) ;
  ts.acquiere(std::make_shared<TesteurSomme<unsigned char>>(100)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

unique = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs ts ;
  ts.acquiere(std::make_unique<TesteurRandCoefs<unsigned char>>(1000,1000)) ;
  ts.acquiere(std::make_unique<TesteurSomme<unsigned char>>(100)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

direct = """
//==============================================
// fonction principale
//==============================================

int main()
 {
  std::vector<std::unique_ptr<Testeur>> ts ;
  ts.push_back(std::make_unique<TesteurRandCoefs<unsigned char>>(1000,1000)) ;
  ts.push_back(std::make_unique<TesteurSomme<unsigned char>>(100)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

