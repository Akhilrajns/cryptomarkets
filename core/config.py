import os
from pydantic import BaseSettings
from dotenv import load_dotenv

env_file = os.path.join(os.getcwd(), '.env')
if env_file:
    load_dotenv(env_file)


class Config(BaseSettings):
    ENV: str = os.getenv("ENV", "development")
    APP_HOST: str = str(os.getenv('APP_HOST'))
    APP_PORT: int = int(os.getenv('APP_PORT'))
    API_KEY: str = str(os.getenv('API_KEY'))
    SECRET_KEY: str = str(os.getenv('SECRET_KEY'))


class DevelopmentConfig(Config):
    DEBUG: str = True


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = os.getenv("ENV", "development")
    config_type = {
        "development": DevelopmentConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


config = get_config()
