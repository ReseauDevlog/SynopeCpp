# -*- coding: utf-8 -*-

HEADER = """
//==============================================
// tests
//==============================================
"""

approxime = HEADER + """
void teste_approxime( int bits, double valeur )
 {
  int numerateur, exposant, erreur ;
  approxime(bits,valeur,numerateur,exposant) ;
  double approximation = double(numerateur)/fois_puissance_de_deux(1,exposant) ;
  erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    << bits << " bits : " << valeur << " ~ "
    << std::setw(8) << approximation
    <<" ("<<erreur<<"/100)"
    <<" ("<<numerateur<<"/2^"<<exposant<<")"
    <<std::endl ;
 }

"""

simple =  HEADER + """
void teste_approxime( int bits, double valeur )
 {
  int numerateur, exposant, erreur ;
  approxime(bits,valeur,numerateur,exposant) ;
  double approximation = double(numerateur)/fois_puissance_de_deux(1,exposant) ;
  erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
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
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

"""

fonctions =  HEADER + """
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

"""

fonctions_rand =  HEADER + """
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

"""

fonctions_ostream =  HEADER + """
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
  (*sortie)<<std::endl ;
  delete [] values ;
 }

"""

struct =  HEADER + """
void teste_approxime( int bits, double valeur )
 {
  Coef coef ;
  int erreur ;
  approxime(bits,valeur,coef) ;
  double approximation = double(coef.numerateur_)/fois_puissance_de_deux(1,coef.exposant_) ;
  erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
    <<" ("<<erreur<<"/100)"
    <<" ("<<coef.numerateur_<<"/2^"<<coef.exposant_<<")"
    <<std::endl ;
 }

void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  int exact, approx, erreur ;
  exact = arrondi(c1*e1+c2*e2) ;
  approx = multiplie(bits,c1,e1) + multiplie(bits,c2,e2) ;
  erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

"""

retour =  HEADER + """
void teste_approxime( int bits, double valeur )
 {
  int erreur ;
  Coef coef = approxime(bits,valeur) ;
  double approximation = double(coef.numerateur_)/fois_puissance_de_deux(1,coef.exposant_) ;
  erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
    <<" ("<<erreur<<"/100)"
    <<" ("<<coef.numerateur_<<"/2^"<<coef.exposant_<<")"
    <<std::endl ;
 }

void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  int exact, approx, erreur ;
  exact = arrondi(c1*e1+c2*e2) ;
  approx = multiplie(bits,c1,e1) + multiplie(bits,c2,e2) ;
  erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

"""

coef =  HEADER + """
void teste_approxime( int bits, double valeur )
 {
  Coef coef ;
  coef.approxime(bits,valeur) ;
  double approximation = coef.approximation() ;
  int erreur = arrondi(100*(valeur-approximation)/valeur) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
    <<" ("<<erreur<<"/100)"
    <<" ("<<coef.numerateur()<<"/2^"<<coef.exposant()<<")"
    <<std::endl ;
 }

void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  Coef coef1, coef2 ;
  coef1.approxime(bits,c1) ;
  coef2.approxime(bits,c2) ;
  int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
  int exact = arrondi(c1*e1+c2*e2) ;
  int erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

"""

tcoef =  HEADER + """
class TesteurCoef
 {
  public :
  
    void execute( int bits )
     {
      teste(bits,0.65) ;
      teste(bits,0.35) ;
     }

  private :
  
    void teste( int bits, double valeur )
     {
      Coef coef ;
      coef.approxime(bits,valeur) ;
      double approximation = coef.approximation() ;
      int erreur = arrondi(100*(valeur-approximation)/valeur) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
        <<" ("<<erreur<<"/100)"
        <<" ("<<coef.numerateur()<<"/2^"<<coef.exposant()<<")"
        <<std::endl ;
     }
    
 } ;
  
void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  Coef coef1, coef2 ;
  coef1.approxime(bits,c1) ;
  coef2.approxime(bits,c2) ;
  int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
  int exact = arrondi(c1*e1+c2*e2) ;
  int erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

"""

tcoefbits =  HEADER + """
class TesteurCoef
 {
  public :
  
    void execute( int bits )
     {
      teste(bits,0.65) ;
      teste(bits,0.35) ;
     }

  private :
  
    void teste( int bits, double valeur )
     {
      Coef coef ;
      coef.init(bits) ;
      coef.approxime(valeur) ;
      double approximation = coef.approximation() ;
      int erreur = arrondi(100*(valeur-approximation)/valeur) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
        <<" ("<<erreur<<"/100)"
        <<" ("<<coef.numerateur()<<"/2^"<<coef.exposant()<<")"
        <<std::endl ;
     }
    
 } ;
  
void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  Coef coef1, coef2 ;
  coef1.init(bits) ;
  coef1.approxime(c1) ;
  coef2.init(bits) ;
  coef2.approxime(c2) ;
  int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
  int exact = arrondi(c1*e1+c2*e2) ;
  int erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

"""

