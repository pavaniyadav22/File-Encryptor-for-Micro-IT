import os
from cryptography.fernet import Fernet
import hashlib
import base64

def generate_key(password: str) -> bytes:
    # Derive a URL-safe base64 key from the password using SHA-256
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def encrypt_file(file_path: str, key: bytes):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        data = file.read()

    encrypted = fernet.encrypt(data)
    output_path = f'encrypted_files/{os.path.basename(file_path)}.enc'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'wb') as file:
        file.write(encrypted)

    print(f"✅ Encrypted file saved as: {output_path}")

def decrypt_file(file_path: str, key: bytes):
    fernet = Fernet(key)
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
        print(f"🔍 Encrypted data size: {len(data)} bytes")  # Debug info
        decrypted = fernet.decrypt(data)
        output_path = f'decrypted_files/{os.path.basename(file_path).replace(".enc", "")}'
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'wb') as file:
            file.write(decrypted)
        print(f"✅ Decrypted file saved as: {output_path}")
    except Exception as e:
        print(f"❌ Decryption failed: {e}")
