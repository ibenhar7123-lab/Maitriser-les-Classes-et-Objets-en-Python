class JournalTaches:
    def __init__(self, nom_fichier: str = "journal.txt"):
        self.nom_fichier = nom_fichier
        self.fichier = None

    def __enter__(self):
        """Appelé au début du bloc with."""
        self.fichier = open(self.nom_fichier, 'a', encoding='utf-8')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Appelé à la fin du bloc with."""
        if self.fichier:
            self.fichier.close()
            self.fichier = None
        # False : les exceptions éventuelles sont propagées
        return False

    def ajouter_tache(self, description: str):
        """Ajoute une tâche au journal."""
        if self.fichier:
            self.fichier.write(f"- {description}\n")
        else:
            raise RuntimeError("Le journal n'est pas ouvert. Utilisez 'with'.")
