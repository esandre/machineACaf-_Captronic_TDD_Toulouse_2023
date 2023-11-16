class MachineACafé:
    def __init__(self, hardware):
        self.__hardware = hardware

    def insérer(self, valeurPièceEnCentimes):
        self.__hardware.declencher_ecoulement()
        pass
