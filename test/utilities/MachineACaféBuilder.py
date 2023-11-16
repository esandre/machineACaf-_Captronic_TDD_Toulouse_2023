from hardware.HardwareInterface import HardwareInterface
from software.MachineACafé import MachineACafé
from utilities.HardwareDéfaillant import HardwareDéfaillant
from utilities.HardwareSpy import HardwareSpy
from utilities.HardwareStub import HardwareStub
from utilities.MachineACaféHarness import MachineACaféHarness


class MachineACaféBuilder:
    __hardware: HardwareInterface = HardwareStub()

    @classmethod
    def default(cls) -> MachineACaféHarness:
        return MachineACaféBuilder().build()

    def build(self) -> MachineACaféHarness:
        hardware = HardwareSpy(self.__hardware)
        return MachineACaféHarness(MachineACafé(hardware), hardware)

    def ayant_un_hardware_défaillant(self):
        self.__hardware = HardwareDéfaillant()
        return self
