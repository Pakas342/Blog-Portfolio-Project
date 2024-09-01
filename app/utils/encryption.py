from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet

load_dotenv()

encryption_key = os.getenv("FERNET_KEY")
fernet = Fernet(encryption_key)


class Encryption:

    @staticmethod
    def encrypt(data: str) -> str:
        return fernet.encrypt(data.encode()).decode()

    @staticmethod
    def decrypt(token: str) -> str:
        return fernet.decrypt(token.encode()).decode()
