from Objet3D import *

class Arene(object):
    """Classe contenant un ensemble d'Objets 3D"""

    def __init__(self):
        """Initialise la liste d'Objets """
        self.objets3D=list()

    def add(self, objet3D):
        o=Objet3D();
        if(type(objet3D)==type(o)):
            self.objets3D.append(objet3D)

    def __repr__(self):
        """Quand on entre une arene dans l'interpreteur"""
        return "Arene: objets3D({})".format(self.objets3D)

    def __getattr__(self, nom):
        """Permet d'acceder aux attributs. s'il n'existent pas:"""
        print("L'attribut {} n'existe pas dans Arene !".format(nom))
