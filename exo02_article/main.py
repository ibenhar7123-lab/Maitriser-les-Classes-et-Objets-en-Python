import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo02_article.article import Article

a1 = Article("REF-001", "Clavier Mécanique", 89.99, 10)
print(round(a1.valeur_stock(), 2))  # 899.9
a1.ajouter_stock(5)
print(a1)  # [REF-001] Clavier Mécanique - Stock: 15 - Prix HT: 89.99€

try:
    a1.ajouter_stock(-3)
except ValueError as e:
    print("Erreur :", e)
