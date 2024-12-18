import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DATABASE_URL = os.getenv('DATABASE_URL_DEV', 'postgresql://...')

class ProductionConfig(BaseConfig):
    DATABASE_URL = os.getenv('DATABASE_URL_PROD', 'postgresql://...')

class DevelopmentConfig(BaseConfig):
    DEBUG = True

def get_config():
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'production':
        return ProductionConfig()
    return DevelopmentConfig()
