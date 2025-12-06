import socket

HOST = "127.0.0.1"
PORT = 3030

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Сервер працює постійно на {HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        print(f"[SERVER] Нове підключення від: {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[SERVER] Клієнт відключився")
                    break
                conn.sendall(data)
