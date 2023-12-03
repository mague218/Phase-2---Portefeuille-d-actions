import requests
import json


class Bourse:
    def __init__(self):
        pass

    def obtenir_prix_historique(self, symbole, date):
        url = f'https://pax.ulaval.ca/action/{symbole}/historique/'

        params = {'début': "", 'fin': date}

        reponse = requests.get(url=url, params=params, timeout=100)
        donnees = json.loads(reponse.text) 