import time
import logging
from config.settings import settings

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def iniciar_nexus():
    logging.info(f"Iniciando {settings.PROJECT_NAME} v{settings.VERSION}")
    logging.info("Cargando módulos base...")
    time.sleep(1)
    logging.info("Sistema listo para recibir órdenes de extracción.")

if __name__ == "__main__":
    iniciar_nexus()