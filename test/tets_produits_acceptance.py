import unittest


class TestProduits(unittest.TestCase):
    """ La machine sert différents produits pour varier les plaisirs

    En tant que consommateur
    Je veux commander un latté, un capuccino ou un chocolat
    Afin de varier les plaisirs
    """

    def test_cas_nominal(self):
        """ Le consommateur peut commander différents produits s'il paie

        ETANT DONNE une machine à café ayant le bouton <produit> appuyé n fois
        QUAND on insère un prix supérieur ou égal à celui du <produit> (<prix>)
        ALORS un signal d'écoulement <produit> est reçu par la machine
        ET la somme est encaissée
        CAS (latté, 55cts)
        CAS (chocolat, 60cts)
        CAS (cappuccino, 65cts)
        """

    def test_changement_choix(self):
        """ Le client peut changer d'avis

        ETANT DONNE une machine à café ayant le bouton <produit> appuyé
        ET le bouton <autre_produit> appuyé ensuite
        QUAND on insère un prix supérieur ou égal à celui de <autre_produit> (<prix>)
        ALORS un signal d'écoulement <autre_produit> est reçu par la machine
        ET la somme est encaissée
        CAS (latté, café, 50cts)
        CAS (latté, chocolat, 60cts)
        CAS (latté, capuccino, 65cts)
        CAS (café, latté, 55cts)
        CAS (café, chocolat, 60cts)
        CAS (café, capuccino, 65cts)
        CAS (chocolat, latté, 55cts)
        CAS (chocolat, café, 50cts)
        CAS (chocolat, capuccino, 65cts)
        CAS (capuccino, café, 50cts)
        CAS (capuccino, latté, 55cts)
        CAS (capuccino, chocolat, 60cts)
        """
        pass

    def test_somme_insuffisante(self):
        """ Pas assez d'argent, pas de produit

        ETANT DONNE une machine à café ayant le bouton <produit> appuyé
        QUAND on insère un prix inférieur à celui du <produit> (<prix>)
        ALORS aucun signal d'écoulement de <produit> n'est reçu par la machine
        ET la somme est restituée
        CAS (latté, 55cts)
        CAS (chocolat, 60cts)
        CAS (cappuccino, 65cts)
        """
        pass

    def test_défaillance(self):
        """ On rembourse si la machine est défaillante

        ETANT DONNE une machine à café ayant le bouton <produit> appuyé
        ET défaillante
        QUAND on insère le prix d'un <produit> (<prix>)
        ALORS la somme est restituée
        CAS (latté, 55cts)
        CAS (chocolat, 60cts)
        CAS (cappuccino, 65cts)
        """
        pass