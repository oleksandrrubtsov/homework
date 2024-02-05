import socket


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)



def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = (ord(char) + key - ord('A')) % 26 + ord('A') if char.isupper() else (ord(char) + key - ord('a')) % 26 + ord('a')
            encrypted_message += chr(shift)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, key):
    return encrypt(encrypted_message, -key)


def caesar_cipher_echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Accepted connection from {client_address}")

            with client_socket:
                data = client_socket.recv(1024).decode('utf-8')
                key = int(data)  # Assuming the first data received is the encryption key

                client_socket.sendall("Key received. Please send the message to encrypt:".encode('utf-8'))

                data = client_socket.recv(1024).decode('utf-8')
                encrypted_data = encrypt(data, key)

                client_socket.sendall(f"Encrypted message: {encrypted_data}".encode('utf-8'))

                print(f"Sent encrypted message to {client_address}")

if __name__ == "__main__":
    HOST = '127.0.0.1'
    PORT = 65432
    caesar_cipher_echo_server(HOST, PORT)

