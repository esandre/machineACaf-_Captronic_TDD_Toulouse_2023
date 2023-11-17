from typing import Callable

from hardware.HardwareInterface import HardwareInterface


class HardwareFake(HardwareInterface):
    __money_inserted_callback: Callable[[int], bool] = None

    def __init__(self, en_defaut=False):
        self.__en_defaut = en_defaut

    def make_product(self, coffee: bool = True, more_water: bool = False, milk: bool = False,
                     chocolate: bool = False) -> int:
        return 1 if self.__en_defaut else 0

    def register_money_inserted_callback(self, callback: Callable[[int], bool]):
        self.__money_inserted_callback = callback

    def simuler_insertion_pièce(self, amount: int):
        self.__money_inserted_callback(amount)
