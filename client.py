import socket

s = socket.socket()
port = 12345
while True:
    try:
        s.connect(('127.0.0.1', port))
        
        if(s.recv(1024).decode() == 'andromeda'):
            s.close()
            break
    except:
        pass