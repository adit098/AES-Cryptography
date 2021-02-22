import socket
import ast
from Main import encrypt, keyExp, conv_to_hexa

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

Message = input("Input Plaintext: ")
key = input("Input Key: ")

key = int(key, 2)               # converted binart key value to int key value
if len(Message)%2 != 0:         # make even length message
    Message+="z"

keyExp(key)                     # Generate keys

plaintext_list = []
ciphertext_list = []
ciphertext_list_hex = []
for i in range(0, len(Message), 2):
    plaintext_list.append(Message[i] + Message[i+1])
    k = 256*ord(Message[i]) + ord(Message[i+1])
    res = encrypt(k)
    ciphertext_list.append(res)
    ciphertext_list_hex.append(conv_to_hexa(res))

print("Final Ciphertext: ", "".join(x[2:] for x in ciphertext_list_hex))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(str.encode("\n".join([str(ciphertext_list), str(key)])))          # send ciphertext and key to server
    data = s.recv(1024)


print('Received', repr(data))