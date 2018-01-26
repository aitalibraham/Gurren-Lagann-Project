from Point import *

class Objet3D(object):
    """Classe definissant un objet 3D (utilise une classe d'attribut x, y, z decrivant un point"""
    #x, y, z: coordonnees du centre geometrique de l'objet
    #sommets : liste de sommets qui doit contenir des objets ayant 3 attributs entiers x, y et z"""

    def __init__(self):
        """Construire un objet 3D en lui attribuant un nom. la position est initialisee a (0, 0, 0)"""
        self.sommets=list()
        self.centre=Point(0,0,0)
        
    def addSommet(self, sommet):
        """Ajoute un sommet a la forme 3D. sommet doit decrire un point de coordonnees (x, y, z)"""
        self.sommets.append(sommet)
    
    def hasSommets(self):
        """Retourne True si la forme a des sommets, False sinon"""
        if not self.sommets:
            return False
        return True

    def deplacer(self, vecteur):
        """deplace les sommets et le centre de l'objet """
        self.centre.deplacer(vecteur)
        if self.hasSommets():
            for s in self.sommets:
                s.deplacer(vecteur)
    
    def __repr__(self):
        """Quand on entre un objet3D dans l'interpreteur"""
        return "Objet3D: position({}), liste de sommets({})".format(self.centre, self.sommets)

    def __getattr__(self, nom):
        """Permet d'acceder aux attributs. s'il n'existent pas:"""
        print("L'attribut {} n'existe pas dans Objet3D !".format(nom))
