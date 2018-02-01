from Objet3D import *

class Robot(Objet3D) :
    def __init__(self, position, vectDir , Vitesse, r1 , r2 , tete) :
        Objet3D.__init__(position)
        