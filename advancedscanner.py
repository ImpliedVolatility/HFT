import socket
import threading
from queue import Queue

printlock = threading.Lock()
target = "www.hackthissite.org"


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with printlock:
            print("port " + str(port) + " is open!!!!!!!")
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()

for x in range(30):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 10000):
    q.put(worker)

q.join()
