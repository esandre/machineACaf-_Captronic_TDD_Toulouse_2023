class Pièce:
    def __init__(self, valeur):
        self.valeur = valeur

    def est_supérieure_ou_égale_a(self, other):
        return self.valeur >= other.valeur
