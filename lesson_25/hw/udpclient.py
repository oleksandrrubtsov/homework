import socket

HOST  = '127.0.0.1'  # Standard loopback interface address (
PORT = 65432

client_socket= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = "Hello UDP Server"
client_socket.sendto(msg.encode('utf-8'),(HOST,PORT))
data,addr = client_socket.recvfrom(1024)
print("Server Says")
print(str(data))
client_socket.close()