from hardware.HardwareInterface import HardwareInterface
from software.Pièce import Pièce

PRIX_DU_CAFE = Pièce(50)


class MachineACafé:
    def __init__(self, hardware: HardwareInterface):
        self.__total_encaissé = 0
        self.__hardware = hardware

    def insérer(self, pièce):
        if pièce.est_supérieure_ou_égale_a(PRIX_DU_CAFE):
            code_retour_hardware = self.__hardware.declencher_ecoulement()
            est_succes = code_retour_hardware == 0

            if est_succes:
                self.__total_encaissé += pièce.valeur

    def get_total_encaissé(self):
        return self.__total_encaissé
