# -*- coding: utf-8 -*-

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

classe = """
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