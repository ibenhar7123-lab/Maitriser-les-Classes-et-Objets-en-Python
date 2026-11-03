import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gc
from exo07_ressource.ressource import Ressource

r = Ressource("Fichier de données")
r.utiliser()

del r        # Suppression explicite
gc.collect() # Force le garbage collector
