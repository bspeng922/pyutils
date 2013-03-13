#-*- coding:cp936 -*-
import socket
import traceback

host=""
port = 51243

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #一个服务器进程结束后，操作系统会保留几分钟他的端口，也可以设置为立即关闭
s.bind((host, port))
s.listen(5)

while 1:
    print "1"
    try:
        clientsocket, clientaddr = s.accept()    #阻塞式
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