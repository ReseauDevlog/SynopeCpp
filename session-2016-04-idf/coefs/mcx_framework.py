# -*- coding: utf-8 -*-

HEADER = """
//==============================================
// framework general de test
//==============================================
"""

pfonctions = HEADER + """
void boucle( int deb, int fin, int inc, void (*f)( int ) )
 {
  int bits ;
  for ( bits = deb ; bits <= fin ; bits += inc )
   { f(bits) ; }
  std::cout<<std::endl ;
 }

"""

pfonctions_ostream = HEADER + """
std::ostream * sortie {} ;

void boucle( int deb, int fin, int inc, void (*f)( int ) )
 {
  int bits ;
  for ( bits = deb ; bits <= fin ; bits += inc )
   { f(bits) ; }
  (*sortie)<<std::endl ;
 }

"""

erreur = HEADER + """
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

testeur = HEADER + """
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

testeur_virtuel_incorrect = """
class Testeur
 {

  public :

    void init( int resolution )
     { resolution_ = resolution ; }
    
    virtual void execute( int bits )
     { std::cout << "Mais qu'est-ce que je fais la ?" << std::endl ; }
     
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

virtual = HEADER + testeur_virtuel_incorrect + """
void boucle( Testeur & testeur, int resolution, int debut, int fin, int inc )
 {
  std::cout<<std::endl ;
  testeur.init(resolution) ;
  for ( int bits =debut ; bits <= fin ; bits = bits + inc )
   { testeur.execute(bits) ; }
 }
 
"""

boucle_foncteur = HEADER + testeur_virtuel_incorrect + """
class Boucle
 {
  public :
    void execute( Testeur & t, int resolution, int debut, int fin, int inc )
     {
      std::cout<<std::endl ;
      t.init(resolution) ;
      for ( int bits =debut ; bits <= fin ; bits = bits + inc )
       { t.execute(bits) ; }
     }
 } ;
 
"""

boucle_conteneur = HEADER + testeur_virtuel_incorrect + """
class Boucle
 {
  public :
    void copie( int indice, Testeur t )
     { testeurs_[indice] = t ; }
    void execute( int resolution, int debut, int fin, int inc )
     {
      for ( Testeur t : testeurs_ )
       {
        std::cout<<std::endl ;
        t.init(resolution) ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { t.execute(bits) ; }
       }
     }
  private :
    Testeur testeurs_[5] ;
 } ;
 
