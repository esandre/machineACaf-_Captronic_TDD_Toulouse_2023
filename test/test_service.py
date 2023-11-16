import unittest

from software.MachineACafé import MachineACafé
from software.MachineACafé import PRIX_DU_CAFE
from software.Pièce import Pièce
from utilities.HardwareSpy import HardwareSpy


class TestService(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine a café reliée à un hardware
        # ET une pièce d'une valeur de 50cts
        pièce = PRIX_DU_CAFE
        hardware = HardwareSpy()
        machine_a_café = MachineACafé(hardware)

        # QUAND on insère la pièce
        machine_a_café.insérer(pièce)

        # ALORS un signal d'écoulement est envoyé au hardware de la machine
        self.assertTrue(hardware.signal_écoulement_reçu)

    def test_manque_argent(self):
        # ETANT DONNE une machine a café reliée à un hardware
        hardware = HardwareSpy()
        machine_a_café = MachineACafé(hardware)

        # ET une pièce d'une valeur valide inférieure à 50cts
        pièce = Pièce(20)

        # QUAND on insère la pièce
        machine_a_café.insérer(pièce)

        # ALORS aucun signal d'écoulement n'est envoyé au hardware de la machine
        self.assertFalse(hardware.signal_écoulement_reçu)
