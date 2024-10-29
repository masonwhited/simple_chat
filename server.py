import socket
import threading

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

clients = {} #Key = Connection, Value = Username
clients_lock = threading.Lock()

def broadcast(message, connection):
    with clients_lock:
        user = clients[connection]
        message = bytes(f"{user}: {message}", "UTF-8")
        for client in clients.keys():
            if client != connection:
                client.sendall(message)

def client_connect(connection, address):
    with clients_lock:
        clients[connection] = address
    while True:
        try:
            data = connection.recv(1024)
            data = str(data, "UTF-8")
        
            print(f"Received: {data}")
            request = data.split("|")
            if len(request) == 0:
                response = bytes("MSG_ERR", "UTF-8")
                connection.sendall(response)
            elif request[0] == "USER" and len(request) == 2:
                user = request[1]
                with clients_lock:
                    clients[connection] = user
                response = bytes("USER_OK", "UTF-8")
                connection.sendall(response)
            elif request[0] == "MSG" and len(request) == 2:
                broadcast(request[1], connection)
                response = bytes("MSG_OK", "UTF-8")
                connection.sendall(response)
            elif request[0] == "DIR":
                with clients_lock:
                    users = ", ".join(clients.values())
                response = bytes(f"Users logged in: {users}", "UTF-8")
                connection.sendall(response)
            else:
                response = bytes("MSG_ERR", "UTF-8")
                connection.sendall(response)
        except:
            break

    print(f"Client disconnected: {address}")
    with clients_lock:
        del clients[connection]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(server_address)
    sock.listen()
    print(f"Server started: {server_address}")

    while True:
        connection, address = sock.accept()
        print(f"Client connected: {address}")
        client_thread = threading.Thread(target=client_connect, args=(connection, address))
        client_thread.start()
        