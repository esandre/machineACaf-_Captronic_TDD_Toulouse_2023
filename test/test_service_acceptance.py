from software.MachineACafé import PRIX_DU_CAFE
from software.Pièce import Pièce
from utilities.HardwareSpy import HardwareSpy
from utilities.HardwareStub import HardwareStub
from utilities.MachineACaféBuilder import MachineACaféBuilder
from utilities.serviceTestCase import ServiceTestCase


class TestService(ServiceTestCase):
    def test_cas_nominal(self):
        for pièce in [PRIX_DU_CAFE, Pièce(100), Pièce(200)]:
            with self.subTest(str(pièce.valeur) + "cts"):
                # ETANT DONNE une machine a café reliée à un hardware
                # ET une pièce d'une valeur supérieure ou égale au prix d'un café
                hardware = HardwareSpy(HardwareStub())
                machine_a_café = (MachineACaféBuilder()
                                  .ayant_un_hardware_spécifique(hardware)
                                  .build())

                # QUAND on insère la pièce
                machine_a_café.insérer(pièce)

                # ALORS un signal d'écoulement est envoyé au hardware de la machine
                self.assertSignalEcoulementReçu(hardware)

                # ET la pièce est encaissée
                self.assertPièceEncaissée(machine_a_café, pièce)

    def test_manque_argent(self):
        for pièce in [Pièce(20), Pièce(10), Pièce(5), Pièce(2), Pièce(1)]:
            with self.subTest(str(pièce.valeur) + "cts"):
                # ETANT DONNE une machine a café reliée à un hardware
                # ET une pièce d'une valeur valide inférieure au prix du café
                hardware = HardwareSpy(HardwareStub())
                machine_a_café = MachineACaféBuilder().ayant_un_hardware_spécifique(hardware).build()

                # QUAND on insère la pièce
                machine_a_café.insérer(pièce)

                # ALORS aucun signal d'écoulement n'est envoyé au hardware de la machine
                self.assertAucunSignalEcoulementReçu(hardware)

                # ET la pièce est rendue
                self.assertAucuneSommeEncaissée(machine_a_café)

    def test_defaut(self):
        machine_a_café = (MachineACaféBuilder()
                          .ayant_un_hardware_défaillant()
                          .build())

        machine_a_café.insérer(PRIX_DU_CAFE)

        self.assertAucuneSommeEncaissée(machine_a_café)
