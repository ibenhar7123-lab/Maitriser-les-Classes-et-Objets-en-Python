import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo06_convertisseur.convertisseur import Convertisseur

# Appel sans instance
print(round(Convertisseur.vers_dh(100), 2))  # 1090.0

# Modification du taux via méthode de classe
Convertisseur.changer_taux(11.0)
print(Convertisseur.depuis_dh(110))  # 10.0

# Avec une instance (possible, mais pas nécessaire)
conv = Convertisseur()
print(conv.vers_dh(50))  # 550.0
