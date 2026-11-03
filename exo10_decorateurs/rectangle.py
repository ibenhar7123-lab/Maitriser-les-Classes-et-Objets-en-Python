from .validateurs import valider_positif


class Rectangle:
    def __init__(self, largeur: float, hauteur: float):
        self.largeur = largeur
        self.hauteur = hauteur

    @valider_positif(1)  # index 0 = self, index 1 = facteur
    def aire(self, facteur: float = 1.0) -> float:
        return self.largeur * self.hauteur * facteur
