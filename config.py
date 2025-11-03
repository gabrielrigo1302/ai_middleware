from pydantic import BaseSettings

class Settings(BaseSettings):
    ENV: str = "development"
    PORT: int = 8000
    RATE_LIMIT_PER_MINUTE: int = 120
    SQL_DATABASE_URL: str = "sqlite:///./test.db"
    OPENAI_API_KEY: str = "your-openai-api-key"

    class Config:
        env_file = ".env" 

settings = Settings()  