tcoefatt =  HEADER + """
class TesteurCoef
 {
  public :
  
    void execute( int bits )
     {
      c_.init(bits) ;
      teste(0.65) ;
      teste(0.35) ;
     }

  private :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      int erreur = arrondi(100*(valeur-approximation)/valeur) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<c_.lit_bits()<<" bits : "
        <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
        <<" ("<<erreur<<"/100)"
        <<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"
        <<std::endl ;
     }
    
    Coef c_ ;

 } ;
  
void teste_somme( int bits, double c1, int e1, double c2, int e2 )
 {
  Coef coef1, coef2 ;
  coef1.init(bits) ;
  coef1.approxime(c1) ;
  coef2.init(bits) ;
  coef2.approxime(c2) ;
  int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
  int exact = arrondi(c1*e1+c2*e2) ;
  int erreur = arrondi(1000*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/1000)"<<std::endl ;
 }

"""

testeurs =  HEADER + """
class TesteurCoef
 {
  public :
  
    void execute( int bits )
     {
      c_.init(bits) ;
      teste(0.65) ;
      teste(0.35) ;
     }

  private :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      int erreur = arrondi(100*(valeur-approximation)/valeur) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<c_.lit_bits()<<" bits : "
        <<std::left<<valeur<<" ~ "<<std::setw(8)<<arrondi(approximation,6)
        <<" ("<<erreur<<"/100)"
        <<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"
        <<std::endl ;
     }
    
    Coef c_ ;

 } ;
 
class TesteurSomme
 {
  public :
    void execute( int bits )
     {
      c1_.init(bits) ;
      c2_.init(bits) ;
      teste(0.65,3515,0.35,4832) ;
     }
  private :
    void teste( double c1, int e1, double c2, int e2 )
     {
      c1_.approxime(c1) ;
      c2_.approxime(c2) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      approx = c1_.multiplie(e1) + c2_.multiplie(e2) ;
      int erreur = arrondi(1000*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<c1_.lit_bits()<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/1000)"<<std::endl ;
     }
    Coef c1_ ;
    Coef c2_ ;
 } ;

"""

erreur =  HEADER + """
class TesteurCoef
 {
  public :
  
    void execute( int bits )
     {
      c_.init(bits) ;
      teste(0.65) ;
      teste(0.35) ;
     }

  private :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      erreur(c_.lit_bits(),valeur,approximation,100) ;
      std::cout<<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"<<std::endl ;
     }
    
    Coef c_ ;

 } ;
 
class TesteurSomme
 {
  public :
    void execute( int bits )
     {
      c1_.init(bits) ;
      c2_.init(bits) ;
      teste(0.65,3515,0.35,4832) ;
     }
  private :
    void teste( double c1, int e1, double c2, int e2 )
     {
      c1_.approxime(c1) ;
      c2_.approxime(c2) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      approx = c1_.multiplie(e1) + c2_.multiplie(e2) ;
      erreur(c1_.lit_bits(),exact,approx,1000) ;
      std::cout<<std::endl ;
     }
    Coef c1_ ;
    Coef c2_ ;
 } ;

"""

heritage =  HEADER + """
class TesteurCoef : public Testeur
 {
  protected :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      erreur(c_.lit_bits(),valeur,approximation) ;
      std::cout<<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"<<std::endl ;
     }
    
    Coef c_ ;

 } ;
 
class TesteurCoef065 : public TesteurCoef
 {
  public :
    void execute( int bits )
     { c_.init(bits) ; teste(0.65) ;  }
 } ;
 
class TesteurCoef035 : public TesteurCoef
 {
  public :
    void execute( int bits )
     { c_.init(bits) ; teste(0.35) ;  }
 } ;
 
class TesteurSomme : public Testeur
 {
  public :
    void execute( int bits )
     {
      c1_.init(bits) ;
      c2_.init(bits) ;
      teste(0.65,3515,0.35,4832) ;
     }
  private :
    void teste( double c1, int e1, double c2, int e2 )
     {
      c1_.approxime(c1) ;
      c2_.approxime(c2) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      approx = c1_.multiplie(e1) + c2_.multiplie(e2) ;
      erreur(c1_.lit_bits(),exact,approx) ;
      std::cout<<std::endl ;
     }
    Coef c1_ ;
    Coef c2_ ;
 } ;

"""

