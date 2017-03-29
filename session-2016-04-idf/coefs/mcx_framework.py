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
  if (exact==0) { echec(1,"division par 0") ; }
  int erreur = arrondi(resolution*(exact-approx)/exact) ;
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
      if (exact==0) { echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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
      if (exact==0) { echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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
      if (exact==0) { echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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
       { echec(2,"trop de testeurs") ; }
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
       { echec(2,"trop de testeurs") ; }
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
      if (exact==0) { echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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
       { echec(2,"trop de testeurs") ; }
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
       { echec(2,"trop de testeurs") ; }
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
      if (exact==0) { echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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
       { echec(2,"trop de testeurs") ; }
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
      if (exact==0) { echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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
       { echec(2,"trop de testeurs") ; }
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
       { echec(2,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    int nb_elements() { return indice_ ; }
    Testeur * element( int indice )
     {
      if ((indice<0)||(indice>=indice_))
       { echec(3,"indice incorrect") ; }
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
  
    static void init( int max )
     {
      max__ = max ;
      indice__ = 0 ;
      testeurs__ = new Testeur * [max__] ;
     }
     
    static void acquiere( Testeur * t )
     {
      if (indice__==max__) { echec(2,"trop de testeurs") ; }
      testeurs__[indice__] = t ;
      indice__++ ;
     }
     
    static int nb_testeurs()
     { return indice__ ; }
     
    static Testeur * testeur( int i )
     {
      if (i>=indice__) { echec(3,"indice de testeur incorrect") ; }
      return testeurs__[i] ;
     }
     
    static void finalise()
     {
      for ( int i=0 ; i<indice__ ; ++i )
       { delete testeurs__[i] ; }
      delete [] testeurs__ ;
     }
     
  private :
  
    static Testeur * * testeurs__ ;
    static int max__ ;
    static int indice__ ;

 } ;

Testeur * * Testeurs::testeurs__ {} ;
int Testeurs::max__ {} ;
int Testeurs::indice__ {} ;

void boucle( int deb, int fin, int inc )
 {
  int i ;
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

testeur_throw = """
class Testeur
 {
  public :
    Testeur( int resolution ) : resolution_{resolution} {}
    virtual void execute( int bits ) = 0 ;
    virtual ~Testeur() {} ;
  protected :
    void erreur( int bits, double exact, double approx )
     {
      if (exact==0) { throw Echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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

testeurs_throw = """
class Testeurs
 {
  public :
    Testeurs( int taille )
     : taille_{taille}, indice_{0}, testeurs_{new Testeur * [taille]}
     {}
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { throw Echec(2,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    int nb_elements() { return indice_ ; }
    Testeur * element( int indice )
     {
      if ((indice<0)||(indice>=indice_))
       { throw Echec(3,"indice de testeur incorrect") ; }
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

"""
 
boucle_sur_testeurs = """
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

throw = HEADER + testeur_throw + testeurs_throw + boucle_sur_testeurs
 
boucle_catch = """
void boucle( int debut, int fin, int inc, Testeurs & ts )
 {
  int nb = ts.nb_elements() ;
  for ( int i=0; i<nb ; i++ )
   {
    try
     {
      std::cout<<std::endl ;
      for ( int bits = debut ; bits <= fin ; bits = bits + inc )
       { ts.element(i)->execute(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }
 
"""

catch = HEADER + testeur_throw + testeurs_throw + boucle_catch

testeurs_opbrackets = """
class Testeurs
 {
  public :
    Testeurs( int taille )
     : taille_{taille}, indice_{0}, testeurs_{new Testeur * [taille]}
     {}
    void acquiere( Testeur * pt )
     {
      if (indice_==taille_)
       { throw Echec(2,"trop de testeurs") ; }
      testeurs_[indice_++] = pt ;
     }
    int nb_elements() { return indice_ ; }
    Testeur * operator[]( int indice )
     {
      if ((indice<0)||(indice>=indice_))
       { throw Echec(3,"indice de testeur incorrect") ; }
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

"""
 
boucle_opbrackets = """
void boucle( int debut, int fin, int inc, Testeurs & ts )
 {
  int nb = ts.nb_elements() ;
  for ( int i=0; i<nb ; i++ )
   {
    try
     {
      std::cout<<std::endl ;
      for ( int bits = debut ; bits <= fin ; bits = bits + inc )
       { ts[i]->execute(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }
 
"""

opbrackets = HEADER + testeur_throw + testeurs_opbrackets + boucle_opbrackets

testeur_opexec = """
class Testeur
 {
  public :
    Testeur( int resolution ) : resolution_{resolution} {}
    virtual void operator()( int bits ) = 0 ;
    virtual ~Testeur() {} ;
  protected :
    void erreur( int bits, double exact, double approx )
     {
      if (exact==0) { throw Echec(1,"division par 0") ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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

boucle_opexec = """
void boucle( int debut, int fin, int inc, Testeurs & ts )
 {
  int nb = ts.nb_elements() ;
  for ( int i=0; i<nb ; i++ )
   {
    try
     {
      Testeur & t {*ts[i]} ;
      std::cout<<std::endl ;
      for ( int bits = debut ; bits <= fin ; bits = bits + inc )
       { t(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }
 
"""

opexec = HEADER + testeur_opexec + testeurs_opbrackets + boucle_opexec

testeur_default = """
class Testeur
 {
 
  public :
  
    class EchecDivisionParZero : public Echec
     { public : EchecDivisionParZero() : Echec(1,"division par 0") {} } ;
  
    Testeur( int resolution ) : resolution_(resolution) {}
    virtual void operator()( int bits ) =0 ;
    virtual ~Testeur() = default ;
    
  protected :
  
    void erreur( int bits, double exact, double approx )
     {
      if (exact==0) { throw EchecDivisionParZero() ; }
      int erreur = arrondi(resolution_*(exact-approx)/exact) ;
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

gen0 = HEADER + testeur_default + """
class Testeurs
 {
  public :
  
    class EchecTropDeTesteurs : public Echec
     { public : EchecTropDeTesteurs() : Echec(2,"trop de testeurs") {} } ;
    
    class EchecIndiceIncorrect : public Echec
     { public : EchecIndiceIncorrect() : Echec(3,"indice de testeur incorrect") {} } ;
    
    Testeurs( int max )
     : max_{max}, indice_{}, testeurs_{new Testeur * [max]}
     {}
     
    void acquiere( Testeur * t )
     {
      if (indice_==max_) { throw EchecTropDeTesteurs() ; }
      testeurs_[indice_] = t ;
      indice_++ ;
     }
     
    int nb_elements()
     { return indice_ ; }
     
    Testeur * operator[]( int i )
     {
      if (i>=indice_) { throw EchecIndiceIncorrect() ; }
      return testeurs_[i] ;
     }
     
    ~Testeurs()
     {
      for ( int i=0 ; i<indice_ ; ++i )
       { delete testeurs_[i] ; }
      delete [] testeurs_ ;
     }
     
  private :
  
    int max_ ;
    int indice_ ;
    Testeur * * testeurs_ ;
 } ;
    
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  for ( int i=0 ; i<ts.nb_elements() ; ++i )
   {
    try
     {
      Testeur & t = *ts[i] ;
      std::cout<<std::endl ;
      for ( int bits = deb ; bits <= fin ; bits = bits + inc )
       { t(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }

"""

template = HEADER + testeur_default + """
template<int SIZE>
class Testeurs
 {
  public :
  
    class EchecTropDeTesteurs : public Echec
     { public : EchecTropDeTesteurs() : Echec(2,"trop de testeurs") {} } ;
    
    class EchecIndiceIncorrect : public Echec
     { public : EchecIndiceIncorrect() : Echec(3,"indice de testeur incorrect") {} } ;
    
    Testeurs() : indice_{} { static_assert(SIZE>=0,"nombre négatif de testeurs") ; }
     
    void acquiere( Testeur * t )
     {
      if (indice_==SIZE) { throw EchecTropDeTesteurs() ; }
      testeurs_[indice_] = t ;
      indice_++ ;
     }
     
    int nb_elements() const
     { return indice_ ; }
     
    Testeur * operator[]( int i )
     {
      if (i>=indice_) { throw EchecIndiceIncorrect() ; }
      return testeurs_[i] ;
     }
     
    ~Testeurs()
     {
      for ( int i=0 ; i<indice_ ; ++i )
       { delete testeurs_[i] ; }
     }
     
  private :
  
    int indice_ ;
    Testeur * testeurs_[SIZE] ;
 } ;
    
template<int SIZE>
void boucle( int deb, int fin, int inc, Testeurs<SIZE> & ts )
 {
  for ( int i=0 ; i<ts.nb_elements() ; ++i )
   {
    try
     {
      Testeur & t = *ts[i] ;
      std::cout<<std::endl ;
      for ( int bits = deb ; bits <= fin ; bits = bits + inc )
       { t(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }

"""

#=====================================================================
# TP BIBLIO
#=====================================================================

rand_testeur = """
class RandTesteur
 {
  public :
    RandTesteur( int nb, int resolution, int width )
     : nb_{nb}, num_{new_rand_coefs(nb)}, 
       exact_{new double [nb]}, approx_{new double [nb]},
       resolution_{resolution}, width_{width}
     {}
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual void execute( int bits ) =0 ;
    virtual ~RandTesteur()
     { delete [] num_ ; delete [] exact_ ; delete [] approx_ ; }
  protected : 
    int nb_ ;
    double * num_, * exact_, * approx_ ;
    void erreur( int bits )
     {
      double exacts {}, approxs {}, erreurs {} ;
      for ( int i=0 ; i<nb_ ; ++i )
       {
        exacts += exact_[i] ; approxs += approx_[i] ;
        erreurs += fabs(exact_[i]-approx_[i])/exact_[i] ;
       }
      exacts /= nb_ ; approxs /= nb_ ; erreurs /= nb_ ;
      erreurs *= resolution_ ;
      std::cout
        <<bits<<" bits : "
        <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
        <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
        <<std::endl ;
     }
  private :
    int const resolution_ ;
    int const width_ ;
 } ;

"""

testeurs_biblio0 = """
template<int SIZE>
class Testeurs
 {
  public :
    Testeurs() : indice_{} {}
    void acquiere( RandTesteur * t ) { testeurs_[indice_++] = t ; }
    int nb_elements()  { return indice_ ; }
    RandTesteur * operator[]( int i ) { return testeurs_[i] ; }
    ~Testeurs()
     {
      for ( int i=0 ; i<indice_ ; ++i )
       { delete testeurs_[i] ; }
     }
  private :
    int indice_ ;
    RandTesteur * testeurs_[SIZE] ;
 } ;
    

"""

boucle_biblio0 = """
template<int SIZE>
void boucle( int deb, int fin, int inc, Testeurs<SIZE> & ts )
 {
  for ( int i=0 ; i<ts.nb_elements() ; ++i )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     { ts[i]->execute(bits) ; }
   }
 }

"""

biblio = HEADER + rand_testeur + testeurs_biblio0 + boucle_biblio0

testeurs_vector = """
class Testeurs
 {
  public :
    void acquiere( RandTesteur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() const { return testeurs_.size() ; }
    RandTesteur * operator[]( int i ) { return testeurs_.at(i) ; }
    ~Testeurs() { for ( RandTesteur * t : testeurs_ ) delete t ; } 
  private :
    std::vector<RandTesteur *> testeurs_ ;
 } ;
    
"""

boucle_biblio = """
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  for ( int i=0 ; i<ts.nb_elements() ; ++i )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     { ts[i]->execute(bits) ; }
   }
 }

"""

vector = HEADER + rand_testeur + testeurs_vector + boucle_biblio

testeurs_pointeur = """
class Testeurs
 {
  public :
    void acquiere( RandTesteur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<RandTesteur> operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<Pointeur<RandTesteur>> testeurs_ ;
 } ;
    
"""

pointeur = HEADER + rand_testeur + testeurs_pointeur + boucle_biblio

testeurs_bavard = """
class Testeurs
 {
  public :
    void acquiere( RandTesteur * t ) { std::cout<<"(testeurs : acquiere "<<t<<")"<<std::endl ; testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<RandTesteur> operator[]( int i )
     {
      std::cout<<"(testeurs : accede "<<i<<"->"<<testeurs_.at(i).get()<<")"<<std::endl ;
      return testeurs_.at(i) ;
     }
    ~Testeurs() { std::cout<<"(testeurs : libere"<<")"<<std::endl ; }
  private :
    std::vector<Pointeur<RandTesteur>> testeurs_ ;
 } ;

"""

pointeur_bavard = HEADER + rand_testeur + testeurs_bavard + boucle_biblio

testeurs_ref_bavard = """
class Testeurs
 {
  public :
    void acquiere( RandTesteur * t ) { std::cout<<"(testeurs : acquiere "<<t<<")"<<std::endl ; testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<RandTesteur> & operator[]( int i )
     {
      std::cout<<"(testeurs : accede "<<i<<"->"<<testeurs_.at(i).get()<<")"<<std::endl ;
      return testeurs_.at(i) ;
     }
    ~Testeurs() { std::cout<<"(testeurs : libere"<<")"<<std::endl ; }
  private :
    std::vector<Pointeur<RandTesteur>> testeurs_ ;
 } ;

"""

auto_pointeur_bavard = HEADER + rand_testeur + testeurs_ref_bavard + boucle_biblio

testeurs_ref = """
class Testeurs
 {
  public :
    void acquiere( RandTesteur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<RandTesteur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<Pointeur<RandTesteur>> testeurs_ ;
 } ;
    
"""

auto_pointeur = HEADER + rand_testeur + testeurs_ref + boucle_biblio

testeurs_shared = """
#include <memory>

class Testeurs
 {
  public :
    void acquiere( std::shared_ptr<RandTesteur> const & t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    std::shared_ptr<RandTesteur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<std::shared_ptr<RandTesteur>> testeurs_ ;
 } ;
    
"""

shared = HEADER + rand_testeur + testeurs_shared + boucle_biblio

testeurs_unique = """
#include <memory>

class Testeurs
 {
  public :
    void acquiere( std::unique_ptr<RandTesteur> && t ) { testeurs_.push_back(std::move(t)) ; }
    int nb_elements() { return testeurs_.size() ; }
    std::unique_ptr<RandTesteur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<std::unique_ptr<RandTesteur>> testeurs_ ;
 } ;
    
"""

unique = HEADER + rand_testeur + testeurs_unique + boucle_biblio

direct = HEADER + rand_testeur + """
void boucle( int deb, int fin, int inc, std::vector<std::unique_ptr<RandTesteur>> & ts )
 {
  for ( int i=0 ; i<ts.size() ; ++i )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     { ts[i]->execute(bits) ; }
   }
 }

"""


#=====================================================================
# TP PARALLELE
#=====================================================================

testeur_parallele = """
#include <array>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      typename conteneur::iterator icoef ;
      for ( icoef = coefs_.begin() ; icoef != coefs_.end() ; ++icoef )
       { *icoef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      double exact, approx ;
      double exacts {0}, approxs {0}, erreurs {0} ;
      typename conteneur::iterator icoef ;
      for ( icoef = coefs_.begin() ; icoef != coefs_.end() ; ++icoef )
       {
        execute(bits,*icoef,exact,approx) ;
        exacts +=exact ; approxs += approx ;
        erreurs += fabs(exact-approx)/exact ;
       }
      exacts /= SIZE ; approxs /= SIZE ; erreurs /= SIZE ;
      erreurs *= resolution_ ;
      std::cout
        <<bits<<" bits : "
        <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
        <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
        <<std::endl ;
     }
     
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    using conteneur = std::array<double,SIZE> ;
    conteneur coefs_ ;
    
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

"""

parallele = HEADER + testeur_parallele +"""
template<typename Testeurs>
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  typename Testeurs::iterator itesteur ;
  for ( itesteur = ts.begin() ; itesteur != ts.end() ; ++itesteur )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     { (*itesteur)->execute(bits) ; }
   }
 }

"""

testeur_auto = """
#include <array>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      for ( auto icoef = coefs_.begin() ; icoef != coefs_.end() ; ++icoef )
       { *icoef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      double exact, approx ;
      double exacts {0}, approxs {0}, erreurs {0} ;
      for ( auto icoef = coefs_.begin() ; icoef != coefs_.end() ; ++icoef )
       {
        execute(bits,*icoef,exact,approx) ;
        exacts +=exact ; approxs += approx ;
        erreurs += fabs(exact-approx)/exact ;
       }
      exacts /= SIZE ; approxs /= SIZE ; erreurs /= SIZE ;
      erreurs *= resolution_ ;
      std::cout
        <<bits<<" bits : "
        <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
        <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
        <<std::endl ;
     }
     
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    std::array<double,SIZE> coefs_ ;
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

"""

boucle_auto = """
template<typename Testeurs>
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  for ( auto itesteur = ts.begin() ; itesteur != ts.end() ; ++itesteur )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     { (*itesteur)->execute(bits) ; }
   }
 }

"""

auto = HEADER + testeur_auto + boucle_auto

testeur_lambdas = """
#include <array>
#include <algorithm>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      std::for_each
       (
        coefs_.begin(),coefs_.end(),
        [this]( double & coef )
         { coef = rand_coefs_() ; }
       ) ;
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      double exact, approx ;
      double exacts {0}, approxs {0}, erreurs {0} ;
      std::for_each
       (
        coefs_.begin(),coefs_.end(),
        [&]( double coef )
         {
          execute(bits,coef,exact,approx) ;
          exacts +=exact ; approxs += approx ;
          erreurs += fabs(exact-approx)/exact ;
         }
       ) ;
      exacts /= SIZE ; approxs /= SIZE ; erreurs /= SIZE ;
      erreurs *= resolution_ ;
      std::cout
        <<bits<<" bits : "
        <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
        <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
        <<std::endl ;
     }
     
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    std::array<double,SIZE> coefs_ ;
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

"""

boucle_lambdas = """
template<typename Testeurs>
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  std::for_each
   (
    ts.begin(),ts.end(),
    [=]( typename Testeurs::value_type & testeur )
     {
      std::cout<<std::endl ;
      for ( int bits = deb ; bits <= fin ; bits = bits + inc )
       { testeur->execute(bits) ; }
     }
   ) ;
 }

"""

lambdas = HEADER + testeur_lambdas + boucle_lambdas

testeur_forgen = """
#include <array>
#include <algorithm>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      for ( double & coef : coefs_ )
       { coef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      double exact, approx ;
      double exacts {0}, approxs {0}, erreurs {0} ;
      for ( double coef : coefs_ )
       {
        execute(bits,coef,exact,approx) ;
        exacts +=exact ; approxs += approx ;
        erreurs += fabs(exact-approx)/exact ;
       }
      exacts /= SIZE ; approxs /= SIZE ; erreurs /= SIZE ;
      erreurs *= resolution_ ;
      std::cout
        <<bits<<" bits : "
        <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
        <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
        <<std::endl ;
     }
     
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    std::array<double,SIZE> coefs_ ;
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

"""

forgen = HEADER + testeur_forgen + boucle_lambdas

testeur_map = """
#include <array>
#include <map>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      for ( double & coef : coefs_ )
       { coef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      double exact, approx ;
      Resultat & res = resultats_[bits] ;
      for ( double coef : coefs_ )
       {
        execute(bits,coef,exact,approx) ;
        res.exacts +=exact ; res.approxs += approx ;
        res.erreurs += fabs(exact-approx)/exact ;
       }
      res.exacts /= SIZE ; res.approxs /= SIZE ; res.erreurs /= SIZE ;
      res.erreurs *= resolution_ ;
     }
     
    void affiche()
     {
      std::cout<<std::endl ;
      for ( auto res : resultats_ )
       {
        std::cout
          <<res.first<<" bits : "
          <<std::left<<res.second.exacts<<" ~ "
          <<std::setw(width_)<<res.second.approxs
          <<" ("<<arrondi(res.second.erreurs)<<"/"<<resolution_<<")"
          <<std::endl ;
       }
     }
     
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    struct Resultat
     {
      Resultat() : exacts {0}, approxs {0}, erreurs {0} {}
      double exacts, approxs, erreurs ;
     } ;
    
    std::array<double,SIZE> coefs_ ;
    std::map<int,Resultat> resultats_ ;
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

"""

testeur_mmap = """
#include <array>
#include <map>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      for ( double & coef : coefs_ )
       { coef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      Resultat res ;
      for ( double coef : coefs_ )
       {
        execute(bits,coef,res.exact,res.approx) ;
        resultats_.insert(std::pair<int,Resultat>(bits,res)) ;
       }
     }
     
    void affiche()
     {
      std::cout<<std::endl ;
      auto ires1 = resultats_.begin() ;
      decltype(ires1) ires2 ;
      auto iend1 = resultats_.end() ;
      decltype(iend1) iend2 ;
      for ( ; ires1 != iend1 ; ires1 = ires2 )
       {
        int bits = ires1->first ;
        double exact, approx ; 
        double exacts {0}, approxs {0}, erreurs {0} ; 
        ires2 = ires1 ;
        iend2 = resultats_.upper_bound(bits) ;
        for ( ; ires2 != iend2 ; ++ires2 )
         {
          exact = ires2->second.exact ;
          approx = ires2->second.approx ;
          exacts += exact ; approxs += approx ;
          erreurs += fabs(exact-approx)/exact ;
         }
        exacts /= SIZE ; approxs /= SIZE ; erreurs /= SIZE ;
        erreurs *= resolution_ ;
        std::cout
          <<bits<<" bits : "
          <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
          <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
          <<std::endl ;
       }
     }
          
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    struct Resultat
     { double exact, approx ; } ;
    
    std::array<double,SIZE> coefs_ ;
    std::multimap<int,Resultat> resultats_ ;
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

"""

boucle_threads = """
#include <thread>

template<typename Testeurs>
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  std::vector<std::thread> threads ;
  for ( auto & testeur : ts )
   {
    threads.push_back(std::thread(
      [deb,fin,inc,&testeur]()
       {
        for ( int bits = deb ; bits <= fin ; bits = bits + inc )
         { testeur->execute(bits) ; }
       })) ;
   }
  for ( auto & thr : threads )
   { thr.join() ; }
  for ( auto & testeur : ts )
   { testeur->affiche() ; }
 }

"""

threads = HEADER + testeur_map + boucle_threads

stress = HEADER + testeur_mmap + boucle_threads

testeur_mutex = """
#include <array>
#include <map>
#include <mutex>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      for ( double & coef : coefs_ )
       { coef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    void execute( int bits )
     {
      Resultat res ;
      for ( double coef : coefs_ )
       {
        execute(bits,coef,res.exact,res.approx) ;
        resultats_mutex_.lock() ;
        resultats_.insert(std::pair<int,Resultat>(bits,res)) ;
        resultats_mutex_.unlock() ;
       }
     }
     
    void affiche()
     {
      std::cout<<std::endl ;
      auto ires1 = resultats_.begin() ;
      decltype(ires1) ires2 ;
      auto iend1 = resultats_.end() ;
      decltype(iend1) iend2 ;
      for ( ; ires1 != iend1 ; ires1 = ires2 )
       {
        int bits = ires1->first ;
        double exact, approx ; 
        double exacts {0}, approxs {0}, erreurs {0} ; 
        ires2 = ires1 ;
        iend2 = resultats_.upper_bound(bits) ;
        for ( ; ires2 != iend2 ; ++ires2 )
         {
          exact = ires2->second.exact ;
          approx = ires2->second.approx ;
          exacts += exact ; approxs += approx ;
          erreurs += fabs(exact-approx)/exact ;
         }
        exacts /= SIZE ; approxs /= SIZE ; erreurs /= SIZE ;
        erreurs *= resolution_ ;
        std::cout
          <<bits<<" bits : "
          <<std::left<<exacts<<" ~ "<<std::setw(width_)<<approxs
          <<" ("<<arrondi(erreurs)<<"/"<<resolution_<<")"
          <<std::endl ;
       }
     }
          
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    struct Resultat
     { double exact, approx ; } ;
    
    std::array<double,SIZE> coefs_ ;
    
    std::mutex resultats_mutex_ ;
    std::multimap<int,Resultat> resultats_ ;
    
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

"""

boucle_mthreads = """
#include <thread>

template<typename Testeurs>
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  std::vector<std::thread> threads ;
  for ( auto & testeur : ts )
   {
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     {
      threads.push_back(std::thread(
        [bits,&testeur]()
         { testeur->execute(bits) ; })) ;
     }
   }
  for ( auto & thr : threads )
   { thr.join() ; }
  for ( auto & testeur : ts )
   { testeur->affiche() ; }
 }

"""

sharedmem = HEADER + testeur_mutex + boucle_mthreads

async = HEADER + """
#include <array>

template<int SIZE>
class RandTesteur
 {
  public :
  
    RandTesteur( int resolution, int width )
     : resolution_{resolution}, width_{width}
     {
      for ( double & coef : coefs_ )
       { coef = rand_coefs_() ; }
     }
     
    RandTesteur( RandTesteur const & ) = delete ;
    RandTesteur & operator=( RandTesteur const & ) = delete ;
    virtual ~RandTesteur() = default ;

    struct Resultat
     {
      Resultat() : exacts {0}, approxs {0}, erreurs {0} {}
      double exacts, approxs, erreurs ;
     } ;
    
    Resultat execute( int bits )
     {
      double exact, approx ;
      Resultat res ;
      for ( double coef : coefs_ )
       {
        execute(bits,coef,exact,approx) ;
        res.exacts +=exact ; res.approxs += approx ;
        res.erreurs += fabs(exact-approx)/exact ;
       }
      res.exacts /= SIZE ; res.approxs /= SIZE ; res.erreurs /= SIZE ;
      res.erreurs *= resolution_ ;
      return res ;
     }
     
    void affiche( int bits, Resultat const & res )
     {
      std::cout
        <<bits<<" bits : "
        <<std::left<<res.exacts<<" ~ "
        <<std::setw(width_)<<res.approxs
        <<" ("<<arrondi(res.erreurs)<<"/"<<resolution_<<")"
        <<std::endl ;
     }
     
  protected : 
  
    virtual void execute( int bits, double coef, double & exact, double & approx ) =0 ;
    
  private :
  
    std::array<double,SIZE> coefs_ ;
    RandCoefs rand_coefs_ ;
    int const resolution_ ;
    int const width_ ;
    
 } ;

#include <map>
#include <future>

template<typename Testeurs>
void boucle( int deb, int fin, int inc, Testeurs & ts )
 {
  using Testeur = typename Testeurs::value_type ;
  using Resultat = typename Testeur::element_type::Resultat ;
  using TesteurResultats = std::map<int,std::future<Resultat>> ;
  std::map<Testeur*,TesteurResultats> resultats ;
  
  for ( auto & testeur : ts )
   {
    resultats[&testeur] = TesteurResultats() ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     {
      resultats[&testeur][bits] = std::async(std::launch::async,
          [bits,&testeur](){ return testeur->execute(bits) ; }) ;
     }
   }
   
  for ( auto & testeur : ts )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
      { testeur->affiche(bits,resultats[&testeur][bits].get()) ; }
   }
 }

"""

