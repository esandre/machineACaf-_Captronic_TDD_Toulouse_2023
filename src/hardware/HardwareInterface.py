from abc import ABC, abstractmethod
from typing import Callable


class HardwareInterface(ABC):
    # 0 = tout va bien
    # Pas zéro = problème (non documenté à ce jour)
    @abstractmethod
    def make_coffee(self) -> int:
        pass

    @abstractmethod
    def register_money_inserted_callback(self, callback: Callable[[], int]):
        pass
