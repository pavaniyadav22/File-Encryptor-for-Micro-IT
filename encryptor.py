import os
from utils import generate_key, encrypt_file, decrypt_file

def main():
    print("\n🔐 File Encryption/Decryption Tool")
    print("1. Encrypt File")
    print("2. Decrypt File")
    choice = input("Choose (1/2): ").strip()

    if choice not in ['1', '2']:
        print("Invalid option.")
        return

    file_path = input("Enter full file path: ").strip().strip('"')

    if not os.path.isfile(file_path):
        print("❌ The path is not a file. Please provide a valid file path.")
        return

    password = input("Enter password: ").strip()

    key = generate_key(password)
    print(f"🔑 Generated key: {key.decode()}")  # Debug: print key

    if choice == '1':
        encrypt_file(file_path, key)
    else:
        decrypt_file(file_path, key)

if __name__ == "__main__":
    main()
