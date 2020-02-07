import socket

host = '127.0.0.1'
port = 9500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
c, addr = s.accept()

while True:
    data = c.recv(1024).decode()
    if data == "Hello":
        print(f"Server received this message from client: {data}")
        c.send("Hi".encode())
        break
    else:
        print(f"Server received this message from client: {data}")
        c.send("Goodbye".encode())
        break
    s.close()
