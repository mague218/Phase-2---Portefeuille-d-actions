from datetime import datetime


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
    
    def solde(self, date=None):
        """méthode acceptant une date d'évaluation"""
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")

        return self.liquidites
    
    def acheter(self, symbole, quantite, date=None):
        """accepte symbole quantite et une date désirée"""
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")

        prix_achat = self.bourse.obtenir_prix_historique(symbole, date.strftime('%Y-%m-%d')) * quantite

        if prix_achat > self.liquidites:
            raise LiquiditeInsuffisante("Liquidités insuffisantes pour effectuer l'achat.")

        if symbole in self.actions:
            self.actions[symbole] += quantite
        else:
            self.actions[symbole] = quantite

        self.liquidites -= prix_achat
        self.transactions.append({'type': 'Achat', 'symbole': symbole, 'prix_achat': prix_achat, 'solde': self.solde(), 'quantite': quantite, 'date': date})

    def vendre(self, symbole, quantite, date=None):
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")
        if symbole not in self.actions or self.actions[symbole] < quantite:
            raise ErreurQuantite("Quantité insuffisante d'actions à vendre.")
        
        prix_vente = self.bourse.obtenir_prix_historique(symbole.date.strftime('%Y-%m-%d'))

        
        self.actions[symbole] -= quantite
        self.liquidites += prix_vente
        self.transactions.append({'type': 'Vente', 'symbole': symbole, 'prix_vente': prix_vente, 'solde': self.solde(), 'quantite': quantite, 'date': date})
        print(self.transactions)
        

    
