import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect(("127.0.0.1", 8080))
mySocket.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n")

while True:
	data = mySocket.recv(1024)
	if not data:
		break
	print(data.decode(), end="")