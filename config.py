from dotenv import load_dotenv
import os

if os.getenv('ENV') == 'DEV':
    load_dotenv()


class Config:
    TESTING = True
    DEBUG = True
    JWT_SECRET_KEY = os.getenv("JWT_DEV_SECRET")
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_COOKIE_SAMESITE = 'Lax'


class LocalDevelopmentConfig(Config):
    SECRET_KEY = os.getenv("LOCAL_DEV_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("LOCAL_DEV_DB_URI")


class ProductionConfig(Config):
    SECRET_KEY = os.getenv("LOCAL_DEV_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("LOCAL_DEV_DB_URI")