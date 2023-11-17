from software.MachineACafé import PRIX_DU_CAFE
from software.Pièce import Pièce
from utilities.MachineACaféBuilder import MachineACaféBuilder
from utilities.serviceTestCase import ServiceTestCase


class TestService(ServiceTestCase):
    def test_cas_nominal(self):
        for pièce in [PRIX_DU_CAFE, Pièce(100), Pièce(200)]:
            with self.subTest(str(pièce.valeur) + "cts"):
                machine_a_café = MachineACaféBuilder.default()

                machine_a_café.insérer(pièce)

                self.assertSignalEcoulementReçuParLeHardware(machine_a_café)
                self.assertPièceEncaissée(machine_a_café, pièce)

    def test_manque_argent(self):
        for pièce in [Pièce(20), Pièce(10), Pièce(5), Pièce(2), Pièce(1)]:
            with self.subTest(str(pièce.valeur) + "cts"):
                machine_a_café = MachineACaféBuilder.default()


                machine_a_café.insérer(pièce)

                self.assertAucunSignalEcoulementReçuParLeHardware(machine_a_café)
                self.assertAucuneSommeEncaissée(machine_a_café)

    def test_defaut(self):
        machine_a_café = (MachineACaféBuilder()
                          .ayant_un_hardware_défaillant()
                          .build())

        machine_a_café.insérer(PRIX_DU_CAFE)

        self.assertAucuneSommeEncaissée(machine_a_café)
