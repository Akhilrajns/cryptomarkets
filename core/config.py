import os
from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000


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
