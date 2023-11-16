import random
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

    def test_valeurs_valides(self):
        for valeur in VALEURS_VALIDES_EN_CENTIMES:
            with self.subTest(str(valeur) + 'cts'):
                piece = Pièce(valeur)
                self.assertEqual(valeur, piece.valeur)

    def test_valeurs_invalides(self):
        for valeur in self.__class__.valeurs_invalides_testées():
            with self.subTest(str(valeur) + 'cts'):
                with self.assertRaises(ValueError):
                    Pièce(valeur)


if __name__ == '__main__':
    unittest.main()
