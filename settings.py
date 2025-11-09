from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    PORT: int = 8000
    ENVIRONMENT: str = "development"
    MISTRAL_KEY: str
    DEBUG: bool = False

settings = Settings()