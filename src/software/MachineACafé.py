PRIX_DU_CAFE = 50


class MachineACafé:
    def __init__(self, hardware):
        self.__hardware = hardware

    def insérer(self, valeur_pièce_en_centimes):
        if valeur_pièce_en_centimes >= PRIX_DU_CAFE:
            self.__hardware.declencher_ecoulement()
        pass
