import socket

HOST = '127.0.0.1'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    message = "Hello, Echo Server!"
    client_socket.sendall(message.encode('utf-8'))
    data = client_socket.recv(1024)

print("Відправлено:", message)
print("Отримано:", data.decode('utf-8'))
