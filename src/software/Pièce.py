VALEURS_VALIDES_EN_CENTIMES = [1, 2, 5, 10, 20, 50, 100, 200]


class Pièce:
    def __init__(self, valeur_en_centimes: int):
        if valeur_en_centimes not in VALEURS_VALIDES_EN_CENTIMES:
            raise ValueError()

        self.valeur = valeur_en_centimes

    def est_supérieure_ou_égale_a(self, other) -> bool:
        return self.valeur >= other.valeur

    @classmethod
    def to_string(cls, valeur):
        euros = round(valeur / 100)
        cents = valeur % 100

        if euros > 0 and cents > 0:
            return f"{euros},{cents:02d}€"
        if cents > 0:
            return str(cents) + "cts"
        return str(euros) + "€"

    def __str__(self):
        self.__class__.to_string(self.valeur)
