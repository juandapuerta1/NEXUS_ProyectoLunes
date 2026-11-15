from nexus.engine import PatronEngine
from nexus.facade import CasinoScraperFacade
from nexus.observers import DatabaseObserver, MockPostgresRepo, TelegramObserver
from nexus.rules import CorteRachaRule


def main() -> None:
    repository = MockPostgresRepo()
    observadores = [TelegramObserver(), DatabaseObserver(repository)]

    engine = PatronEngine()
    engine.agregar_regla(CorteRachaRule(cantidad=3))
    for observador in observadores:
        engine.suscribir_observador(observador)

    facade = CasinoScraperFacade()
    facade.conectar_mesa("https://casino.example/mesa/roulette")
    data = facade.capturar_ronda_simulada()
    engine.analyze(data)


if __name__ == "__main__":
    main()
