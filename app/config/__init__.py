from pydantic import BaseSettings

class CommonSettings(BaseSettings):
    APP_NAME: str = "FastAPI GraphQL Starter"
    DEBUG_MODE: bool = False

class ServerSettings(BaseSettings):
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    WEBHOOKS_PORT: int = 8001


class DatabaseSettings(BaseSettings):
    DB_URL: str = ''
    DB_NAME: str = ''

class Settings(CommonSettings, ServerSettings, DatabaseSettings):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()