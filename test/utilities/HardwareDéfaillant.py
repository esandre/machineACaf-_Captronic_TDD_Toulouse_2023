from hardware.HardwareInterface import HardwareInterface


class HardwareDéfaillant(HardwareInterface):
    def declencher_ecoulement(self):
        return 1

    def get_compteur_pieces(self):
        pass


