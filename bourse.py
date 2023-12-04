import requests
import json
from exceptions import ErreurDate
from datetime import datetime, timedelta


class Bourse:
    def __init__(self, source_donnees='https://pax.ulaval.ca'):
        self.source_donnees = source_donnees

    def obtenir_prix_historique(self, symbole, date):
        url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

        params = {'début': "", 'fin': date}

        reponse = requests.get(url=url, params=params, timeout=100)
        donnees = json.loads(reponse.text)
        
        donnees_historiques = donnees.get("historique", {})
        if date in donnees_historiques:
            return donnees_historiques[date]["fermeture"]

        date_actuelle = datetime.now().date()
        if datetime.strptime(date, '%Y-%m-%d').date() > date_actuelle:
            raise ErreurDate("Date postérieure à la date du jour.")
        
        dates_anterieures = [d for d in donnees_historiques if d < date]
        if dates_anterieures:
            date_precedente_recente = max(dates_anterieures)
            return donnees_historiques[date_precedente_recente]["fermeture"]
        else:
            raise ValueError("Aucune date antérieure à la date spécifiée trouvée.")