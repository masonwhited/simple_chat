## Overview

**Project Title**: Simple Chat

**Project Description**: A simple chat program that uses host and user servers to communicate with each other

**Project Goals**: Allow multiple users to link to a single server and send messages to each other via the server.

## Instructions for Build and Use

Steps to build and/or run the software:

1. set up the server program by importing socket and threading.
2. hard code the server ip and port into global variables and combine them into the server address global variable.
3. Set up a dictionary of clients and create a client_lock to prevent simultaneous access to the dictionary.
4. Create a function to handle new connections and a function to handle messages from clients.
5. Create a function to broadcast messages to all clients.
6. Create a function to handle disconnections from clients.
7. Create the client program by importing socket, threading, and os.
8. Hard code the client ip and port into global variables and combine them into the client address global variable.
9. Create a function to handle messages from the server and a function to send messages to the server
10. Create a function to handle disconnections from the server.

Instructions for using the software:

1. Launch the server program
2. In two seperate terminals launch the client program
3. Input your username into both client terminals (preferably different names)
4. Type messages into the client terminals to send to the other user
5. Type 'users' to see a list of all usernames connected to the server.
6. Type 'exit' to disconnect from the server.
7. trashcan the terminals to exit the server program.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* VSCode

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Networking Workshop](https://video.byui.edu/media/t/1_4o1tpofn)
* [ChatGPT](chatgpt.com)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Find a way to make it work across different wifi networks
* [ ] Create a GUI for better visual presentation
