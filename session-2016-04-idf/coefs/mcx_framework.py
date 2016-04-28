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
      if (exact==0) { echec(1,"division par 0") ; }
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
      if (exact==0) { echec(1,"division par 0") ; }
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
      if (exact==0) { echec(1,"division par 0") ; }
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

testeur_biblio = """
class Testeur
 {
  public :
    Testeur( int resolution, int width )
     : resolution_(resolution), width_(width) {}
    Testeur( Testeur const & ) = delete ;
    Testeur & operator=( Testeur const & ) = delete ;
    virtual void execute( int bits ) =0 ;
    virtual ~Testeur() = default ;
  protected : 
    // recoit des tableaux de valeurs exactes et approximations
    void erreur( int bits, double * exact, double * approx, int nb )
     {
      double exacts {}, approxs {}, erreurs {} ;
      for ( int i=0 ; i<nb ; ++i )
       {
        exacts += exact[i] ;
        approxs += approx[i] ;
        erreurs += fabs(exact[i]-approx[i])/exact[i] ;
       }
      exacts /= nb ;
      approxs /= nb ;
      erreurs *= (resolution_/nb) ;
      std::cout
        <<std::right<<std::setw(2)<<bits<<" bits : "
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
    void acquiere( Testeur * t ) { testeurs_[indice_++] = t ; }
    int nb_elements()  { return indice_ ; }
    Testeur * operator[]( int i ) { return testeurs_[i] ; }
    ~Testeurs()
     {
      for ( int i=0 ; i<indice_ ; ++i )
       { delete testeurs_[i] ; }
     }
  private :
    int indice_ ;
    Testeur * testeurs_[SIZE] ;
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

biblio0 = HEADER + testeur_biblio + testeurs_biblio0 + boucle_biblio0

testeurs_vector = """
class Testeurs
 {
  public :
    void acquiere( Testeur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() const { return testeurs_.size() ; }
    Testeur * operator[]( int i ) { return testeurs_.at(i) ; }
    ~Testeurs() { for ( Testeur * t : testeurs_ ) delete t ; } 
  private :
    std::vector<Testeur *> testeurs_ ;
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

vector = HEADER + testeur_biblio + testeurs_vector + boucle_biblio

testeurs_pointeur = """
class Testeurs
 {
  public :
    void acquiere( Testeur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<Testeur> operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<Pointeur<Testeur>> testeurs_ ;
 } ;
    
"""

pointeur = HEADER + testeur_biblio + testeurs_pointeur + boucle_biblio

testeurs_bavard = """
class Testeurs
 {
  public :
    void acquiere( Testeur * t ) { std::cout<<"(testeurs : acquiere "<<t<<")"<<std::endl ; testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<Testeur> operator[]( int i )
     {
      std::cout<<"(testeurs : accede "<<i<<"->"<<testeurs_.at(i).get()<<")"<<std::endl ;
      return testeurs_.at(i) ;
     }
    ~Testeurs() { std::cout<<"(testeurs : libere"<<")"<<std::endl ; }
  private :
    std::vector<Pointeur<Testeur>> testeurs_ ;
 } ;

"""

pointeur_bavard = HEADER + testeur_biblio + testeurs_bavard + boucle_biblio

testeurs_ref_bavard = """
class Testeurs
 {
  public :
    void acquiere( Testeur * t ) { std::cout<<"(testeurs : acquiere "<<t<<")"<<std::endl ; testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<Testeur> & operator[]( int i )
     {
      std::cout<<"(testeurs : accede "<<i<<"->"<<testeurs_.at(i).get()<<")"<<std::endl ;
      return testeurs_.at(i) ;
     }
    ~Testeurs() { std::cout<<"(testeurs : libere"<<")"<<std::endl ; }
  private :
    std::vector<Pointeur<Testeur>> testeurs_ ;
 } ;

"""

auto_pointeur_bavard = HEADER + testeur_biblio + testeurs_ref_bavard + boucle_biblio

testeurs_ref = """
class Testeurs
 {
  public :
    void acquiere( Testeur * t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    Pointeur<Testeur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<Pointeur<Testeur>> testeurs_ ;
 } ;
    
"""

auto_pointeur = HEADER + testeur_biblio + testeurs_ref + boucle_biblio

testeurs_shared = """
#include <memory>

class Testeurs
 {
  public :
    void acquiere( std::shared_ptr<Testeur> const & t ) { testeurs_.push_back(t) ; }
    int nb_elements() { return testeurs_.size() ; }
    std::shared_ptr<Testeur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<std::shared_ptr<Testeur>> testeurs_ ;
 } ;
    
"""

shared = HEADER + testeur_biblio + testeurs_shared + boucle_biblio

testeurs_unique = """
#include <memory>

class Testeurs
 {
  public :
    void acquiere( std::unique_ptr<Testeur> && t ) { testeurs_.push_back(std::move(t)) ; }
    int nb_elements() { return testeurs_.size() ; }
    std::unique_ptr<Testeur> & operator[]( int i ) { return testeurs_.at(i) ; }
  private :
    std::vector<std::unique_ptr<Testeur>> testeurs_ ;
 } ;
    
"""

unique = HEADER + testeur_biblio + testeurs_unique + boucle_biblio

direct = HEADER + testeur_biblio + """
void boucle( int deb, int fin, int inc, std::vector<std::unique_ptr<Testeur>> & ts )
 {
  for ( int i=0 ; i<ts.size() ; ++i )
   {
    std::cout<<std::endl ;
    for ( int bits = deb ; bits <= fin ; bits = bits + inc )
     { ts[i]->execute(bits) ; }
   }
 }

"""

