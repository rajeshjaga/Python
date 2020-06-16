import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1024))
s.listen()
while True:
    clt, adrs = s.accept()
    print(f"Connection estab..{adrs}")
    clt.send(bytes("hello world", "utf-8"))
