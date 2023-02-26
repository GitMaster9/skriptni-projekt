import threading

def startThread(functionThread, targetFunction, functionArgument = None, logTurnedOn = False):
    if functionThread.is_alive is True:
        print("ERROR: thread " + str(functionThread) + " is alive. Killing the thread by code...")
        print()
        functionThread.join()
        return

    if functionArgument:
        functionThread = threading.Thread(target=targetFunction, args=(functionArgument,))
    else:
        functionThread = threading.Thread(target=targetFunction)

    if logTurnedOn is True:
        print("LOG: Starting thread: " + str(functionThread) + ".")
        print("LOG: Target function: " + str(targetFunction) + ".")
        print()
    functionThread.start()

def endThread(functionThread, logTurnedOn = False):
    if functionThread.is_alive is True:
        if logTurnedOn is True:
            print("LOG: thread " + str(functionThread) + " is alive. Killing the thread by code...")
            print()
        functionThread.join()
        return
    else:
        print("LOG: thread is not alive.")