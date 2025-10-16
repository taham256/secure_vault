# Secure Vault System
This is a simple secure vault system implemented in python.it keep your importent passwords,login keys,files safe in your local system.
## **Features**
- **Master Password Protection**:Set one master password to access your entire vault.
- **Strong Encrytion**:Uses Fernet encryption(AES 128-bit) to protect your data.
- **Password Hashing**:Master password hashed with SHA-256 for security.
- **Key Derivation**:Uses PBKDF2 WITH 100,000 iterations to generate encrytion key.
- **Password Storage**: Organize passwords with names and usernames
- **File Encryption**:Encrypt and store any file securely
- **JSON Storage**:Stores encrypted data in an easy-to-backup JSON file
## **Requirements**
- Python 3.x
- for pip:
  ```bash
     pip install cryptography
- for conda:
  ```bash
     conda install cryptography
- Standard libraries used: os, hashlib, json, base64
## **Installation**
   1.**Clone the repository**:
     ```bash
        git clone https://github.com/taham256/secure_vault.git
        cd secure_vault
## **How to Use**
```bash
       # Create and setup vault
   vault = VaultManager("passwords.json")
   vault.set_master_password("MyMasterPass123!")

   # --- Store passwords ---
   # Create a password entry
   email_pass = PasswordEntry(
      name="Work Email",
      username="john@company.com",
      password="WorkPass456!"
   )

   # Encrypt and store
   encrypted = vault.encrypt(email_pass.password)
   print(f"Encrypted: {encrypted}")

   # Retrieve the password
   decrypted = vault.decrypt(encrypted)
   print(f"Decrypted: {decrypted}")

   # --- Encrypt files ---
   # Read a secret file
   with open("confidential.txt", "rb") as f:
       file_content = f.read()

   # Encrypt and save the file
   encrypted_file_data = vault.encrypt(file_content.decode())
   file_entry = FileEntry("confidential", encrypted_file_data)
   file_entry.save("vault_files")

   # The file is now saved as: vault_files/confidential.enc

   # --- Verify master password ---
   if vault.verify_master_password("MyMasterPass123!"):
      print("Correct password!")



    
