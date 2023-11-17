import unittest


class TestCaféAllongé(unittest.TestCase):
    """ Fonctionnalité permettant de demander plus d'eau sur un café

    En tant que consommateur
    Je veux ajouter de l'eau
    Afin de ne pas boire un café trop serré
    """

    def test_cas_nominal(self):
        """ Appui simple sur le bouton "plus d'eau"

            ETANT DONNE une machine ayant le bouton "plus d'eau" appuyé un nombre impair de fois
            QUAND on insère une somme supérieure ou égale au prix d'un café
            ALORS la somme est encaissée
            ET un signal d'écoulement café allongé est reçu par la machine
        """
        pass

    def test_bouton_réappuyé(self):
        """ Réappuyer sur le bouton remet le café en mode court
            ETANT DONNE une machine ayant le bouton "plus d'eau" appuyé un nombre pair de fois
            QUAND on insère une somme supérieure ou égale au prix d'un café
            ALORS la somme est encaissée
            ET un signal d'écoulement café court est reçu par la machine
        """
        pass

    def test_reset_après_paiement(self):
        """ Si un café est servi, remise à zéro du statut allongé
            ETANT DONNE une machine ayant le bouton "plus d'eau" appuyé
            QUAND on insère deux fois de suite une somme supérieure ou égale au prix d'un café
            ALORS un signal d'écoulement café allongé est reçu par la machine
            ET un signal d'écoulement café court est reçu par la machine
        """
        pass

    def test_reset_après_échec_paiement(self):
        """ Si aucun café n'est servi, remise à zéro du statut allongé
            ETANT DONNE une machine ayant le bouton "plus d'eau" appuyé
            ET qu'une somme inférieure au prix d'un café a été insérée
            QUAND on insère une somme supérieure ou égale au prix d'un café
            ALORS un signal d'écoulement café court est reçu par la machine
        """
        pass
