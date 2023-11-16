import unittest

from software.MachineACafé import MachineACafé
from software.Pièce import Pièce
from utilities.HardwareSpy import HardwareSpy
from utilities.MachineACaféHarness import MachineACaféHarness


class ServiceTestCase(unittest.TestCase):
    def assertSignalEcoulementReçuParLeHardware(self, machine_a_café: MachineACaféHarness):
        self.assertTrue(machine_a_café.signal_ecoulement_reçu_par_le_hardware())

    def assertAucunSignalEcoulementReçuParLeHardware(self, machine_a_café: MachineACaféHarness):
        self.assertFalse(machine_a_café.signal_ecoulement_reçu_par_le_hardware())

    def assertAucuneSommeEncaissée(self, machine_a_café: MachineACaféHarness):
        self.assertEqual(0, machine_a_café.get_somme_encaissée())

    def assertPièceEncaissée(self, machine_a_café: MachineACaféHarness, pièce: Pièce):
        self.assertEqual(pièce.valeur, machine_a_café.get_somme_encaissée())