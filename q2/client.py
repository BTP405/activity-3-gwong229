import socket
import sys
sys.path.append('..')
import pickleUtilities

def sendTask(workerNode, task):
    """Sends a task to a node, after pickling using my pickle utilities"""
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
    """i couldnt get rid of these ;("""
    return x + y
def exampleTask2(x, y):
    return x - y

if __name__ == "__main__":
    """creates tasks, sends to workernodes in an array"""
    workerNodes = ['localhost', 'localhost']
    tasks = [
        {'function': exampleTask1, 'args': (1, 2)},
        {'function': exampleTask2, 'args': (4, 3)}
    ]
    i = 0
    for task in tasks:
        sendTask(workerNodes[i], task)
        i += 1