virtual =  HEADER + """
class TesteurCoef : public Testeur
 {
  protected :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      erreur(c_.lit_bits(),valeur,approximation) ;
      std::cout<<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"<<std::endl ;
     }
    
    Coef c_ ;
 } ;
 
class TesteurCoef065 : public TesteurCoef
 {
  public :
    virtual void execute( int bits ) { c_.init(bits) ; teste(0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    virtual void execute( int bits ) { c_.init(bits) ; teste(0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :
    virtual void execute( int bits )
     {
      c1_.init(bits) ;
      c2_.init(bits) ;
      teste(0.65,3515,0.35,4832) ;
     }
  private :
    void teste( double c1, int e1, double c2, int e2 )
     {
      c1_.approxime(c1) ;
      c2_.approxime(c2) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      approx = c1_.multiplie(e1) + c2_.multiplie(e2) ;
      erreur(c1_.lit_bits(),exact,approx) ;
      std::cout<<std::endl ;
     }
    Coef c1_ ;
    Coef c2_ ;
 } ;

"""


constructeurs_derives =  HEADER + """
class TesteurCoef : public Testeur
 {
  protected :
  
    void teste( double valeur )
     {
      c_.approxime(valeur) ;
      double approximation = c_.approximation() ;
      erreur(c_.lit_bits(),valeur,approximation) ;
      std::cout<<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"<<std::endl ;
     }
    
    Coef c_ ;
 } ;
 
class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) { init(resolution) ; }
    virtual void execute( int bits ) { c_.init(bits) ; teste(0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) { init(resolution) ; }
    virtual void execute( int bits ) { c_.init(bits) ; teste(0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :
    TesteurSomme( int resolution )
     { init(resolution) ; }
    virtual void execute( int bits )
     {
      c1_.init(bits) ;
      c2_.init(bits) ;
      teste(0.65,3515,0.35,4832) ;
     }
  private :
    void teste( double c1, int e1, double c2, int e2 )
     {
      c1_.approxime(c1) ;
      c2_.approxime(c2) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      approx = c1_.multiplie(e1) + c2_.multiplie(e2) ;
      erreur(c1_.lit_bits(),exact,approx) ;
      std::cout<<std::endl ;
     }
    Coef c1_ ;
    Coef c2_ ;
 } ;

"""

constructeurs_testeurs =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      c_.approxime(valeur) ;
      erreur(bits,valeur,arrondi(c_.approximation(),6)) ;
      std::cout<<" ("<<c_.numerateur()<<"/2^"<<c_.exposant()<<")"<<std::endl ;
     }

    Coef c_ ;
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     {
      c1_.init(bits) ;
      c2_.init(bits) ;
      teste(0.65,3515,0.35,4832) ;
     }

  private :
  
    void teste( double c1, int e1, double c2, int e2 )
     {
      c1_.approxime(c1) ;
      c2_.approxime(c2) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      approx = c1_.multiplie(e1) + c2_.multiplie(e2) ;
      erreur(c1_.lit_bits(),exact,approx) ;
      std::cout<<std::endl ;
     }

    Coef c1_ ;
    Coef c2_ ;
 } ;

"""

constructeurs =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c.approxime(valeur) ;
      erreur(bits,valeur,arrondi(c.approximation(),6)) ;
      std::cout<<" ("<<c.numerateur()<<"/2^"<<c.exposant()<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1.approxime(c1) ;
      coef2.approxime(c2) ;
      int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

affiche =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c.approxime(valeur) ;
      erreur(bits,valeur,arrondi(c.approximation(),6)) ;
      std::cout<<" (" ;
      affiche(c) ;
      std::cout<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1.approxime(c1) ;
      coef2.approxime(c2) ;
      int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

bug =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c.approxime(valeur) ;
      erreur(bits,valeur,arrondi(c.approximation(),6)) ;
      std::cout<<" (" ;
      affiche(c) ;
      std::cout<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1.approxime(c1) ;
      coef2.approxime(c2) ;
      int approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

opmult =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c.approxime(valeur) ;
      erreur(bits,valeur,arrondi(c.approximation(),6)) ;
      std::cout<<" (" ;
      affiche(c) ;
      std::cout<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1.approxime(c1) ;
      coef2.approxime(c2) ;
      int approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

opaffect =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c.approximation(),6)) ;
      std::cout<<" (" ;
      affiche(c) ;
      std::cout<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      int approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

ostream =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c.approximation(),6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      int approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

opdouble =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c,6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void execute( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      int approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

opexec =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c,6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void operator()( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      int approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

gen0 = opexec

coefint =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef<int> c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c,6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.35) ; }
 } ;

class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void operator()( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, int e1, double c2, int e2 )
     {
      int exact = arrondi(c1*e1+c2*e2) ;
      Coef<int> coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      int approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

gensomme =  HEADER + """
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef<int> c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c,6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

