from cryptography.fernet import Fernet
import logging

def load_encryption_key(key_file):
    """Loads the encryption key from the specified file."""
    with open(key_file, 'rb') as file:
        return file.read()

def encrypt_file(file_path, key_file):
    """Encrypts the given file using the provided encryption key."""
    key = load_encryption_key(key_file)
    fernet = Fernet(key)

    with open(file_path, 'rb') as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)
    encrypted_file_path = f"{file_path}.enc"

    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    logging.info(f"File encrypted: {encrypted_file_path}")
    return encrypted_file_path

def decrypt_file(encrypted_file_path, key_file):
    """Decrypts the given file using the provided encryption key."""
    key = load_encryption_key(key_file)
    fernet = Fernet(key)

    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    decrypted_file_path = encrypted_file_path.replace(".enc", "")
    
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    logging.info(f"File decrypted: {decrypted_file_path}")
    return decrypted_file_path
