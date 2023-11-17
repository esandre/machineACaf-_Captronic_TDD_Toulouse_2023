from typing import Callable

from hardware.HardwareInterface import HardwareInterface


class HardwareSpy(HardwareInterface):
    def __init__(self, spied: HardwareInterface):
        self.make_coffee_appelé = False
        self.__decorated = spied

    def make_product(self) -> int:
        self.make_coffee_appelé = True
        return self.__decorated.make_product()

    def register_money_inserted_callback(self, callback: Callable[[int], bool]):
        pass


