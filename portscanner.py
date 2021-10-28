import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "www.hackthissite.org"


def pscan(port):
    try:
        s.connect(server, port)
        return True
    except:
        return False


for x in range(1, 26):
    if pscan(x):
        print("port " + str(x) + " is open!!!!!!!!!!!!!!!!!!")
    else:
        print("port " + str(x) + " is closed.")

