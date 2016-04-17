
#include <iostream>
#include <iomanip>
#include <random>
#include <string>
#include <vector>


//==============================================
// utilitaires
//==============================================

class Echec
 {
  public :
    Echec( unsigned int c, std::string const & comm )
     : code_(c), commentaire_(comm) {}
      unsigned int code() const { return code_ ; }
      std::string const & commentaire() const { return commentaire_ ; }
  private :
    unsigned int code_ ;
      std::string commentaire_ ;
 } ;

double arrondi( double d, unsigned precision =0 )
 {
  double mult {1.} ;
  while (precision-->0) mult *= 10. ;
  if (d>0) { return int(d*mult+.5)/mult ; }
  else { return int(d*mult-.5)/mult ; }
 }

constexpr int fois_puissance_de_deux( int nombre, int exposant )
 { return (exposant>0)?(nombre<<exposant):(nombre>>(-exposant)) ; }

constexpr int entier_max( int nombre_bits )
 { return (fois_puissance_de_deux(1,nombre_bits)-1) ; }

template<typename T> constexpr bool avec_signe() { return true ; }
template<> constexpr bool avec_signe<unsigned int>() { return false ; }
template<> constexpr bool avec_signe<unsigned short>() { return false ; }
template<> constexpr bool avec_signe<unsigned char>() { return false ; }

template<typename T>
constexpr int nombre_bits_hors_signe()
 { return avec_signe<T>()?(sizeof(T)*8-1):(sizeof(T)*8) ; }

class RandCoefs
 {
  public :
    RandCoefs() : rd_{}, gen_{rd_()}, dis_(0,1) {}
    double operator()()
     { return dis_(gen_) ; }
  private :
    std::random_device rd_ ;
    std::mt19937 gen_ ;
    std::uniform_real_distribution<> dis_ ;
 } ;


//==============================================
// framework general de test
//==============================================

class Testeur
 {
 
  public :
  
    class EchecDivisionParZero : public Echec
     { public : EchecDivisionParZero() : Echec(1,"division par 0") {} } ;
  
    Testeur( int resolution ) : resolution_(resolution) {}
    virtual void operator()( int bits ) =0 ;
    virtual ~Testeur() {} ;
    
  protected :
  
    struct ResultatTest
     {
      double exact ;
      double approx ;
     } ;

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
    void erreur( int bits, std::vector<ResultatTest> resultats )
     {
      double err_moyenne {} ;
      for ( auto const & res : resultats )
       {
        double exact = res.exact;
        double approx = res.approx;
        
        if (res.exact == 0.0) { throw EchecDivisionParZero() ; }
        double err = resolution_*(res.exact-res.approx)/res.exact ;
        if (err<0) err = -err ;
        if (err>resolution_) err = resolution_ ;
        
        err_moyenne += err;
       }
      
      err_moyenne /= resultats.size() ;
      int err_finale = arrondi(err_moyenne);
      
      std::cout << bits << " bits : " << err_finale <<"/" << resolution_ << std::endl ;
     }

    RandCoefs rand_ ;
    
  private :
  
    int const resolution_ ;

 } ;

class Testeurs
 {
  public :
    using pointer = std::unique_ptr<Testeur> ;
    using container = std::vector<pointer> ;
    using const_iterator = container::const_iterator ;
    void acquiere( pointer && t ) { testeurs__.push_back(std::move(t)) ; }
    const_iterator begin() const { return testeurs__.begin() ; }
    const_iterator end() const { return testeurs__.end() ; }
  private :
    container testeurs__ ;
 } ;
    
void boucle( int deb, int fin, int inc, const Testeurs & ts )
 {
  for ( const auto & t : ts ) // Testeurs::pointer
   {
    try
     {
      std::cout<<std::endl ;
      int bits ;
      for ( bits = deb ; bits <= fin ; bits = bits + inc )
       { (*t)(bits) ; }
     }
    catch ( Echec const & e )
     { std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ; }
   }
 }


