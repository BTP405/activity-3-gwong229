import socket
import threading
import time
import sys
sys.path.append('..')
import pickleUtilities

def receiveMessages(clientSocket):
    """receive messages loop with pickling logic"""
    while True:
        try:
            data = clientSocket.recv(1024)
            if not data:
                break

            message = pickleUtilities.unPickler(data)
            print(message)

        except Exception as e:
            print(f"Error: {e}")
            break

def sendMessage(clientSocket):
    """sending messages loop with pickling logic and spam protection time delay"""
    while True:
        message = input("Enter your message: ")
        clientSocket.send(pickleUtilities.pickler(message))
        time.sleep(0.5)


def main():
    """main function which creates sockets and two threads, one for each logic for concurrency"""
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 5555))

    receiveThread = threading.Thread(target=receiveMessages, args=(clientSocket,))
    sendThread = threading.Thread(target=sendMessage, args=(clientSocket,))

    receiveThread.start()
    sendThread.start()

    receiveThread.join()
    sendThread.join()

if __name__ == "__main__":
    main()