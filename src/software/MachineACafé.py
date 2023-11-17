from hardware.HardwareInterface import HardwareInterface
from software.Pièce import Pièce

PRIX_DU_CAFE = Pièce(50)


class MachineACafé:
    def __init__(self, hardware: HardwareInterface):
        self.__total_encaissé = 50
        self.__hardware = hardware
        hardware.register_money_inserted_callback(
            lambda amount: self.__insérer(Pièce(amount))
        )

    def __insérer(self, pièce: Pièce):
        if pièce.est_supérieure_ou_égale_a(PRIX_DU_CAFE):
            code_retour_hardware = self.__hardware.make_product()
            est_succes = code_retour_hardware == 0

            if est_succes:
                self.__total_encaissé += pièce.valeur
                return True
        return False

    def get_total_encaissé(self) -> int:
        return self.__total_encaissé
