import unittest

from software.MachineACafé import MachineACafé
from software.MachineACafé import PRIX_DU_CAFE
from software.Pièce import Pièce
from utilities.HardwareSpy import HardwareSpy


class TestService(unittest.TestCase):
    def test_cas_nominal(self):
        for pièce in [PRIX_DU_CAFE, Pièce(100), Pièce(200)]:
            with self.subTest(str(pièce.valeur) + "cts"):
                # ETANT DONNE une machine a café reliée à un hardware
                # ET une pièce d'une valeur supérieure ou égale au prix d'un café
                hardware = HardwareSpy()
                machine_a_café = MachineACafé(hardware)

                # QUAND on insère la pièce
                machine_a_café.insérer(pièce)

                # ALORS un signal d'écoulement est envoyé au hardware de la machine
                self.assertTrue(hardware.signal_écoulement_reçu)

                # ET la pièce est encaissée
                self.assertEqual(pièce.valeur, machine_a_café.get_total_encaissé())

    def test_manque_argent(self):
        for pièce in [Pièce(20), Pièce(10), Pièce(5), Pièce(2), Pièce(1)]:
            with self.subTest(str(pièce.valeur) + "cts"):
                # ETANT DONNE une machine a café reliée à un hardware
                # ET une pièce d'une valeur valide inférieure au prix du café
                hardware = HardwareSpy()
                machine_a_café = MachineACafé(hardware)

                # QUAND on insère la pièce
                machine_a_café.insérer(pièce)

                # ALORS aucun signal d'écoulement n'est envoyé au hardware de la machine
                self.assertFalse(hardware.signal_écoulement_reçu)

                # ET la pièce est rendue
                self.assertEqual(0, machine_a_café.get_total_encaissé())
