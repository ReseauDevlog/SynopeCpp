# -*- coding: utf-8 -*-

HEADER = """
//==============================================
// fonction principale
//==============================================

"""

test_utilitaires = HEADER + """
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

boucle_exposant = HEADER + """
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

approxime = HEADER + """
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

approxime_max = HEADER + """
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

approxime_bits = HEADER + """
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

teste_approxime = HEADER + """
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

multiplie = HEADER + """
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

simple = HEADER + """
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

pfonctions = HEADER + """
int main()
 {
  std::cout<<std::endl ;
  boucle(2,8,2,teste_065) ;
  boucle(2,8,2,teste_035) ;
  boucle(1,8,1,teste_065_3515_035_4832) ;
  return 0 ;
 }

"""

pfonctions_rand = HEADER + """
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

pfonctions_ostream = HEADER + """
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

tcoef = HEADER + """
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

testeurs = HEADER + """
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

heritage = HEADER + """
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

virtual = HEADER + """
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

boucle_foncteur = HEADER + """
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

boucle_conteneur = HEADER + """
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

conteneur_ptr = HEADER + """
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

conteneur_indice = HEADER + """
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

conteneur_dyn = HEADER + """
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

conteneur_owner = HEADER + """
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

constructeurs_testeurs = HEADER + """
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

constructeurs = HEADER + """
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

conteneur_dedie = HEADER + """
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

statiques = HEADER + """
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

catch_check = HEADER + """
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

catch = HEADER + """
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

template = HEADER + """
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

shortsomme = HEADER + """
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

shortcoef = HEADER + """
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

uchar = HEADER + """
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

gentesteurs = HEADER + """
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

traits = HEADER + """
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

biblio = HEADER + """
int main()
 {
  Testeurs<2> ts ;
  ts.acquiere(new TesteurCoefs<unsigned char>(1000,1000)) ;
  ts.acquiere(new TesteurSommes<unsigned char>(1000,1000)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

vector = HEADER + """
int main()
 {
  Testeurs ts ;
  ts.acquiere(new TesteurCoefs<unsigned char>(1000,1000)) ;
  ts.acquiere(new TesteurSommes<unsigned char>(1000,1000)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

vector_bavard = HEADER + """
int main()
 {
  std::cout<<"===== Debut"<<std::endl ;
  Testeurs ts ;
  std::cout<<"===== TesteurCoefs"<<std::endl ;
  ts.acquiere(new TesteurCoefs<unsigned char>(1000,1000)) ;
  std::cout<<"===== TesteurSommes"<<std::endl ;
  ts.acquiere(new TesteurSommes<unsigned char>(1000,1000)) ;
  std::cout<<"===== Boucle"<<std::endl ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  std::cout<<"===== Fin"<<std::endl ;
  return 0 ;
 }
 
"""

shared = HEADER + """
int main()
 {
  Testeurs ts ;
  ts.acquiere(std::make_shared<TesteurCoefs<unsigned char>>(1000,1000)) ;
  ts.acquiere(std::make_shared<TesteurSommes<unsigned char>>(1000,1000)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

unique = HEADER + """
int main()
 {
  Testeurs ts ;
  ts.acquiere(std::make_unique<TesteurCoefs<unsigned char>>(1000,1000)) ;
  ts.acquiere(std::make_unique<TesteurSommes<unsigned char>>(1000,1000)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""

direct = HEADER + """
int main()
 {
  std::vector<std::unique_ptr<RandTesteur>> ts ;
  ts.push_back(std::make_unique<TesteurCoefs<unsigned char>>(1000,1000)) ;
  ts.push_back(std::make_unique<TesteurSommes<unsigned char>>(1000,1000)) ;
  boucle(1,8,1,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }
 
"""


#=====================================================================
# TP PARALLELE
#=====================================================================

parallele = HEADER + """
#include <chrono>

int main()
 {
  std::chrono::time_point<std::chrono::steady_clock> debut = std::chrono::steady_clock::now() ;

  constexpr int SIZE = 1000000 ;
  std::vector<std::unique_ptr<RandTesteur<SIZE>>> ts ;
  ts.push_back(std::make_unique<TesteurCoefs<unsigned char,SIZE>>(1000)) ;
  ts.push_back(std::make_unique<TesteurSommes<unsigned char,SIZE>>(1000)) ;
  boucle(1,8,1,ts) ;
  
  std::chrono::time_point<std::chrono::steady_clock> fin = std::chrono::steady_clock::now() ;
  std::chrono::milliseconds temps = std::chrono::duration_cast<std::chrono::milliseconds>(fin - debut) ;
  
  std::cout<<"\\ntemps ecoule : "<<temps.count()<<" ms\\n"<<std::endl ;
  
  return 0 ;
 }
 
"""

main1 = """
#include <chrono>

int main()
 {
  using namespace std ;
  using namespace chrono ;
  
  auto debut = steady_clock::now() ;

  constexpr int SIZE = """
  
main2 = """ ;
  vector<unique_ptr<RandTesteur<SIZE>>> ts ;
  ts.push_back(make_unique<TesteurCoefs<unsigned char,SIZE>>(1000)) ;
  ts.push_back(make_unique<TesteurSommes<unsigned char,SIZE>>(1000)) ;
  boucle(1,8,1,ts) ;
  
  auto fin = steady_clock::now() ;
  auto temps = duration_cast<milliseconds>(fin - debut) ;
  
  std::cout<<"\\ntemps ecoule : "<<temps.count()<<" ms\\n"<<std::endl ;
  
  return 0 ;
 }
 
"""

auto = HEADER + main1 + "1000000" + main2
stress = HEADER + main1 + "100000" + main2
mutex = HEADER + main1 + "10000" + main2
