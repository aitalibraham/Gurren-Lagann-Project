class Point(object):
    """Classe definissant un point dans un espace 3D"""
    def __init__(self, x, y, z):
        """Initialise les coordonnees du point """
        self.x=x
        self.y=y
        self.z=z

    def setPosition(self, point):
        """Modifie les coordonnees du point """
        self.x=point.x
        self.y=point.y
        self.z=point.z
    
    def deplacer(self, vecteur):
        """Deplace le point d'un vecteur (dx, dy, dz)"""
        self.x=self.x+vecteur.x
        self.y=self.y+vecteur.y
        self.z=self.z+vecteur.z

    def __repr__(self):
        """Quand on entre un objet3D dans l'interpreteur"""
        return "Point: (x={}, y={}, z={})".format(self.x, self.y, self.z)

    def __getattr__(self, nom):
        """Permet d'acceder a un attribut. s'il n'existe pas:"""
        print("L'attribut {} n'existe pas dans Point !".format(nom))
