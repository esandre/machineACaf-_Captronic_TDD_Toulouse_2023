import unittest

from software.MachineACafé import MachineACafé
from software.Pièce import Pièce
from utilities.HardwareSpy import HardwareSpy
from utilities.MachineACaféHarness import MachineACaféHarness


class ServiceTestCase(unittest.TestCase):
    def assertSignalEcoulementReçu(self, hardware: HardwareSpy):
        self.assertTrue(hardware.signal_écoulement_reçu)

    def assertAucunSignalEcoulementReçu(self, hardware: HardwareSpy):
        self.assertFalse(hardware.signal_écoulement_reçu)

    def assertAucuneSommeEncaissée(self, machine_a_café: MachineACaféHarness):
        self.assertEqual(0, machine_a_café.get_somme_encaissée())

    def assertPièceEncaissée(self, machine_a_café: MachineACaféHarness, pièce: Pièce):
        self.assertEqual(pièce.valeur, machine_a_café.get_somme_encaissée())