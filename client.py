import socket

s = socket.socket()
port = 12345
while True:
    try:
        s.connect(('192.168.1.52', port))

        data = s.recv(1024).decode()
        splitted = data.split('~')
        print(splitted)
        s.close()
        break
    except:
        pass