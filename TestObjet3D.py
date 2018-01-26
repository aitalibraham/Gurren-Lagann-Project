from Objet3D import *

#Creation d'un carre de cote 1 et deplacement de celui-ci du vecteur v
v=Point(1,1,1)
o = Objet3D()
o.addSommet(Point(0,0,0))
o.addSommet(Point(1,0,0))
o.addSommet(Point(0,1,0))
o.addSommet(Point(1,1,0))
o.centre=Point(0,0,0)
print(o)

o.deplacer(v)
print(o)

