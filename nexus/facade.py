class CasinoScraperFacade:
    def conectar_mesa(self, url: str) -> None:
        print(f"[CasinoScraperFacade Mock] Conectando a la mesa: {url}")

    def capturar_ronda_simulada(self) -> list[str]:
        print("[CasinoScraperFacade Mock] Capturando ronda simulada")
        return ["Rojo", "Rojo", "Rojo"]
