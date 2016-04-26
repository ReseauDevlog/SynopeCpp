# -*- coding: utf-8 -*-

approxime_for = """
//==============================================
// calculs
//==============================================

void approxime( double valeur )
 {
  int exposant ;
  for ( exposant = 1 ; exposant <= 8 ; exposant = exposant + 1 )
   {
    int num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
    std::cout
      << valeur << " ~ " << std::setw(3) << num << "/2^" << exposant
      << std::endl ;
   }
 }

"""

approxime_for_approximation = """
//==============================================
// calculs
//==============================================

void approxime( double valeur )
 {
  int exposant ;
  for ( exposant = 1 ; exposant <= 8 ; exposant = exposant + 1 )
   {
    int num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
    std::cout
      << valeur << " ~ " << std::setw(3) << num << "/2^" << exposant
      << " = " << double(num)/fois_puissance_de_deux(1,exposant)
      << std::endl ;
   }
 }

"""

approxime_max = """
//==============================================
// calculs
//==============================================

void approxime( int max, double valeur )
 {
  int exposant {}, num ;
  do
   {
    exposant = exposant + 1 ;
    num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
   } while (num<=max) ;
  exposant = exposant - 1 ;
  num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
  std::cout
    << valeur << " ~ " << std::setw(3) << num << "/2^" << exposant
    << " = " << double(num)/fois_puissance_de_deux(1,exposant)
    << std::endl ;
 }

"""

approxime_bits = """
//==============================================
// calculs
//==============================================

void approxime( int bits, double valeur )
 {
  int max = entier_max(bits) ;
  int exposant {}, num ;
  do
   {
    exposant = exposant + 1 ;
    num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
   } while (num<=max) ;
  exposant = exposant - 1 ;
  num = arrondi(valeur*fois_puissance_de_deux(1,exposant))  ;
  std::cout
    << bits << " bits : "
    << valeur << " ~ " << std::setw(3) << num << "/2^" << exposant
    << " = " << double(num)/fois_puissance_de_deux(1,exposant)
    << std::endl ;
 }

"""

approxime_ref = """
//==============================================
// calculs
//==============================================

void approxime( int bits, double valeur, int & numerateur, int & exposant )
 {
  numerateur = exposant = 0 ;
  if (valeur==0) { return ; }
  double min = (entier_max(bits)+0.5)/2 ;
  while (valeur<min)
   {
    exposant = exposant + 1 ;
    valeur = valeur * 2 ;
   }
  numerateur = arrondi(valeur) ;
 }

"""

simple = """
//==============================================
// calculs
//==============================================

void approxime( int bits, double valeur, int & numerateur, int & exposant )
 {
  numerateur = exposant = 0 ;
  if (valeur==0) { return ; }
  double min = (entier_max(bits)+0.5)/2 ;
  while (valeur<min)
   {
    exposant = exposant + 1 ;
    valeur = valeur * 2 ;
   }
  numerateur = arrondi(valeur) ;
 }

int multiplie( int bits, double c, int e )
 {
  int numerateur, exposant ;
  approxime(bits,c,numerateur,exposant) ;
  return fois_puissance_de_deux(numerateur*e,-exposant) ;
 }

"""

struct = """
//==============================================
// calculs
//==============================================

class Coef
 {
  public :
    int numerateur_ ;
    int exposant_ ;
 } ;

void approxime( int bits, double valeur, Coef & coef )
 {
  coef.numerateur_ = coef.exposant_ = 0 ;
  if (valeur==0) { return ; }
  double min = (entier_max(bits)+0.5)/2 ;
  while (valeur<min)
   {
    coef.exposant_ = coef.exposant_ + 1 ;
    valeur = valeur * 2 ;
   }
  coef.numerateur_ = arrondi(valeur) ;
 }

int multiplie( int bits, double c, int e )
 {
  Coef coef ;
  approxime(bits,c,coef) ;
  return fois_puissance_de_deux(coef.numerateur_*e,-coef.exposant_) ;
 }

"""

retour = """
//==============================================
// calculs
//==============================================

class Coef
 {
  public :
    int numerateur_ ;
    int exposant_ ;
 } ;

Coef approxime( int bits, double valeur )
 {
  Coef coef ;
  coef.numerateur_ = coef.exposant_ = 0 ;
  if (valeur==0) { return coef ; }
  double min = (entier_max(bits)+0.5)/2 ;
  while (valeur<min)
   {
    coef.exposant_ = coef.exposant_ + 1 ;
    valeur = valeur * 2 ;
   }
  coef.numerateur_ = arrondi(valeur) ;
  return coef ;
 }

int multiplie( int bits, double c, int e )
 {
  Coef coef = approxime(bits,c) ;
  return fois_puissance_de_deux(coef.numerateur_*e,-coef.exposant_) ;
 }

"""

classe = """
//==============================================
// calculs
//==============================================

class Coef
 {
  public :
  
    // transformation d'un double en Coef
    void approxime( int bits, double valeur )
     {
      numerateur_ = exposant_ = 0 ;
      double min = (entier_max(bits)+0.5)/2 ;
      while (valeur<min)
       {
        exposant_ = exposant_ + 1 ;
        valeur = valeur * 2 ;
       }
      numerateur_ = arrondi(valeur) ;
     }
    
    // transformation d'un Coef en double
    double approximation()
     { return double(numerateur_)/fois_puissance_de_deux(1,exposant_) ; }
    
    int multiplie( int e )
     { return fois_puissance_de_deux(numerateur_*e,-exposant_) ; }
    
    std::string texte()
     { return std::to_string(numerateur_)+"/2^"+std::to_string(exposant_) ; }

  private :
  
    int numerateur_ ;
    int exposant_ ;
    
 } ;

"""

coef_bits = """
//==============================================
// calculs
//==============================================

class Coef
 {
  public :
  
    void init( int bits )
     { bits_ = bits ; }
    
    int lit_bits()
     { return bits_ ; }
    
    // transformation d'un double en Coef
    void approxime( double valeur )
     {
      numerateur_ = exposant_ = 0 ;
      double min = (entier_max(bits_)+0.5)/2 ;
      while (valeur<min)
       {
        exposant_ = exposant_ + 1 ;
        valeur = valeur * 2 ;
       }
      numerateur_ = arrondi(valeur) ;
     }
    
    // transformation d'un Coef en double
    double approximation()
     { return double(numerateur_)/fois_puissance_de_deux(1,exposant_) ; }
    
    int multiplie( int e )
     { return fois_puissance_de_deux(numerateur_*e,-exposant_) ; }
    
    std::string texte()
     { return std::to_string(numerateur_)+"/2^"+std::to_string(exposant_) ; }

  private :
  
    int bits_ ;
    int numerateur_ ;
    int exposant_ ;
    
 } ;

"""

const = """
//==============================================
// calculs
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

"""