import socket

# if __name__=="__main__":
#     host = "127.0.0.1"
#     port = 4455

#     server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#     server.bind((host, port))

#     while True:
#         data, addr = server.recvfrom(1024)
#         data = data.decode('utf-8')

#         print(f"Client: {data}")

#         data = data.upper()
#         data = data.encode('utf-8')
#         server.sendto(data,addr)

HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket()
sock.bind((HOST,PORT))
sock.listen(1)
conn, addr = sock.accept()

print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())

conn.close()
