import socket
import threading

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

def client_connect(connection, address):
    while True:
        data = connection.recv(1024)
        if len(data) == 0:
             break
        print(f"Received: {data}")

        connection.sendall(data)
        print(f"Client disconnected: {address}")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(server_address)
    sock.listen()
    print(f"Server started: {server_address}")

    while True:
        connection, address = sock.accept()
        print(f"Client connected: {address}")
        client_thread = threading.Thread(target=client_connect, args=(connection, address))
        client_thread.start()
        