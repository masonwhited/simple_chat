import socket

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(server_address)
    print(f"Connected to server: {server_address}")
    while True:
        message = input("Enter your message to send (exit to quit): ")
        if message == "exit":
            break
        
        message = bytes(message, "UTF-8")
        sock.sendall(message)

        response = sock.recv(1024)
        response = str(response, "UTF-8")
        print(response)

print("Client closed")