import socket

HOST = "192.168.1.98"  # Server IP Adress
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))

socket.send(input("MSG: ").encode("ascii"))
print(socket.recv(1024).decode("ascii"))
