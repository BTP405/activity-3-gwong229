import pickle

def pickler(pickleTarget):
    return pickle.dumps(pickleTarget)

def unPickler(unPickleTarget):
    return pickle.loads(unPickleTarget)