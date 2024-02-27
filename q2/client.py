import socket
import pickleUtilities

def sendTask(workerNode, task):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySocket:
            mySocket.connect((workerNode, 5000))
            pickledTask = pickleUtilities.pickler(task)
            mySocket.send(pickledTask)
            result = pickleUtilities.unPickler(mySocket.recv(4096))
            if result is not None:
                print(f"Result from {workerNode}: {result}")
                return result
            else:
                print("error")
    except Exception as e:
        print(f"Error connecting to {workerNode}: {str(e)}")


def exampleTask1(x, y):
    return x + y
def exampleTask2(x, y):
    return x - y
globals()['exampleTask1'] = exampleTask1
globals()['exampleTask2'] = exampleTask2

if __name__ == "__main__":
    workerNodes = ['localhost', 'localhost']
    tasks = [
        {'function': exampleTask1, 'args': (1, 2)},
        {'function': exampleTask2, 'args': (4, 3)}
    ]
    i = 0
    for task in tasks:
        sendTask(workerNodes[i], task)
        i += 1