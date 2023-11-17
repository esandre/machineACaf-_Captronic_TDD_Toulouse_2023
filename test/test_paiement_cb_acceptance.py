class TestPaiementCB:
    """ Paiement par carte bleue

    En tant que consommateur
    Je veux payer par carte
    Afin de ne pas être bloqué si je n'ai pas de monnaie
    """

    def test_cas_nominal(self):
        """ Paiement par carte réussi

        ETANT DONNE une machine équipée d'un lecteur de cartes
        QUAND le lecteur signale un pré-paiement réussi
        ALORS le prépaiement est confirmé
        ET un signal d'écoulement café est reçu par la machine
        """
        pass

    def test_echec_prepaiement(self):
        """ Paiement par carte dont le prépaiement échoue

        ETANT DONNE une machine équipée d'un lecteur de cartes
        QUAND le lecteur signale un pré-paiement échoué
        ALORS aucun signal d'écoulement café n'est reçu par la machine
        """
        pass

    def test_défaillance_remboursement(self):
        """ Défaillance de la machine entraînant l'abandon du prépaiement

        ETANT DONNE une machine équipée d'un lecteur de cartes
        ET défaillante
        QUAND le lecteur signale un pré-paiement réussi
        ALORS le prépaiement est abandonné
        """

        