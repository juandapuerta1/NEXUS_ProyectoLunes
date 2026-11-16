from .interfaces import IAlertaRepository, IObserver


class TelegramObserver(IObserver):
    """Suscriptor encargado de despachar alertas inmediatas a Telegram Bot API."""

    def __init__(self, max_retries: int = 3) -> None:
        self.max_retries: int = max_retries
        self.estado_ultima_senal: str = "PENDIENTE"

    def formatear_mensaje(self, alerta: str) -> str:
        if not alerta or not alerta.strip():
            raise ValueError("La alerta no puede estar vacía")
        return alerta.strip()

    def update(self, alerta: str, simular_fallo_red: bool = False) -> None:
        mensaje = self.formatear_mensaje(alerta)
        if simular_fallo_red:
            for intento in range(1, self.max_retries + 1):
                print(f"[Telegram Retry] Intento {intento}/{self.max_retries} por HTTPException...")
            self.estado_ultima_senal = "ERROR"
            print("[Telegram Error] Máximo de reintentos alcanzado. Estado de señal: ERROR")
            return

        print(f"[Telegram Mock] Enviando alerta: {mensaje}")
        self.estado_ultima_senal = "ENVIADA"


class DatabaseObserver(IObserver):
    def __init__(self, repository: IAlertaRepository) -> None:
        self.repository = repository

    def update(self, alerta: str) -> None:
        print(f"[DatabaseObserver] Guardando alerta: {alerta}")
        self.repository.save(alerta)


class MockPostgresRepo(IAlertaRepository):
    def save(self, alerta: str) -> None:
        print(f"[PostgreSQL Mock] Alerta guardada: {alerta}")
