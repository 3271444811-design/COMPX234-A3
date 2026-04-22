import socket
import sys

def recv_all(conn, n):
    
    data = b''
    while len(data) < n:
        chunk = conn.recv(n - len(data))
        if not chunk:
            return None
        data += chunk
    return data

def main():
    port = int(sys.argv[1])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', port))
    s.listen(10)
    print(f"Server on port {port}")
    
    
