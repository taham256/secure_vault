import os
import base64
import hashlib
from cryptography.fernet import fernet, Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class VaultManager:
    def __init__(self,vault_path):
        self.vault_path = vault_path
        self.salt = os.urandom(16)
        self.key = None
        self.hashed_master_password = None

    def set_master_password(self,password):
        self.hashed_master_password = hashlib.sha256(password.encode()).hexdigest()
        self.key = self.derive_key(password)

    def verify_master_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest() == self.hashed_master_password

    def derive_key(self,password):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt= self.salt,
            iterations=100_000,
            backend=default_backend()
        )
        return base64.urlsafe_b64encode(kdf.derive(password.encode()))

    def encrypt(self,data):
        fernet = Fernet(self.key)
        return fernet.encrypt(data.encode())

    def decrypt(self, token):
        fernet = Fernet(self.key)
        return fernet.decrypt(token).decode()

    def load_vault(self):
        if os.path.exists(self.vault_path):
            with open(self.vault_path, "r") as f:
                self.vault_data = json.load(f)

    def save_vault(self):
        with open(self.vault_data, "w") as f:
            json.dump(self.vault_data, f, indent = 2)