import socket


s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#设置可以广播
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("172.20.10.5", 8888))

while True:
    data,addr = s.recvfrom(100)
    print(data)
