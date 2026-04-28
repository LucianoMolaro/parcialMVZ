from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"  # ignora POSTGRES_USER, POSTGRES_HOST, etc del .env

settings = Settings()
