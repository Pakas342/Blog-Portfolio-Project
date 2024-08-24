from config import LocalDevelopmentConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize an open instance of SQLAlchemy and Migrate

db = SQLAlchemy()
migrate = Migrate(render_as_batch=True)

VALID_CONFIG_CLASSES = {
    "LocalDev" : LocalDevelopmentConfig
}

def create_app(config_class_name: str) -> Flask:
    if config_class_name not in VALID_CONFIG_CLASSES:
        raise ValueError(f"The config name {config_class_name} isn't part of the valid config classes")
    
    config_class = VALID_CONFIG_CLASSES[config_class_name]
    
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Linking the initialized instance of db and migrate to the app and db context
    db.init_app(app)
    migrate.init_app(app, db)
    
    return app
    