import socket

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(server_address)
    sock.listen()
    print(f"Server started: {server_address}")

    while True:
        connection, address = sock.accept()
        print(f"Client connected: {address}")

        data = connection.recv(1024)
        print(f"Received: {data}")

        connection.sendall(data)

