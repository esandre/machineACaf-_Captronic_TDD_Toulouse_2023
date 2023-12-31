import random
import sys
import unittest

from software.Pièce import Pièce, VALEURS_VALIDES_EN_CENTIMES


class TestValeurPièces(unittest.TestCase):
    @classmethod
    def valeurs_invalides_testées(cls):
        # Test des limites supérieures et inférieures des valeurs valides
        for valeurValide in VALEURS_VALIDES_EN_CENTIMES:
            valeur_supérieure = valeurValide + 1
            if valeur_supérieure not in VALEURS_VALIDES_EN_CENTIMES:
                yield valeur_supérieure

            valeur_inférieure = valeurValide - 1
            if valeur_inférieure not in VALEURS_VALIDES_EN_CENTIMES:
                yield valeur_inférieure

    @classmethod
    def valeurs_invalides_avec_random(cls):
        valeurs_invalides_testées = list(cls.valeurs_invalides_testées())
        valeurs_déjà_testées = valeurs_invalides_testées + VALEURS_VALIDES_EN_CENTIMES

        random_value = 0
        while random_value in valeurs_déjà_testées:
            random_value = random.randint(0, (sys.maxsize * 2 + 1))

        return valeurs_invalides_testées + [random_value]

    def test_valeurs_valides(self):
        for valeur in VALEURS_VALIDES_EN_CENTIMES:
            with self.subTest(Pièce.to_string(valeur)):
                piece = Pièce(valeur)
                self.assertEqual(valeur, piece.valeur)

    def test_valeurs_invalides(self):
        for valeur in self.__class__.valeurs_invalides_avec_random():
            with self.subTest(Pièce.to_string(valeur)):
                with self.assertRaises(ValueError):
                    Pièce(valeur)


if __name__ == '__main__':
    unittest.main()
