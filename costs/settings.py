from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '0.0.0.0'
    server_port: int = 5555
    database_url: str = 'sqlite:///./database.sqlite3'

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'


settings = Settings()
