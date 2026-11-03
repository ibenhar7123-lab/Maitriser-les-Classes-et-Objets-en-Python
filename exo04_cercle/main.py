import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo04_cercle.cercle import Cercle

c = Cercle(5.0)
print(c.aire())       # 78.53981633974483
print(c.perimetre())  # 31.41592653589793
print(c)

try:
    c.rayon = -10
except ValueError as e:
    print(f"Erreur interceptée : {e}")
