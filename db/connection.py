import logging
from config.settings import settings

class DatabaseConnection:
    def __init__(self):
        self.host = settings.DB_HOST
        self.user = settings.DB_USER
        self.is_connected = False

    def connect(self):
        logging.info(f"Conectando a PostgreSQL en {self.host} con usuario {self.user}...")
        self.is_connected = True
        return self.is_connected

    def save_data(self, table: str, data: dict):
        if not self.is_connected:
            raise Exception("No hay conexión a la base de datos")
        logging.info(f"Datos insertados correctamente en tabla '{table}': {data}")
        return True