from abc import ABC, abstractmethod
from typing import Callable


class HardwareInterface(ABC):
    @abstractmethod
    def make_coffee(self) -> int:
        """
        Déclenche l'écoulement d'un café
        :return: un code d'erreur éventuel ou 0 si tout est ok
        """
        pass

    @abstractmethod
    def register_money_inserted_callback(self, callback: Callable[[int], bool]):
        """ Enregistre un callback appelé lorsque le hardware reçoit une pièce
        Le callback envoie un entier qui correspont à la valeur de la pièce.
        0 : pièce invalide
        Le retour booléen correspond à l'encaissement de la pièce (true) où à son renvoi (false)
        """
        pass
