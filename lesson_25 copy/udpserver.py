import socket

HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST,PORT))



while True:
    data,addr = sock.recvfrom(1024)
    print(str(data))
    message =  "Hello, I am a UDP server".encode('utf-8')
    sock.sendto(message, addr)