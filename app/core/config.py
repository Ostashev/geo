from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = ''
    api_root_path: str = ''


    class Config:
        env_file = '.env'


settings = Settings()
