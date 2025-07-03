import socket
import pickle

SOCKET_PATH = "/tmp/matiz_df_socket"

# Connect and receive
with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client_sock:
    client_sock.connect(SOCKET_PATH)
    data = b""
    while True:
        chunk = client_sock.recv(1024)
        if not chunk:
            break
        data += chunk

# Deserialize
df_received = pickle.loads(data)

print("📦 Received DataFrame:")
print(df_received)
