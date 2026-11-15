import os

class Settings:
    PROJECT_NAME = "Nexus Casino Scraper"
    VERSION = "1.0.0"
    
    # Mocks de variables de entorno para PostgreSQL y Telegram
    DB_USER = os.getenv("DB_USER", "nexus_admin")
    DB_PASS = os.getenv("DB_PASS", "dummy_password")
    DB_HOST = os.getenv("DB_HOST", "ep-cool-pine-12345.us-east-2.aws.neon.tech")
    
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "mock_token_123")

settings = Settings()