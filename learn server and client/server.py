import socket

def creat_server():
	serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	try:
		serverSocket.bind(("localhost", 8080))
		serverSocket.listen(10)
		print("Server Listening on port 8080")
		t = 1
		while True:
			clientSocket, addr = serverSocket.accept()
			print(f"Connection from {addr} has been established.")

			rd = clientSocket.recv(1024).decode()
			rd = rd.split("\r\n")
			text = ""
			text += "HTTP/1.1 200 OK\r\n"
			text += "Content-Type: text/html\r\n"
			text += "Connection: close\r\n"
			text += "\r\n"
			
			text += "<html>"
			text += "<head>"
			text += "<title>My First HTML Page</title>"
			text += "</head>"
			text += "<body>"
			text += f"<h1>Hello, this {t} time be seen</h1>"
			text += "\r\n"
			text += f"<p>{rd}</p>"

			text += "</body> </html>"
			t += 1
			clientSocket.sendall(text.encode())
			clientSocket.shutdown(socket.SHUT_WR)

	except KeyboardInterrupt:
		print("Server shutting down.")
		serverSocket.close()
		exit(0)
	except Exception as e:
		print(f"An error occurred: {e}")
		serverSocket.close()
		exit(1)

	serverSocket.close()


if __name__ == "__main__":
	print("OK")
	print(creat_server())
