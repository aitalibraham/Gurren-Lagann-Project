from Point import *

#Modification/acces des attributs
A=Point(0,0,0)
B=Point(1,2,3)
print(A)
A.setPosition(Point(1,2,3))
A.deplacer(Point(0,1,0))
print(A)

print("coordonnee y: {}".format(A.y))
print("Attribut inexistant: {}".format(A.att))

