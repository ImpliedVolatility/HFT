import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

fullmsg = ""
while True:
    message = s.recv(1024)
    if len(message) <= 0:
        break
    fullmsg += message.decode("utf-8")
    print(message.decode("utf-8"))
print(fullmsg)
