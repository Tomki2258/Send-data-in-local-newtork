import eel
from random import randint
import socket

eel.init("web")
@eel.expose
def server_do():

    s = socket.socket()		
    print ("Socket successfully created")


    port = 12345			
    s.bind(('', port))		
    print ("socket binded to %s" %(port))

    s.listen(5)	
    print ("socket is listening")		

    while True:
        print('sus')
        c, addr = s.accept()	
        print ('Got connection from', addr )

        c.send('andromeda'.encode())

        c.close()

        break

eel.start("index.html")