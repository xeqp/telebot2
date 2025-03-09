from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str
    OPENAI_API_KEY: str
    OPENAI_ASSISTANT_ID: str

    class Config:
        env_file = '.env'

settings = Settings()
