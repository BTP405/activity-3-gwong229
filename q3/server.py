import socket
import threading
import pickleUtilities
import signal
import sys

clients = []
lock = threading.Lock()

def handleClient(clientSocket):
    while True:
        try:
            data = clientSocket.recv(1024)
            if not data:
                break
            message = pickleUtilities.unPickler(data)
            print(message)
            with lock:
                for c in clients:
                    c.send(pickleUtilities.pickler(message))
        except Exception as e:
            print(f"Error: {e}")
            break
    with lock:
        clients.remove(clientSocket)
        clientSocket.close()

def signal_handler(sig, frame):
    print("Shutting down the server...")
    with lock:
        for client_socket in clients:
            client_socket.close()
    sys.exit(0)

def startServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 5555))
    server.listen(5)

    print("Server listening on port 5555...")

    while True:
        clientSocket, addr = server.accept()
        with lock:
            clients.append(clientSocket)
        
        client_handler = threading.Thread(target=handleClient, args=(clientSocket,))
        client_handler.start()

if __name__ == "__main__":
    startServer()