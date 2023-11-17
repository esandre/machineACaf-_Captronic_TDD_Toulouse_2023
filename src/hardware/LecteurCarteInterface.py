import abc


class LecteurCarteInterface(abc.ABC):
    @abc.abstractmethod
    def wait_for_prepayment(self, for_amount: int, callback: [[bool], bool]):
        """ Enregistre auprès du lecteur un callback à appeler lors de la réception d'un prépaiement

        :param for_amount: le montant du prépaiement à effectuer
        :param callback: le callback appelé en cas de réussite ou d'échec du prépaiement.
            Le booléen en paramètre indique le succès du prépaiement
            Le booléen à renvoyer demande l'abandon (False) ou le prélèvement (True) de la somme
            Attention, prélever si le prépaiement a échoué n'offre aucune garantie de recevoir la somme.
        """
        pass
