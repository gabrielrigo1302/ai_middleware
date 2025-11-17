from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    PORT: int = 8000
    ENVIRONMENT: str = "development"
    MISTRAL_KEY: str = "nHhCZUlfKPIHWYG6xX0Raulu2OeYITjk"
    DEBUG: bool = False
    NEO4J_URI: str
    NEO4J_USER: str
    NEO4J_PASSWORD: str


settings = Settings()  # type: ignore
