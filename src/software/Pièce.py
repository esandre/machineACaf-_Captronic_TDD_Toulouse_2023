VALEURS_VALIDES_EN_CENTIMES = [1, 2, 5, 10, 20, 50, 100, 200]


class Pièce:
    def __init__(self, valeur_en_centimes: int):
        if valeur_en_centimes not in VALEURS_VALIDES_EN_CENTIMES:
            raise ValueError()

        self.valeur = valeur_en_centimes

    def est_supérieure_ou_égale_a(self, other) -> bool:
        return self.valeur >= other.valeur
