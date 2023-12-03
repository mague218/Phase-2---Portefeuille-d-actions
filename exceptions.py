class ErreurDate(RuntimeError):
   """Exception levée pour des erreurs liées à des dates."""
pass


class ErreurQuantite(RuntimeError):
   """Exception levée pour des erreurs liées à la quantité"""
pass


class LiquiditeInsuffisante(RuntimeError):
   """Exception levée pour des erreurs liées à la liquidité."""
pass
