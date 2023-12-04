"""Module pour définir un portefeuille d'action"""
from datetime import datetime
from exceptions import ErreurDate, ErreurQuantité, LiquiditéInsuffisante


class Portefeuille:
    """Classe pour encapsuler les actions du portefeuille"""
    def __init__(self, bourse):
        """méthode d'initialisation"""
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
        """Effectuer l'achat de la quantité d'actions du titre symbole à la date spécifiée"""
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")

        K = symbole, date.strftime('%Y-%m-%d')
        prix_achat = self.bourse.obtenir_prix_historique(K) * quantite

        if prix_achat > self.liquidites:
            raise LiquiditéInsuffisante("Liquidités insuffisantes pour effectuer l'achat.")

        if symbole in self.actions:
            self.actions[symbole] += quantite
        else:
            self.actions[symbole] = quantite

        self.liquidites -= prix_achat
        self.transactions.append({'type': 'Achat',
                                  'symbole': symbole,
                                  'prix_achat': prix_achat,
                                  'solde': self.solde(),
                                  'quantite': quantite,
                                  'date': date})

    def vendre(self, symbole, quantite, date=None):
        """Effectuer une vente de la quantité d'action du titre du symbole à la date spécifiée"""
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")
        if symbole not in self.actions or self.actions[symbole] < quantite:
            raise ErreurQuantité("Quantité insuffisante d'actions à vendre.")
        prix_vente = self.bourse.obtenir_prix_historique(symbole.date.strftime('%Y-%m-%d'))

        self.actions[symbole] -= quantite
        self.liquidites += prix_vente
        self.transactions.append({'type': 'Vente',
                                  'symbole': symbole,
                                  'prix_vente': prix_vente,
                                  'solde': self.solde(),
                                  'quantite': quantite,
                                  'date': date})
        print(self.transactions)
    def valeur_totale(self, date=None):
        """Méthode retournant la valeur totale du portefeuille à cette date"""
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")
        valeur_liquidites = self.liquidites
        valeur_actions = sum(self.bourse.obtenir_prix_historique(sym, date.strftime('%Y-%m-%d')) * quant for sym, quant in self.actions.items())
        return valeur_liquidites + valeur_actions
    def valeur_actions(self, symboles, date=None):
        """Méthode retournant pour la date spécifiée la valeur totale des titres spécifiés"""
        date = date or datetime.now().date()
        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")
        valeur_actions = sum(self.bourse.obtenir_prix_historique(sym, date.strftime("%Y-%m-%d")) * quant for sym, quant in self.actions.items() if sym in symboles)
        return valeur_actions
    def actions_detenues(self, date=None):
        """Méthode retournant les actions détenues à la date spécifiée"""
        date = date or datetime.now().date()

        if date > datetime.now().date():
            raise ErreurDate("La date spécifiée est postérieure à la date du jour.")

        return {sym: quant for sym, quant in self.actions.items()}

    def  valeur_projetee(self, date, taux_rendement):
        """Méthode retournant la valeur du portefeuille projetée à cette date en supposant le ou les rendements spécifiés"""    
        if date <= datetime.now().date():
            raise ErreurDate("La date future spécifiée est antérieure ou égale à la date du jour.")
        valeur_projetee = self.liquidites
        for sym, quant in self.actions.items():
            taux_rendement_titre = taux_rendement if isinstance(taux_rendement, (int, float)) else taux_rendement.get(sym, 0)
            prix_titre = self.bourse.obtenir_prix_historique(sym, date.strftime('%Y-%m-%d'))
            valeur_projetee += quant * prix_titre * (1 + taux_rendement_titre / 100)

        return valeur_projetee
