import socket

HOST = "192.168.1.98"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)
print(f"Server is running on {HOST}:{PORT}")

while True:
    communcation_sock, addr = server.accept()
    print(f"Connected to {addr}")
    msg = communcation_sock.recv(1024).decode("ascii")
    print(f"Client says: {msg}")
    communcation_sock.send("Got you, thanks".encode('ascii'))
    communcation_sock.close()
    print(f"Connection with {addr} was closed")
