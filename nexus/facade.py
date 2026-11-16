class CasinoScraperFacade:
    """Patrón Facade: Encapsula la complejidad de Playwright y gestión de sesión."""

    def __init__(self, frecuencia_seg: int = 30) -> None:
        if frecuencia_seg < 30:
            raise ValueError("El intervalo mínimo permitido es 30 segundos (HU-02)")
        self.frecuencia_seg: int = frecuencia_seg
        self.url_actual: str | None = None
        self.conectado: bool = False
        self.rondas_capturadas: int = 0

    def conectar_mesa(self, url: str, simular_timeout: bool = False) -> bool:
        if not url or not url.startswith(("http://", "https://")):
            raise ValueError(f"Formato de URL inválido: {url}")

        print(f"[CasinoScraperFacade Mock] Conectando a la mesa: {url}")
        if simular_timeout:
            self.conectado = False
            self.registrar_error(f"TimeoutException al conectar con {url}")
            raise TimeoutError(f"Tiempo de espera agotado al conectar a {url}")

        self.url_actual = url
        self.conectado = True
        return self.conectado

    def registrar_error(self, detalle: str) -> None:
        print(f"[CasinoScraperFacade Log] Error registrado: {detalle}")

    def capturar_ronda_simulada(self) -> list[str]:
        if not self.conectado:
            raise RuntimeError("No hay sesión activa con la mesa de casino")
        print("[CasinoScraperFacade Mock] Capturando ronda simulada")
        self.rondas_capturadas += 1
        return ["Rojo", "Rojo", "Rojo"]
