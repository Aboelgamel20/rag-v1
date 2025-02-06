from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_KEY: str

    FILE_ALLOWED_EXTENTION:list
    FILE_ALLOWED_SIZE:int

    class Config:
        env_file=".env"

def get_settings():
    return Settings()