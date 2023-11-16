import unittest

from software.MachineACafé import MachineACafé
from software.MachineACafé import PRIX_DU_CAFE
from utilities.HardwareSpy import HardwareSpy


class TestService(unittest.TestCase):
    def test_cas_nominal(self):
        # ETANT DONNE une machine a café reliée à un hardware
        # ET une pièce d'une valeur de 50cts
        valeur_pièce_en_centimes = PRIX_DU_CAFE
        hardware = HardwareSpy()
        machine_a_café = MachineACafé(hardware)

        # QUAND on insère la pièce
        machine_a_café.insérer(valeur_pièce_en_centimes)

        # ALORS un signal d'écoulement est envoyé au hardware de la machine
        self.assertTrue(hardware.signal_écoulement_reçu)

    def test_manque_argent(self):
        # ETANT DONNE une machine a café reliée à un hardware
        hardware = HardwareSpy()
        machine_a_café = MachineACafé(hardware)

        # ET une pièce d'une valeur de 49cts
        valeur_pièce_en_centimes = PRIX_DU_CAFE - 1

        # QUAND on insère la pièce
        machine_a_café.insérer(valeur_pièce_en_centimes)

        # ALORS aucun signal d'écoulement n'est envoyé au hardware de la machine
        self.assertFalse(hardware.signal_écoulement_reçu)
