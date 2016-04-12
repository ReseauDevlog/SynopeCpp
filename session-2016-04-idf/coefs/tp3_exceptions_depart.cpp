
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>


//==============================================
// utilitaires
//==============================================

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


//==============================================
// framework general de test
//==============================================

class Testeur
 {
  public :
  
    Testeur( int resolution )  : resolution_(resolution) {}
    virtual void execute( int bits ) =0 ;
    virtual ~Testeur() {} ;
    
  protected :
  
    void erreur( int bits, double exact, double approx )
     {
      if (exact==0) { echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/"<<resolution_<<")" ;
     }

  private :
  
    int const resolution_ ;

 } ;

class Testeurs
 {
  public :
  
    Testeurs( unsigned int max )
     : max__{max}, indice__{}, testeurs__{new Testeur * [max__]}
     {}
     
    void acquiere( Testeur * t )
     {
      if (indice__==max__) { echec(2,"trop de testeurs") ; }
      testeurs__[indice__] = t ;
      indice__++ ;
     }
     
    unsigned int nb_testeurs() const
     { return indice__ ; }
     
    Testeur * testeur( unsigned i ) const
     {
      if (i>=indice__) { echec(3,"indice de testeur incorrect") ; }
      return testeurs__[i] ;
     }
     
    ~Testeurs()
     {
      for ( unsigned i=0 ; i<max__ ; ++i )
       { delete testeurs__[i] ; }
      delete [] testeurs__ ;
     }
     
  private :
  
    unsigned int max__ ;
    unsigned int indice__ ;
    Testeur * * testeurs__ ;
 } ;

void boucle( int deb, int fin, int inc, const Testeurs & ts )
 {
  unsigned int i ;
  for ( i=0 ; i<ts.nb_testeurs() ; ++i )
   {
    Testeur * t = ts.testeur(i) ;
    std::cout<<std::endl ;
    int bits ;
    for ( bits = deb ; bits <= fin ; bits = bits + inc )
     { t->execute(bits) ; }
   }
 }


//==============================================
// Coef
//==============================================

class Coef
 {
  public :
  
    Coef( unsigned int bits )
     : bits_(bits), numerateur_{}, exposant_{}
     {}
    unsigned int lit_bits() const
     { return bits_ ; }
    void approxime( double valeur )
      {
       numerateur_ = exposant_ = 0 ;
       if (valeur==0) { return ; }
       double min = (entier_max(bits_)+0.5)/2 ;
       while (valeur<min)
        {
         exposant_ = exposant_ + 1 ;
     	valeur = valeur * 2 ;
        }
       numerateur_ = arrondi(valeur) ;
      }
    double approximation() const
      {
       if (exposant_<0) { echec(5,"exposant negatif") ; }
       return (double(numerateur_)/fois_puissance_de_deux(1,exposant_)) ;
      }
    int multiplie( int arg ) const
     { return fois_puissance_de_deux(numerateur_*arg,-exposant_) ; }
    std::string texte() const
     { return std::to_string(numerateur_)+"/2^"+std::to_string(exposant_) ; }

  private :
  
    unsigned int const bits_ ;
    int numerateur_ ;
    int exposant_ ;
 } ;

void affiche( Coef const & c )
 { std::cout << c.texte() ; }


//==============================================
// Testeurs dedies a Coef
//==============================================

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
      erreur(bits,valeur,c.approximation()) ;
      std::cout<<" (" ;
      affiche(c) ;
      std::cout<<")"<<std::endl ;
     }
 } ;

class TesteurCoefO65 : public TesteurCoef
 {
  public :
    TesteurCoefO65( int resolution ) : TesteurCoef(resolution) {}
    virtual void execute( int bits ) { teste(bits,0.65) ; }
 } ;

class TesteurCoefO35 : public TesteurCoef
 {
  public :
    TesteurCoefO35( int resolution ) : TesteurCoef(resolution) {}
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
      Coef coef1(bits), coef2(bits) ;
      int exact, approx ;
      exact = arrondi(c1*e1+c2*e2) ;
      coef1.approxime(c1) ;
      coef2.approxime(c2) ;
      approx = coef1.multiplie(e1) + coef2.multiplie(e2) ;
      erreur(bits,exact,approx) ;
      std::cout<<std::endl ;
     }
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  Testeurs ts(5) ;
  ts.acquiere(new TesteurCoef065(1000000)) ;
  ts.acquiere(new TesteurCoef035(1000000)) ;
  ts.acquiere(new TesteurSomme(1000000)) ;
  boucle(4,16,4,ts) ;
  std::cout<<std::endl ;
  return 0 ;
 }


