from abc import ABC, abstractmethod


class HardwareInterface(ABC):
    # 0 = tout va bien
    # Pas zéro = problème (non documenté à ce jour)
    @abstractmethod
    def declencher_ecoulement(self):
        pass

    @abstractmethod
    def get_compteur_pieces(self):
        pass
