from datetime import datetime


class ErreurDate(RuntimeError):
   """Exception levée pour des erreurs liées à des dates."""
pass


class ErreurQuantite(RuntimeError):
   """Exception levée pour des erreurs liées à la quantité"""
pass


class LiquiditeInsuffisante(RuntimeError):
   """Exception levée pour des erreurs liées à la liquidité."""
pass


class Portefeuille:
    def __init__(self, bourse):
        """méthode d'innitialisation"""
        self.bourse = bourse
        self.liquidites = 0
        self.actions = {}
        self.transactions = []

    def deposer(self, montant, date=None):
        """méthode acceptant montant et date de transaction"""
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")

        self.liquidites += montant
        self.transactions.append({'type': 'Dépôt', 'montant': montant, 'date': date})