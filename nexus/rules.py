from .interfaces import IPatronRule


class CorteRachaRule(IPatronRule):
    def __init__(self, cantidad: int = 3) -> None:
        if cantidad < 1:
            raise ValueError("cantidad debe ser mayor que cero")
        self.cantidad = cantidad

    def matches(self, data: list) -> bool:
        if len(data) < self.cantidad:
            return False
        ultimos = data[-self.cantidad:]
        return all(elemento == ultimos[0] for elemento in ultimos)

    def get_name(self) -> str:
        return "CorteRachaRule"
