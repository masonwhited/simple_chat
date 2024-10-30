import tkinter as tk
from tkinter import scrolledtext
import socket
import threading

HOST = '127.0.0.1'  # Server IP (localhost for testing)
PORT = 7000         # Server port


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# GUI class for chat client
class ChatGUI:
    def __init__(self):
        # Set up the main window
        self.root = tk.Tk()
        self.root.title("Chat Room")
        self.root.geometry("400x500")

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(self.root)
        self.chat_area.pack(pady=10, padx=10)
        self.chat_area.config(state="disabled")  # Read-only

        # Entry box for typing messages
        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(pady=10)
        self.message_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        # Thread to receive messages
        threading.Thread(target=self.receive_messages, daemon=True).start()

    # Method to send messages
    def send_message(self, event=None):
        message = self.message_entry.get()
        if message:
            client.send(message.encode('utf-8'))
            self.message_entry.delete(0, tk.END)  # Clear entry box

    # Method to receive messages
    def receive_messages(self):
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                self.display_message(message)
            except:
                print("Error receiving message")
                client.close()
                break

    # Method to display messages in chat area
    def display_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.config(state="disabled")
        self.chat_area.yview(tk.END)  # Auto-scroll to the latest message

    # Run the GUI loop
    def run(self):
        self.root.mainloop()

# Prompt for nickname
nickname = input("Enter your nickname: ")
client.send(nickname.encode('utf-8'))

# Start chat client GUI
chat_gui = ChatGUI()
chat_gui.run()