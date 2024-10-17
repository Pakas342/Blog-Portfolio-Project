import os
from flask_migrate import upgrade
from app import create_app

# Set up the database URI
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_name = os.getenv("DB_NAME")
instance_connection_name = os.getenv("INSTANCE_CONNECTION_NAME")

database_uri = f"mysql+pymysql://{db_user}:{db_pass}@/{db_name}?unix_socket=/cloudsql/{instance_connection_name}"

# Create the app with the database URI
app = create_app("Production")
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

# Run the migrations
with app.app_context():
    upgrade()

print("Migrations complete!")
