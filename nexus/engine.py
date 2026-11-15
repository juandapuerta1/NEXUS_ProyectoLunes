from .interfaces import IPatronRule, IObserver


class PatronEngine:
    def __init__(self) -> None:
        self.reglas: list[IPatronRule] = []
        self.observadores: list[IObserver] = []

    def agregar_regla(self, regla: IPatronRule) -> None:
        self.reglas.append(regla)

    def suscribir_observador(self, observador: IObserver) -> None:
        self.observadores.append(observador)

    def notificar(self, alerta: str) -> None:
        for observador in self.observadores:
            observador.update(alerta)

    def analyze(self, data: list) -> None:
        for regla in self.reglas:
            if regla.matches(data):
                alerta = f"Patrón detectado: {regla.get_name()} en {data}"
                self.notificar(alerta)
