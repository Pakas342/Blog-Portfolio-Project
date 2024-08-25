from config import LocalDevelopmentConfig
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# TODO configure the already installed flask-jwt-extended for managing user authentication

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

    # Calling the models because those are not getting initialized correctly
    from app import models
    # Linking the instance of the app context 
    db.init_app(app)
    # Linking migrate to the app and db context
    migrate.init_app(app, db)

    # Linking a bp to the app
    from app.main_blueprint import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Code for printing the current routes
    # print("Registered routes:")
    # for rule in app.url_map.iter_rules():
    #     print(f"{rule.endpoint}: {rule.rule}")

    return app
