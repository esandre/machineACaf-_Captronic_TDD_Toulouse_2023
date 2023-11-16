import random
import unittest

from software.Pièce import Pièce


class MyTestCase(unittest.TestCase):
    def test_valeurs_valides(self):
        for valeur in [1, 2, 5, 10, 20, 50, 100, 200]:
            with self.subTest(str(valeur) + 'cts'):
                piece = Pièce(valeur)
                self.assertEqual(valeur, piece.valeur)

    def test_valeurs_invalides(self):
        for valeur in [0, 3, 4, 6, 9, 11, 19, 21, 49, 51, 99, 101, 199, 201]:
            with self.subTest(str(valeur) + 'cts'):
                with self.assertRaises(ValueError):
                    Pièce(valeur)


if __name__ == '__main__':
    unittest.main()
