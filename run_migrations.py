import os
from flask_migrate import upgrade
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from app import create_app


def recreate_db(app):
    db = SQLAlchemy(app)
    with app.app_context():
        db.drop_all()
        db.create_all()
    print("Database schema recreated.")


def run_migrations():
    app = create_app("Production")

    try:
        with app.app_context():
            upgrade()
        print("Migrations completed successfully!")
    except OperationalError as e:
        if "1071" in str(e):  # MySQL error code for key too long
            print("Error: Key too long. Attempting to recreate the database schema...")
            recreate_db(app)
            # Try migrations again after recreating the schema
            with app.app_context():
                upgrade()
            print("Migrations completed after schema recreation!")
        else:
            print(f"An error occurred during migration: {e}")
            raise


run_migrations()
