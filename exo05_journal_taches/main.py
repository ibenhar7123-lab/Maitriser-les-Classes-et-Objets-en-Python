import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from exo05_journal_taches.journal import JournalTaches

with JournalTaches("taches_demo.txt") as journal:
    journal.ajouter_tache("Réviser la POO")
    journal.ajouter_tache("Faire le TP 1")
# Le fichier est fermé automatiquement ici

with open("taches_demo.txt", "r", encoding="utf-8") as f:
    print(f.read())
