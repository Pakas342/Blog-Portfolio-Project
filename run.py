from app import create_app
import os

if os.getenv('ENV') == 'PROD':
    app = create_app("Production")
else:
    app = create_app("LocalDev")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(port=port, host="127.0.0.1")

