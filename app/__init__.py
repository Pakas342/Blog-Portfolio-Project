from config import LocalDevelopmentConfig, ProductionConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .cors_config import dev_cors_resources, prod_cors_resources
from flask_cors import CORS

# Initialize an open instance of SQLAlchemy, Migrate, JWTManager, and the IP limiter
db = SQLAlchemy()
migrate = Migrate(render_as_batch=True)
jwt = JWTManager()
cors = CORS()
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per day", "20 per hour"]  # Define default limits here
)

VALID_CONFIG_CLASSES = {
    "LocalDev": LocalDevelopmentConfig,
    "Production": ProductionConfig
}


def create_app(config_class_name: str) -> Flask:
    if config_class_name not in VALID_CONFIG_CLASSES:
        raise ValueError(f"The config name {config_class_name} isn't part of the valid config classes")

    config_class = VALID_CONFIG_CLASSES[config_class_name]

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Calling the models because those are not getting initialized correctly
    from app import models

    # linking open instances to app context
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    limiter.init_app(app)

    # Connecting CORS
    cors_resources = dev_cors_resources if config_class_name == "LocalDev" else prod_cors_resources
    cors.init_app(app=app, resources=cors_resources)

    # Linking all the created blueprints
    from app.routes import add_blueprints
    add_blueprints(app)

    return app
