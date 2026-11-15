import time
import logging
from config.settings import settings
from db.connection import DatabaseConnection

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def iniciar_nexus():
    logging.info(f"Iniciando {settings.PROJECT_NAME} v{settings.VERSION}")
    
    # Inicializar Base de Datos
    db = DatabaseConnection()
    try:
        db.connect()
        logging.info("Conexión a BD establecida exitosamente.")
        
        # Simulación de flujo de guardado
        mock_data = {"casino": "BacBo", "cuota": 1.95, "estado": "activo"}
        db.save_data("historico_cuotas", mock_data)
        
    except Exception as e:
        logging.error(f"Error crítico en la inicialización: {e}")

if __name__ == "__main__":
    iniciar_nexus()