import socket
import threading
import os

server_ip = "127.0.0.1"
server_port = 7000
server_address = (server_ip, server_port)

def reader(sock):
    while True:
        try:
            response = sock.recv(1024)
            response = str(response, "UTF-8")
            print()
            print(response)
            print()
        except:
            print("Client Disconnected")
            os._exit(0)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(server_address)
    print(f"Connected to server: {server_address}")

    thread = threading.Thread(target=reader, args=(sock,))
    thread.start()

    name = input("What is your name?: ")
    name = bytes(f"USER|{name}", "UTF-8")
    sock.sendall(name)

    print("Enter your messages to send (exit to quit):")
    while True:
        message = input()
        if message == "exit":
            break
        if message == "users":
            message = bytes(f"DIR", "UTF-8")
        else:
            message = bytes(f"MSG|{message}", "UTF-8")
        sock.sendall(message)