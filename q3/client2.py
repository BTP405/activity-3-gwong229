import socket
import pickleUtilities
import threading
import time

def receiveMessages(clientSocket):
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
    while True:
        message = input("Enter your message: ")
        clientSocket.send(pickleUtilities.pickler(message))
        time.sleep(0.5)


def main():
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