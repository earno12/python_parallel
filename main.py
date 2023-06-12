import threading
# or can use the following:
    # multiprocessing
    # threading
    # concurrent.futures

def my_function():
    # do something
    return

t = threading.Thread(target=my_function)
t.start
t.join()
