import socket

HOST = "127.0.0.1"
PORT = 3030

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("[CLIENT] Підключено до сервера")

    while True:
        message = input("Введіть повідомлення (або 'exit'): ")
        if message.lower() == "exit":
            break

        s.sendall(message.encode())
        data = s.recv(1024)
        print("Відповідь сервера:", data.decode())
