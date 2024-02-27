import socket
import os
import sys
sys.path.append('..')
import pickleUtilities

def saveFile(contents, fileName):
    """creates and writes to a file, the contents given in the parameter"""
    fileDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(fileDir, fileName)
    with open(filePath, 'wb') as file:
        file.write(contents)

def runServer():
    """the main function which, sets up the server side socket, then has a loop which accepts a connection from the client
    and uses the pickleUtilities file to unpickle the contents received"""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print("Server is listening")

    while True:
        client_socket, client_address = server_socket.accept()
        try:
            print("Connected to:", client_address)
            pickleData = client_socket.recv(1024)
            data = pickleUtilities.unPickler(pickleData)
            print("Received:", data)
            saveFile(data, 'receivedPickle.txt')
        finally:
            client_socket.close()
if __name__ == "__main__":
    runServer()