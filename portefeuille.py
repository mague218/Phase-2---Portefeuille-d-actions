class Portefeuille:
    def __init__(self, bourse):
        self.bourse = bourse
        self.liquidites = 0
        self.actions = {}
        self.transactions = []