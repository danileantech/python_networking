import socket

HOST = '127.0.0.1'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT)) # Tells the socket to listen on the given host and port
server_socket.listen(5)

print(f"Server is listening on {HOST}:{PORT}")

