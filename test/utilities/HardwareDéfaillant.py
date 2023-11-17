from typing import Callable

from hardware.HardwareInterface import HardwareInterface


class HardwareDéfaillant(HardwareInterface):
    def make_product(self) -> int:
        return 1

    def register_money_inserted_callback(self, callback: Callable[[int], bool]):
        pass


