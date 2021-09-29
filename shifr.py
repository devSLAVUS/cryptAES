from cryptography.fernet import Fernet
import sys

while True:
    print("1. incrypt")
    print("2. decrypt")
    print("0. exit")
    choose_number = input("choose one: ")
    def choose_test():
        if choose_number == "1":
            print("specify the path file to incrypt") 
            file_path_in = input("path:")
            key = load_key()
            encrypt(file_path_in, key)
            print("===Done!===")

                   
        elif  choose_number == "2":
            print("specify the path  file to decrypt")
            file_path_de = input("path:")
            key = load_key()
            decrypt(file_path_de, key)
            print("===Done!===")
        elif choose_number == "0":
            sys.exit()
        else:
            print("===ERROR TRY(0,1,2)===")

    def load_key():
    # Загружаем ключ 'crypto.key' из текущего каталога
        return open('crypto.key', 'rb').read()
    def encrypt(filename, key):
    # Зашифруем файл и записываем его
        f = Fernet(key)
        with open(filename, 'rb') as file:
            # прочитать все данные файла
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        with open(filename, 'wb') as file:
            file.write(encrypted_data)
    def decrypt(filename, key):
    # Расшифруем файл и записываем его
        f = Fernet(key)
        with open(filename, 'rb') as file:
            # читать зашифрованные данные
            encrypted_data = file.read()
        # расшифровать данные
        decrypted_data = f.decrypt(encrypted_data)
        # записать оригинальный файл
        with open(filename, 'wb') as file:
            file.write(decrypted_data)

    choose_test()

