from dotenv import load_dotenv
import os

if os.getenv('ENV') == 'DEV':
    load_dotenv()


class Config:
    TESTING = True
    DEBUG = True
    JWT_TOKEN_LOCATION = ['cookies']
    JWT_COOKIE_SECURE = True
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_COOKIE_SAMESITE = 'Lax'


class LocalDevelopmentConfig(Config):
    SECRET_KEY = os.getenv("LOCAL_DEV_SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("LOCAL_DEV_DB_URI")
    JWT_SECRET_KEY = os.getenv("JWT_DEV_SECRET")


class ProductionConfig(Config):
    SECRET_KEY = os.getenv("PROD_SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("PROD_JWT_SECRET")

    # Construct the database URL for Google Cloud SQL
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")
    db_name = os.getenv("DB_NAME")
    instance_connection_name = os.getenv("INSTANCE_CONNECTION_NAME")

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{db_user}:{db_pass}@/{db_name}?unix_socket=/cloudsql/{instance_connection_name}"
