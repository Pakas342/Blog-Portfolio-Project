from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    TESTING = True
    DEBUG = True


class LocalDevelopmentConfig(Config):
    SECRET_KEY = os.getenv("LOCAL_DEV_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("LOCAL_DEV_DB_URI")
