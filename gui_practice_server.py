import socket
import threading

# Server setup
HOST = '127.0.0.1'  # Localhost for testing
PORT = 7000         # Port to listen on

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Broadcast message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle each client
def handle_client(client):
    while True:
        try:
            # Receive and broadcast message
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remove client on disconnect
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat.".encode('utf-8'))
            nicknames.remove(nickname)
            break

# Accept new clients
def receive_clients():
    while True:
        client, address = server.accept()
        print(f"Connected with {address}")

        # Request and store nickname
        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        # Notify all clients
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server.".encode('utf-8'))

        # Start handling client messages
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running...")
receive_clients()
