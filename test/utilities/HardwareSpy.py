from hardware.HardwareInterface import HardwareInterface


class HardwareSpy(HardwareInterface):
    def __init__(self, spied: HardwareInterface):
        self.signal_écoulement_reçu = False
        self.__decorated = spied

    def declencher_ecoulement(self):
        self.signal_écoulement_reçu = True
        return self.__decorated.declencher_ecoulement()

    def get_compteur_pieces(self):
        return self.__decorated.get_compteur_pieces()


