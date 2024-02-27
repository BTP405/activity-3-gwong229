import socket
import threading
import sys
sys.path.append('..')
import pickleUtilities

def exampleTask1(x, y):
        return x + y
def exampleTask2(x, y):
        return x - y

def handleClient(clientSocket):
    """code to receive the task and arguments from the client, and unpickle, and then return result"""
    data = clientSocket.recv(4096)
    while data:
        try:
            task = pickleUtilities.unPickler(data)
            result = task['function'](*task['args'])
            clientSocket.send(pickleUtilities.pickler(result))
        except Exception as e:
            print(f"Error processing task: {str(e)}")
            clientSocket.send(pickleUtilities.pickler(None))
        data = clientSocket.recv(4096)
    clientSocket.close()

def startWorker(port):
    "main code which sets up the socket, and then executes the handleclient"
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(5)
    print(f"Worker node listening on port {port}")
    while True:
        client, addr = server.accept()
        print(f"Accepted connection from {addr}")
        clientHandler = threading.Thread(target=handleClient, args=(client,))
        clientHandler.start()

if __name__ == "__main__":
    startWorker(5000)