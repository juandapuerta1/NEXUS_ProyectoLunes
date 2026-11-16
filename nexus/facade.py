class CasinoScraperFacade:
    """Patrón Facade: Encapsula la complejidad de Playwright, keep-alive y reconexión."""

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

    def reconectar_mesa(self, url: str, max_reintentos: int = 3) -> bool:
        for intento in range(1, max_reintentos + 1):
            print(f"[CasinoScraperFacade] Reintento {intento}/{max_reintentos} hacia {url}...")
            try:
                return self.conectar_mesa(url, simular_timeout=False)
            except TimeoutError as exc:
                self.registrar_error(str(exc))
        return False

    def ejecutar_keep_alive(self, inactividad_detectada: bool = False) -> bool:
        if inactividad_detectada:
            print("[CasinoScraperFacade Keep-Alive] Clic de refresco en grid secundario (RNF-02)")
            return True
        return False

    def registrar_error(self, detalle: str) -> None:
        print(f"[CasinoScraperFacade Log] Error registrado: {detalle}")

    def capturar_ronda_simulada(self, inactividad_detectada: bool = False) -> list[str]:
        if not self.conectado:
            raise RuntimeError("No hay sesión activa con la mesa de casino")
        self.ejecutar_keep_alive(inactividad_detectada=inactividad_detectada)
        print("[CasinoScraperFacade Mock] Capturando ronda simulada")
        self.rondas_capturadas += 1
        return ["Rojo", "Rojo", "Rojo"]