class TesteurCoef065 : public TesteurCoef
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoef035 : public TesteurCoef
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef(resolution) {}
    virtual void operator()( int bits ) { teste(bits,0.35) ; }
 } ;

template<typename U>
class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void operator()( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, U e1, double c2, U e2 )
     {
      U exact = arrondi(c1*e1+c2*e2) ;
      Coef<U> coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      U approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

gencoef =  HEADER + """
template<typename U>
class TesteurCoef : public Testeur
 {
  public :
  
    TesteurCoef( int resolution )
     : Testeur(resolution)
     {}

  protected :
  
    void teste( int bits, double valeur )
     {
      Coef<U> c(bits) ;
      c = valeur ;
      erreur(bits,valeur,arrondi(c,6)) ;
      std::cout<<" ("<<c<<")"<<std::endl ;
     }
 } ;

template<typename U>
class TesteurCoef065 : public TesteurCoef<U>
 {
  public :
    TesteurCoef065( int resolution ) : TesteurCoef<U>(resolution) {}
    virtual void operator()( int bits ) { this->teste(bits,0.65) ; }
 } ;

template<typename U>
class TesteurCoef035 : public TesteurCoef<U>
 {
  public :
    TesteurCoef035( int resolution ) : TesteurCoef<U>(resolution) {}
    virtual void operator()( int bits ) { this->teste(bits,0.35) ; }
 } ;

template<typename U>
class TesteurSomme : public Testeur
 {
  public :

    TesteurSomme( int resolution )
     : Testeur(resolution)
     {}

    virtual void operator()( int bits )
     { teste(bits,0.65,3515,0.35,4832) ; }

  private :
  
    void teste( int bits, double c1, U e1, double c2, U e2 )
     {
      U exact = arrondi(c1*e1+c2*e2) ;
      Coef<U> coef1(bits), coef2(bits) ;
      coef1 = c1 ;
      coef2 = c2 ;
      U approx = coef1*e1 + coef2*e2 ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;

"""

#=====================================================================
# TP BIBLIO
#=====================================================================

biblio =  HEADER + """
template<typename U>
class TesteurCoefs : public RandTesteur
 {
  public :
    TesteurCoefs( int nb, int resolution )
     : RandTesteur(nb,resolution,8) {}
    virtual void execute( int bits )
     {
      Coef<U> c(bits) ;
      for ( int i=0 ; i<nb_ ; ++i )
       {
        c = num_[i] ;
        exact_[i] = num_[i] ;
        approx_[i] = arrondi(c,6) ;
       }
      erreur(bits) ;
     }
 } ;

template<typename U>
class TesteurSommes : public RandTesteur
 {
  public :
    TesteurSommes( int nb, int resolution )
     : RandTesteur(nb,resolution,7) {}
    virtual void execute( int bits )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      for ( int i=0 ; i<nb_ ; ++i )
       {
        coef1 = num_[i] ; coef2 = (1-num_[i]) ;
        exact_[i] = 200. ;
        approx_[i] = arrondi(coef1*U(exact_[i]) + coef2*U(exact_[i]),3) ;
       }
      erreur(bits) ;
     }
 } ;

"""


#=====================================================================
# TP PARALLELE
#=====================================================================

parallele =  HEADER + """
template<typename U, int SIZE>
class TesteurCoefs : public RandTesteur<SIZE>
 {
  public :
    TesteurCoefs( int resolution )
     : RandTesteur<SIZE>(resolution,8) {}
    virtual void execute( int bits, double coef, double & exact, double & approx )
     {
      Coef<U> c(bits) ;
      c = coef ;
      exact =coef ;
      approx = arrondi(c,6) ;
     }
 } ;

template<typename U, int SIZE>
class TesteurSommes : public RandTesteur<SIZE>
 {
  public :
    TesteurSommes( int resolution )
     : RandTesteur<SIZE>(resolution,7) {}
    virtual void execute( int bits, double coef, double & exact, double & approx )
     {
      Coef<U> coef1(bits), coef2(bits) ;
      coef1 = coef ; coef2 = (1-coef) ;
      exact = 200. ;
      approx = arrondi(coef1*U(exact) + coef2*U(exact),3) ;
     }
 } ;

"""


