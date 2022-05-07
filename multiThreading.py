import threading
import time


lock1 = threading.Lock()
lock2 = threading.Lock()


def printThread1():
    for i in range(10):
        lock1.acquire()
        print(threading.current_thread())
        lock2.release()


def printThread2():
    for i in range(10):
        lock2.acquire()
        print(threading.current_thread())
        lock1.release()


t1 = threading.Thread(target=printThread1)
t2 = threading.Thread(target=printThread2)

lock2.acquire()

t1.start()
t2.start()

t1.join()
t2.join()

