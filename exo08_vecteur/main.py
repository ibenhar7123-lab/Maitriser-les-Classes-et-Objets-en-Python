import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo08_vecteur.vecteur import Vecteur2D

v1 = Vecteur2D(1, 2)
v2 = Vecteur2D(3, 4)

print(v1 + v2)                 # Vecteur2D(4, 6)
print(v2 - v1)                 # Vecteur2D(2, 2)
print(v1 * 2)                  # Vecteur2D(2, 4)
print(v1 == Vecteur2D(1, 2))   # True
print({v1, Vecteur2D(1, 2)})   # un seul élément grâce à __hash__
