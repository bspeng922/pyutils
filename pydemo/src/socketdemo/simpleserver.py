#-*- coding:cp936 -*-
import socket
import traceback

host=""
port = 51243

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #һ�����������̽����󣬲���ϵͳ�ᱣ�����������Ķ˿ڣ�Ҳ��������Ϊ�����ر�
s.bind((host, port))
s.listen(5)

while 1:
    print "1"
    try:
        clientsocket, clientaddr = s.accept()    #����ʽ
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        continue
    
    try:
        print "Got connection from ",clientsocket.getpeername()
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()
        
    try: 
        clientsocket.close()
    except KeyboardInterrupt:
        raise
    except:
        traceback.print_exc()
        
    print "2"

solist = [x for x in dir(socket) if x.startswith("SO_")]
solist.sort()
for x in solist:
    print x