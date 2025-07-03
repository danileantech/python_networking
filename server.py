import pickle
import socket
import os
import pandas as pd

SOCKET_PATH = "/tmp/socket"

if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

df = pd.DataFrame({'name': ['John', 'Jane', 'Jim', 'Jill'], 'age': [25, 30, 35, 40]})

data_bytes = pickle.dumps(df) # serialize data (encode)

# Create a socket obj and bind it
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
    s.bind(SOCKET_PATH)

    # Listen for connections
    s.listen(1)
    print("Waiting for connection...")

    # Accept a connection
    conn, addr = s.accept()
    with conn:
        conn.sendall(data_bytes)