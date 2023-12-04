class ErreurDate(RuntimeError):
    def __init__(self, message="Erreur de date"):
        """Exception levée pour des erreurs liées à des dates."""
        self.message = message
        super().__init__(self.message)

class ErreurQuantité(RuntimeError):
    def __init__(self, message="Erreur de quantité"):
        """Exception levée pour des erreurs liées à la quantité"""
        self.message = message
        super().__init__(self.message)

class LiquiditéInsuffisante(RuntimeError):
    def __init__(self, message="Liquidité insuffisante"):
        """Exception levée pour des erreurs liées à la liquidité."""
        self.message = message
        super().__init__(self.message)