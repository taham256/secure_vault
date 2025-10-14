import os

class FileEntry:
    def __init__(self,filename,encrypted_data):
        self.filename = filename
        self.encrypted_data = encrypted_data

    def save(self, vault_dir):
        path = os.path.join(vault_dir,self.filename + "enc")
        with open(path,"wb") as f:
            f.write((self.encrypted_data))