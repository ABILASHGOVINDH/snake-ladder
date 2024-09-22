import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1111))
s.listen()

while True:
    client,address = s.accept()
    print("connect",address)
    client.send("you are connected".encode())
    client.close()