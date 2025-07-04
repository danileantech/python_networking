import socket
from threading import Thread # simultaneous listening and sending messages
import os

class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT)) # Tells the socket to listen on the given host and port
        self.socket.listen()
        print("Server waiting for connection...")
        
        pass