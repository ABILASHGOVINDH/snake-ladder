import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1111))
msg = s.recv(1024)
s.close()

print(msg.decode())