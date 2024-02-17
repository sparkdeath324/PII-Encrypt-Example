from cryptography.fernet import Fernet


def get_key():
    with open('secret.key', 'rb') as key_file:
        key = key_file.read()
    return key

def encryptdata(text):
    key = Fernet(get_key())
    encrypted_pii = key.encrypt(text.encode('utf-8'))
    return encrypted_pii

def decryptdata(text):
    key = Fernet(get_key())
    decrypted_pii = key.decrypt(text).decode('utf-8')
    return decrypted_pii