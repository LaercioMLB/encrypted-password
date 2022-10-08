from cryptography.fernet import Fernet
import base64

def EncriptyPassword(password):
    key = Fernet.generate_key()
    f = Fernet(key)
    conv_bytes = bytes(password, 'utf-8')
    encrypted_data = f.encrypt(conv_bytes).decode()
    return [encrypted_data, key.decode()]

def DescriptyPassword(encrypted_data, key):
    key_base64 = bytes(key, 'utf-8')
    f = Fernet(key_base64)
    conv_bytes = bytes(encrypted_data, 'utf-8')
    return f.decrypt(conv_bytes).decode()