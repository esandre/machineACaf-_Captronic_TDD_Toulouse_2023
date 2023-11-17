from typing import Callable

from hardware.HardwareInterface import HardwareInterface


class HardwareSpy(HardwareInterface):
    def __init__(self, spied: HardwareInterface):
        self.__make_product_invocations = []
        self.__decorated = spied

    def make_product(self,
                     coffee: bool = True,
                     more_water: bool = False,
                     milk: bool = False,
                     chocolate: bool = False) -> int:
        self.__make_product_invocations.append((coffee, more_water, milk, chocolate))
        return self.__decorated.make_product()

    def register_money_inserted_callback(self, callback: Callable[[int], bool]):
        pass

    def make_product_appelé(self):
        return len(self.__make_product_invocations) > 0


