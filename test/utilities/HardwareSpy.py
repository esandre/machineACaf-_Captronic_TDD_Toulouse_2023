from typing import Callable

from hardware.HardwareInterface import HardwareInterface


class HardwareSpy(HardwareInterface):
    def __init__(self, spied: HardwareInterface):
        self.signal_écoulement_reçu = False
        self.__decorated = spied

    def make_coffee(self) -> int:
        self.signal_écoulement_reçu = True
        return self.__decorated.make_coffee()

    def register_money_inserted_callback(self, callback: Callable[[], int]):
        pass


