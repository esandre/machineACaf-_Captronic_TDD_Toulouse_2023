from software.MachineACafé import MachineACafé
from software.Pièce import Pièce


class MachineACaféHarness:
    def __init__(self, harnessed: MachineACafé):
        self.__harnessed = harnessed
        self.__somme_initiale = harnessed.get_total_encaissé()

    def insérer(self, pièce: Pièce):
        return self.__harnessed.insérer(pièce)

    def get_total_encaissé(self) -> int:
        return self.__harnessed.get_total_encaissé()

    def get_somme_encaissée(self) -> int:
        return self.get_total_encaissé() - self.__somme_initiale
