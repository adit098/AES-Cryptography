import socket
import ast
from Main import decrypt, keyExp, conv_to_hexa

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            ciphertext_list, key = [i for i in data.decode('utf-8').split('\n')]
            ciphertext_list = ast.literal_eval(ciphertext_list)
            key = int(key)        
            print(ciphertext_list, key)
            keyExp(key)                         # Generate keys

            plaintext_list = []
            
            for val in ciphertext_list:
                print("Input Cipher Text:: ", hex(val))
                print("Input Cipher Key:: ", hex(key))
                plaintext_list.append(decrypt(val))
            conn.sendall("message decypted succesfully".encode())
