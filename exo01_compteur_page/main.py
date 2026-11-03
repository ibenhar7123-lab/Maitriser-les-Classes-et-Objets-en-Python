import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo01_compteur_page.compteur_page import CompteurPage

page1 = CompteurPage("Accueil")
page2 = CompteurPage("Contact")

page1.ajouter_visite()
page1.ajouter_visite()
page2.ajouter_visite()

print(page1.afficher_statistiques())  # Page 'Accueil': 2 visites. Total global: 3
print(page2.afficher_statistiques())  # Page 'Contact': 1 visites. Total global: 3
print(CompteurPage.total_visites)     # 3
