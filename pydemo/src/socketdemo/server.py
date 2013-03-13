import socket

host = ""
port = 51423

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print "server is running on port %d, press ctrl-C to terminate. " \
%port

while 1:
    clientsock, clientaddr = s.accept()
    print clientaddr
    clientfile = clientsock.makefile('rw', 0)
    clientfile.write("Welcome, "+str(clientaddr) + "\n")
    clientfile.write("Please enter a string: ")
    
    line = clientfile.readline().strip()
    clientfile.write("You entered %d cjaracters .\n"%len(line))
    clientfile.close()
    clientsock.close()