from cryptography.fernet import Fernet


def write_key():
# Создаем ключ и сохраняем его в файл
    key = Fernet.generate_key()
    with open('/home/naruto/jutsu/cryptos/crypto.key', 'wb') as key_file:
        key_file.write(key)

write_key()