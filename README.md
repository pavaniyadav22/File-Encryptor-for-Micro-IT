
# 🔐 File Encryption/Decryption Tool

A secure Python-based tool that encrypts and decrypts files using password-protected AES encryption. It ensures the confidentiality of sensitive information, providing a simple CLI for secure file management.

---

## 📌 Features

- 🔐 Encrypt files using a password  
- 🔓 Decrypt files with the correct password  
- 🛡️ AES-based secure encryption using Fernet (cryptography library)  
- 📁 Stores encrypted and decrypted files in dedicated folders  
- ✅ Simple, clean command-line interface  

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x  
- cryptography library  
  ```bash
  pip install cryptography
  ```

### 📥 Installation

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/your-username/file-encryptor.git
   cd file-encryptor
   ```

2. **Install dependencies**:  
   ```bash
   pip install cryptography
   ```

3. **Run the tool**:  
   ```bash
   python encryptor.py
   ```

---

## 🗂️ Project Structure

```
file_encryptor/
├── encryptor.py           # Main script to run the CLI
├── utils.py               # Helper functions (key generation, encryption, decryption)
├── encrypted_files/       # Encrypted output files
├── decrypted_files/       # Decrypted files (outputs)
└── README.md              # Project documentation
```

---

## 🔐 How It Works

1. Enter the full path of the file you want to encrypt/decrypt.  
2. Input a password — this is used to generate a secure key.  
3. The file is encrypted and saved in the `encrypted_files/` directory.  
4. The same password is required to decrypt and restore the original file.  

---

## ⚠️ Note

- Always remember the password used during encryption; without it, the file cannot be decrypted.  
- Only `.enc` files are accepted for decryption.  

---

## 👨‍💻 Author

**Guggulla Pavani**  
📧 guggullapavani@gmail.com  
📍 India
