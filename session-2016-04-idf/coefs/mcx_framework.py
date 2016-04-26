# -*- coding: utf-8 -*-

pfonctions = """
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

"""

pfonctions_ostream = """
//==============================================
// framework general de test
//==============================================

std::ostream * sortie {} ;

void boucle( int deb, int fin, int inc, void (*f)( int ) )
 {
  int bits ;
  for ( bits = deb ; bits <= fin ; bits += inc )
   { f(bits) ; }
  (*sortie)<<std::endl ;
 }

"""

erreur = """
//==============================================
// framework general de test
//==============================================

void erreur( int bits, double exact, double approx, int resolution )
 {
  int erreur = arrondi(resolution*double(exact-approx)/exact) ;
  if (erreur<0) { erreur = -erreur ; }
  std::cout
    <<std::right<<std::setw(2)<<bits<<" bits : "
    <<std::left<<exact<<" ~ "<<approx
    <<" ("<<erreur<<"/"<<resolution<<")" ;
 }
 
"""

testeur = """
//==============================================
// framework general de test
//==============================================

class Testeur
 {

  public :

    void init( int resolution )
     { resolution_ = resolution ; }
    
  protected :

    void erreur( int bits, double exact, double approx )
     {
      int erreur = arrondi(resolution_*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/"<<resolution_<<")" ;
     }
    
  private :

    int resolution_ ;
 } ;

"""

virtual = """
//==============================================
// framework general de test
//==============================================

class Testeur
 {

  public :

    void init( int resolution )
     { resolution_ = resolution ; }
    
    virtual void execute( int bits )
     { std::cout << "Mais qu'est-ce que je fais là ?" << std::endl ; }

  protected :
  
    void erreur( int bits, double exact, double approx )
     {
      int erreur = arrondi(resolution_*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/"<<resolution_<<")" ;
     }
    
  private :

    int resolution_ ;
 } ;

void boucle( Testeur & testeur, int resolution, int debut, int fin, int inc )
 {
  std::cout<<std::endl ;
  testeur.init(resolution) ;
  for ( int bits =debut ; bits <= fin ; bits = bits + inc )
   { testeur.execute(bits) ; }
 }
 
"""

classe_boucle = """
//==============================================
// framework general de test
//==============================================

class Testeur
 {

  public :

    void init( int resolution )
     { resolution_ = resolution ; }
    
    virtual void execute( int bits )
     { std::cout << "Mais qu'est-ce que je fais là ?" << std::endl ; }

  protected :
  
    void erreur( int bits, double exact, double approx )
     {
      int erreur = arrondi(resolution_*double(exact-approx)/exact) ;
      if (erreur<0) { erreur = -erreur ; }
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
        <<std::left<<exact<<" ~ "<<approx
        <<" ("<<erreur<<"/"<<resolution_<<")" ;
     }
    
  private :

    int resolution_ ;
 } ;

class Boucle
 {
  public :
    void init( int taille )
     {
      taille_ = taille ;
      indice_ = 0 ;
      testeurs_ = new Testeur * [taille_] ;
     }
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { echec(10,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    void execute( int resolution, int debut, int fin, int inc )
     {
      for ( int i=0; i<indice_ ; i++ )
       {
        if (testeurs_[i]!=nullptr)
         {
          std::cout<<std::endl ;
          testeurs_[i]->init(resolution) ;
          for ( int bits =debut ; bits <= fin ; bits = bits + inc )
           { testeurs_[i]->execute(bits) ; }
         }
       }
     }
    void finalise()
     {
      for ( int i=0; i<indice_ ; i++ )
       { delete testeurs_[i] ; }
      delete [] testeurs_ ;
     }
    
  private :
  
    int taille_ ;
    int indice_ ;
    Testeur * * testeurs_ ;
    
 } ;
 
"""

constructeurs_et_statiques = """
//==============================================
// framework general de test
//==============================================

class Testeur ;

class Testeur
 {
  public :
  
    Testeur( int resolution )
     : resolution_(resolution)
     {}
    
    virtual void execute( int bits )
     { std::cout << "Qu'est-ce que je fais la ??" << std::endl ; }
        
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
  
    static void init( unsigned int max )
     {
      max__ = max ;
      indice__ = 0 ;
      testeurs__ = new Testeur * [max__] ;
     }
     
    static void acquiere( Testeur * t )
     {
      if (indice__==max__) { echec(1,"trop de testeurs") ; }
      testeurs__[indice__] = t ;
      indice__++ ;
     }
     
    static unsigned int nb_testeurs()
     { return indice__ ; }
     
    static Testeur * testeur( unsigned int i )
     {
      if (i>=indice__) { echec(1,"indice de testeur incorrect") ; }
      return testeurs__[i] ;
     }
     
    static void finalise()
     {
      for ( unsigned int i=0 ; i<indice__ ; ++i )
       { delete testeurs__[i] ; }
      delete [] testeurs__ ;
     }
     
  private :
  
    static Testeur * * testeurs__ ;
    static unsigned int max__ ;
    static unsigned int indice__ ;

 } ;

Testeur * * Testeurs::testeurs__ {} ;
unsigned int Testeurs::max__ {} ;
unsigned int Testeurs::indice__ {} ;

void boucle( int deb, int fin, int inc )
 {
  unsigned int i ;
  for ( i=0 ; i<Testeurs::nb_testeurs() ; ++i )
   {
    Testeur * t = Testeurs::testeur(i) ;
    std::cout<<std::endl ;
    int bits ;
    for ( bits = deb ; bits <= fin ; bits = bits + inc )
     { t->execute(bits) ; }
   }
 }

"""