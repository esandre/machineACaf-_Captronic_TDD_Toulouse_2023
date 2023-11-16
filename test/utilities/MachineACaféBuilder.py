from hardware.HardwareInterface import HardwareInterface
from software.MachineACafé import MachineACafé
from utilities.HardwareDéfaillant import HardwareDéfaillant
from utilities.HardwareStub import HardwareStub


class MachineACaféBuilder:
    __hardware : HardwareInterface = HardwareStub()

    @classmethod
    def default(cls) -> MachineACafé:
        return MachineACaféBuilder().build()

    def build(self) -> MachineACafé:
        return MachineACafé(self.__hardware)

    def ayant_un_hardware_spécifique(self, hardware: HardwareInterface):
        self.__hardware = hardware
        return self

    def ayant_un_hardware_défaillant(self):
        self.__hardware = HardwareDéfaillant()
        return self
