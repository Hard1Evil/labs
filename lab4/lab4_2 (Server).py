import socket

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    print("Echo server is running...")

    while True:
        conn, addr = s.accept()
        print("Connected by", addr)

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

        print("Connection closed:", addr)