"""

testeur_abstrait_incorrect = """
class Testeur
 {
  public :
    void init( int resolution ) { resolution_ = resolution ; }
    virtual void execute( int bits ) = 0 ;
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

conteneur_ptr = HEADER + testeur_abstrait_incorrect + """
class Boucle
 {
  public :
    void init()
     {
      for ( Testeur * & pt : testeurs_ )
       { pt = nullptr ; }
     }
    void enregistre( int indice, Testeur * t )
     { testeurs_[indice] = t ; }
    void execute( int resolution, int debut, int fin, int inc )
     {
      for ( Testeur * pt : testeurs_ )
       {
        if (pt==nullptr) continue ;
        std::cout<<std::endl ;
        pt->init(resolution) ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { pt->execute(bits) ; }
       }
     }
  private :
    Testeur * testeurs_[5] ;
 } ;
 
"""

conteneur_indice = HEADER + testeur_abstrait_incorrect + """
class Boucle
 {
  public :
    void init()
     { indice_ = 0 ; }
    void enregistre( Testeur * t )
     {
      if (indice_==5)
       { echec(10,"trop de testeurs") ; }
      testeurs_[indice_++] = t ;
     }
    void execute( int resolution, int debut, int fin, int inc )
     {
      for ( int i=0; i<indice_ ; i++ )
       {
        std::cout<<std::endl ;
        testeurs_[i]->init(resolution) ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { testeurs_[i]->execute(bits) ; }
       }
     }
  private :
    Testeur * testeurs_[5] ;
    int indice_ ;
 } ;
 
"""

conteneur_dyn = HEADER + testeur_abstrait_incorrect + """
class Boucle
 {
  public :
    void init( int taille )
     {
      taille_ = taille ;
      indice_ = 0 ;
      testeurs_ = new Testeur * [taille_] ;
     }
    void enregistre( Testeur * t )
     {
      if (indice_==taille_)
       { echec(10,"trop de testeurs") ; }
      testeurs_[indice_++] = t ;
     }
    void execute( int resolution, int debut, int fin, int inc )
     {
      for ( int i=0; i<indice_ ; i++ )
       {
        std::cout<<std::endl ;
        testeurs_[i]->init(resolution) ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { testeurs_[i]->execute(bits) ; }
       }
     }
    void finalise()
     { delete [] testeurs_ ; }
  private :
    int taille_ ;
    int indice_ ;
    Testeur * * testeurs_ ;
 } ;
 
"""

testeur_abstrait_correct = """
class Testeur
 {
  public :
    void init( int resolution ) { resolution_ = resolution ; }
    virtual void execute( int bits ) = 0 ;
    virtual ~Testeur() {} ;
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

conteneur_owner = HEADER + testeur_abstrait_correct + """
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
        std::cout<<std::endl ;
        testeurs_[i]->init(resolution) ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { testeurs_[i]->execute(bits) ; }
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

boucle_owner = """
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
    void execute( int debut, int fin, int inc )
     {
      for ( int i=0; i<indice_ ; i++ )
       {
        std::cout<<std::endl ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { testeurs_[i]->execute(bits) ; }
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

constructeurs_testeurs_derives = HEADER + testeur_abstrait_correct + boucle_owner
 
testeur_construit = """
class Testeur
 {
  public :
    Testeur( int resolution ) { resolution_ = resolution ; }
    virtual void execute( int bits ) = 0 ;
    virtual ~Testeur() {} ;
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

constructeurs_testeurs = HEADER + testeur_construit + boucle_owner

boucle_construite = """
class Boucle
 {
  public :
    Boucle( int taille )
     : taille_{taille}, indice_{0}, testeurs_{new Testeur * [taille]}
     {}
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { echec(10,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    void execute( int debut, int fin, int inc )
     {
      for ( int i=0; i<indice_ ; i++ )
       {
        std::cout<<std::endl ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { testeurs_[i]->execute(bits) ; }
       }
     }
    ~Boucle()
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

constructeurs = HEADER + testeur_construit + boucle_construite

testeur_const = """
class Testeur
 {
  public :
    Testeur( int resolution ) : resolution_{resolution} {}
    virtual void execute( int bits ) = 0 ;
    virtual ~Testeur() {} ;
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
    int const resolution_ ;
 } ;
 
"""

const = HEADER + testeur_const + """
class Boucle
 {
  public :
    Boucle( int taille )
     : taille_{taille}, indice_{0}, testeurs_{new Testeur * [taille]}
     {}
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { echec(10,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    void execute( int debut, int fin, int inc )
     {
      for ( int i=0; i<indice_ ; i++ )
       {
        std::cout<<std::endl ;
        for ( int bits =debut ; bits <= fin ; bits = bits + inc )
         { testeurs_[i]->execute(bits) ; }
       }
     }
    ~Boucle()
     {
      for ( int i=0; i<indice_ ; i++ )
       { delete testeurs_[i] ; }
      delete [] testeurs_ ;
     }
    
  private :
  
    int const taille_ ;
    int indice_ ;
    Testeur * * testeurs_ ;
    
 } ;
 
"""

conteneur_dedie = HEADER + testeur_const + """
class Testeurs
 {
  public :
    Testeurs( int taille )
     : taille_{taille}, indice_{0}, testeurs_{new Testeur * [taille]}
     {}
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { echec(10,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    int nb_elements() { return indice_ ; }
    Testeur * element( int indice )
     {
      if ((indice<0)||(indice>=indice_))
       { echec(10,"indice incorrect") ; }
      return testeurs_[indice] ;
     }
    ~Testeurs()
     {
      for ( int i=0; i<indice_ ; i++ )
       { delete testeurs_[i] ; }
      delete [] testeurs_ ;
     }
  private :
    int const taille_ ;
    int indice_ ;
    Testeur * * testeurs_ ;
    
 } ;
 
void boucle( int debut, int fin, int inc, Testeurs & ts )
 {
  int nb = ts.nb_elements() ;
  for ( int i=0; i<nb ; i++ )
   {
    std::cout<<std::endl ;
    for ( int bits =debut ; bits <= fin ; bits = bits + inc )
     { ts.element(i)->execute(bits) ; }
   }
 }
 
"""

statiques = HEADER + testeur_const + """
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