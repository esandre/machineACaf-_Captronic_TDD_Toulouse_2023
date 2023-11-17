from hardware.HardwareInterface import HardwareInterface
from software.MachineACafé import MachineACafé
from utilities.HardwareFake import HardwareFake
from utilities.HardwareSpy import HardwareSpy
from utilities.MachineACaféHarness import MachineACaféHarness


class MachineACaféBuilder:
    __hardware: HardwareFake = HardwareFake()

    @classmethod
    def default(cls) -> MachineACaféHarness:
        return MachineACaféBuilder().build()

    def build(self) -> MachineACaféHarness:
        hardware_spy = HardwareSpy(self.__hardware)
        return MachineACaféHarness(MachineACafé(hardware_spy), hardware_spy, self.__hardware)

    def ayant_un_hardware_défaillant(self):
        self.__hardware = HardwareFake(True)
        return self
