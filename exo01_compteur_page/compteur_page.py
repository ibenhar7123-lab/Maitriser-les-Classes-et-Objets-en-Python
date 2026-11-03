class CompteurPage:
    # Attribut de classe : partagé par toutes les instances
    total_visites = 0

    def __init__(self, nom_page):
        # Attributs d'instance : uniques à chaque objet
        self.nom_page = nom_page
        self.visites = 0

    def ajouter_visite(self):
        self.visites += 1
        CompteurPage.total_visites += 1

    def afficher_statistiques(self):
        return f"Page '{self.nom_page}': {self.visites} visites. Total global: {CompteurPage.total_visites}"
