from urllib import request

response = request.urlopen("http://127.0.0.1:8080")

for line in response.readlines():
	print(line.decode().strip())