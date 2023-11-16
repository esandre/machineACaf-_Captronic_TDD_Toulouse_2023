from hardware.HardwareInterface import HardwareInterface


class HardwareStub(HardwareInterface):
    def declencher_ecoulement(self):
        return 0

    def get_compteur_pieces(self):
        pass


