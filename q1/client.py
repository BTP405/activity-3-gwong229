import socket
import os
import pickleUtilities

def readFile(fileName):
    fileDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(fileDir, fileName)
    with open(filePath, 'rb') as file:
        return file.read()

def runClient(fileName):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)
    try:
        fileContents = readFile(fileName)
        print(fileContents)
        pickledContents = pickleUtilities.pickler(fileContents)
        client_socket.sendall(pickledContents)
    finally:
        client_socket.close()

if __name__ == "__main__":
    runClient("test.txt")
