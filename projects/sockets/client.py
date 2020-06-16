import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.connect(socket.gethostname)
mssg = s.recv(1024)
print(mssg.decode("utf-8"))
