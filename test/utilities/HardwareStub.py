from typing import Callable

from hardware.HardwareInterface import HardwareInterface


class HardwareStub(HardwareInterface):
    def make_coffee(self) -> int:
        return 0

    def register_money_inserted_callback(self, callback: Callable[[], int]):
        pass


