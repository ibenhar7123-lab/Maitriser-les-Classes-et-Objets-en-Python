import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo03_carnet_adresses.contact import Contact
from exo03_carnet_adresses.carnet import Carnet

carnet = Carnet()
c1 = Contact("Alice Dupont", "0612345678", "alice@example.com")
c2 = Contact("Bob Martin", "0698765432", "bob@example.com")
carnet.ajouter(c1)
carnet.ajouter(c2)

print(c1.initiale)             # A
print(carnet.chercher("ali"))  # [Contact(nom='Alice Dupont', email='alice@example.com')]
print(len(carnet))             # 2