//==============================================
// Coef
//==============================================

template<typename U>
class Coef
 {
  public :
  
    class EchecTropDeBits : public Echec
     { public : EchecTropDeBits() : Echec(2,"trop de bits pour ce type") {} } ;
     
    explicit Coef( unsigned int bits )
     : bits_{bits}, numerateur_{0}, exposant_{0}
     { if (bits_>max_bits__) throw EchecTropDeBits() ; }
    unsigned int lit_bits() const
     { return bits_ ; }
    void operator=( double valeur )
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
    operator double() const
     {
      if (exposant_<0) { throw Echec(5,"exposant negatif") ; }
      return (double(numerateur_)/fois_puissance_de_deux(1,exposant_)) ;
     }
    U operator*( U arg ) const
     { return fois_puissance_de_deux(numerateur_*arg,-exposant_) ; }   
    U numerateur() const
     { return numerateur_ ; }
    int exposant() const
     { return exposant_ ; }

  private :
  
    const unsigned int bits_ ;
    U numerateur_ ;
    int exposant_ ;
    
    static constexpr unsigned int max_bits__
     = nombre_bits_hors_signe<U>() ;
    
 } ;

template<typename U>
std::ostream & operator<<( std::ostream & os, Coef<U> const & c )
 { return (os<<c.numerateur()<<"/2^"<<c.exposant()) ; }

template<>
std::ostream & operator<<( std::ostream & os, Coef<unsigned char> const & c )
 { return (os<<int(c.numerateur())<<"/2^"<<c.exposant()) ; }


//==============================================
// Testeurs dedies a Coef
//==============================================

template< typename U >
class TesteurCoefs : public Testeur
 {
  public :
  
    TesteurCoefs( int resolution, int nombre_iterations )
     : Testeur(resolution), iterations_(nombre_iterations)
     {}

    virtual void operator()( int bits )
     {
      Coef<U> c(bits) ;
      std::vector<Testeur::ResultatTest> resultats ;
      resultats.reserve(iterations_) ;
      
      for ( int i = 0 ; i < iterations_ ; ++i )
       {
        double coef = rand_() ;
        c = coef ;
        resultats.push_back({coef, c}) ;
       }
       
      erreur(bits,resultats) ;
     }
     
  private :
  
    int iterations_ ;
  
 } ;


template< typename U >
class TesteurSommes : public Testeur
 {
  public :

    TesteurSommes( int resolution, int nombre_iterations )
     : Testeur(resolution), iterations_(nombre_iterations)
     {}

    virtual void operator()( int bits )
     {
      constexpr U e {10000} ;
      Coef<U> coef1(bits), coef2(bits) ;
      std::vector<Testeur::ResultatTest> resultats;
      resultats.reserve(iterations_);
      
      for ( int i = 0 ; i < iterations_ ; ++i )
       {
        double c1 = rand_();
        double c2 = 1.0-c1;
        
        int exact = arrondi(c1*e+c2*e) ;
        
        coef1 = c1 ;
        coef2 = c2 ;
        int approx = coef1*e + coef2*e ;
        
        resultats.push_back({double(exact), double(approx)});
       }
      
      erreur(bits,resultats) ;
     }
     
  private :
  
    int iterations_ ;
  
 } ;


//==============================================
// fonction principale
//==============================================

int main()
 {
  try
   {
    Testeurs ts ;
    ts.acquiere(std::make_unique<TesteurCoefs<unsigned short>>(10000,10000000)) ;
    ts.acquiere(std::make_unique<TesteurSommes<unsigned short>>(10000,10000000)) ;
    boucle(1,8,1,ts) ;
    std::cout<<std::endl ;
    return 0 ;
   }
  catch ( Echec const & e )
   {
    std::cout<<"[ERREUR "<<e.code()<<" : "<<e.commentaire()<<"]"<<std::endl ;
    return e.code() ;
   }
 }

