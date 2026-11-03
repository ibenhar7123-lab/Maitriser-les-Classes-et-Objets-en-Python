import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo09_dataclass.produit import Produit

p1 = Produit("Café", 5.5, 10, ["boisson", "chaud"])
p2 = Produit("Café", 5.5, 10, ["boisson", "chaud"])

print(p1)                 # Produit(nom='Café', prix=5.5, quantite=10, tags=['boisson', 'chaud'])
print(p1 == p2)           # True
print(p1.valeur_totale()) # 55.0

p3 = Produit("Thé", 3.0)
print(p3.tags)            # []
