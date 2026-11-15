from .interfaces import IAlertaRepository, IObserver


class TelegramObserver(IObserver):
    def update(self, alerta: str) -> None:
        print(f"[Telegram Mock] Enviando alerta: {alerta}")


class DatabaseObserver(IObserver):
    def __init__(self, repository: IAlertaRepository) -> None:
        self.repository = repository

    def update(self, alerta: str) -> None:
        print(f"[DatabaseObserver] Guardando alerta: {alerta}")
        self.repository.save(alerta)


class MockPostgresRepo(IAlertaRepository):
    def save(self, alerta: str) -> None:
        print(f"[PostgreSQL Mock] Alerta guardada: {alerta}")
