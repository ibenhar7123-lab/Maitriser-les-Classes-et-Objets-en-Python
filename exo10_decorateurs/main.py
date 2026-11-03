import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo10_decorateurs.rectangle import Rectangle

rect = Rectangle(5, 10)
print(rect.aire())    # 50.0
print(rect.aire(2))   # 100

try:
    rect.aire(-1)
except ValueError as e:
    print(e)  # L'argument à l'index 1 doit être un nombre positif.
