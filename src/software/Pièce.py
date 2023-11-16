class Pièce:
    __valeurs_valides = [1, 2, 5, 10, 20, 50, 100, 200]

    def __init__(self, valeur):
        if valeur not in self.__valeurs_valides:
            raise ValueError()

        self.valeur = valeur

    def est_supérieure_ou_égale_a(self, other):
        return self.valeur >= other.valeur
