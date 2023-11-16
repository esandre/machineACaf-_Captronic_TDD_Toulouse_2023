import unittest

from software.MachineACafé import MachineACafé
from utilities.HardwareSpy import HardwareSpy


class TestService(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine a café reliée à un hardware
        # ET une pièce d'une valeur de 50cts
        valeur_pièce_en_centimes = 50
        hardware = HardwareSpy()
        machine_a_café = MachineACafé(hardware)

        # QUAND on insère la pièce
        machine_a_café.insérer(valeur_pièce_en_centimes)

        # ALORS un signal d'écoulement est envoyé au hardware la machine
        self.assertTrue(hardware.signal_écoulement_reçu)

