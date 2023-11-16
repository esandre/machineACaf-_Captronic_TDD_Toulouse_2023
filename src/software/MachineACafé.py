from hardware.HardwareInterface import HardwareInterface
from software.Pièce import Pièce

PRIX_DU_CAFE = Pièce(50)


class MachineACafé:
    def __init__(self, hardware: HardwareInterface):
        self.__hardware = hardware

    def insérer(self, pièce):
        if pièce.est_supérieure_ou_égale_a(PRIX_DU_CAFE):
            self.__hardware.declencher_ecoulement()
        pass
