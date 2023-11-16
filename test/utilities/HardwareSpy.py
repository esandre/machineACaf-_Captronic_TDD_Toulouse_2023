class HardwareSpy():
    # 0 = tout va bien
    # Pas zéro = problème (non documenté à ce jour)
    def __init__(self):
        self.signal_écoulement_reçu = False

    def declencher_ecoulement(self):
        self.signal_écoulement_reçu = True

    def get_compteur_pieces(self):
        pass


