import sys
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


def demostrar_flujos_alternativos() -> None:
    print("=== Demostración de Flujos Alternativos (Entregable 3) ===")
    facade = CasinoScraperFacade(frecuencia_seg=30)
    try:
        facade.conectar_mesa("https://casino.example/mesa/roulette", simular_timeout=True)
    except TimeoutError:
        facade.reconectar_mesa("https://casino.example/mesa/roulette", max_reintentos=3)

    data_parcial = ["Rojo", "Negro", "Rojo"]
    engine = PatronEngine()
    engine.agregar_regla(CorteRachaRule(cantidad=3))
    engine.analyze(data_parcial)

    tg_obs = TelegramObserver(max_retries=3)
    tg_obs.update("Patrón detectado: CorteRachaRule", simular_fallo_red=True)

    db_desconectada = MockPostgresRepo(conectado=False)
    db_obs = DatabaseObserver(db_desconectada)
    db_obs.update("Patrón detectado: CorteRachaRule")


if __name__ == "__main__":
    if "--alternativos" in sys.argv:
        demostrar_flujos_alternativos()
    else:
        main()
