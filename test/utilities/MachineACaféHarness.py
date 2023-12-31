from software.MachineACafé import MachineACafé
from software.Pièce import Pièce
from utilities.HardwareFake import HardwareFake
from utilities.HardwareSpy import HardwareSpy


class MachineACaféHarness:
    def __init__(self,
                 harnessed: MachineACafé,
                 hardware_spy: HardwareSpy,
                 hardware_fake: HardwareFake):
        self.__hardware_fake = hardware_fake
        self.__harnessed = harnessed
        self.__somme_initiale = harnessed.get_total_encaissé()
        self.__hardware_spy = hardware_spy

    def signal_ecoulement_reçu_par_le_hardware(self):
        return self.__hardware_spy.make_product_appelé()

    def insérer(self, pièce: Pièce):
        return self.__hardware_fake.simuler_insertion_pièce(pièce.valeur)

    def get_total_encaissé(self) -> int:
        return self.__harnessed.get_total_encaissé()

    def get_somme_encaissée(self) -> int:
        return self.get_total_encaissé() - self.__somme_initiale
