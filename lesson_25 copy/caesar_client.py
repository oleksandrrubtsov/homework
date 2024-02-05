import socket

HOST = '127.0.0.1'  
PORT = 65432       


import socket

def caesar_cipher_echo_client(host, port, key, message):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        client_socket.sendall(str(key).encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

        client_socket.sendall(message.encode('utf-8'))
        encrypted_response = client_socket.recv(1024).decode('utf-8')
        print(f"Received encrypted message: {encrypted_response}")

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    KEY = 3
    MESSAGE = "Hello, world!"

    caesar_cipher_echo_client(HOST, PORT, KEY, MESSAGE)
