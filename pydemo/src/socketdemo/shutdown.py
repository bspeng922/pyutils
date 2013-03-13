import socket
import sys
import time

host = "quux.org"
textport = "http"
filename = "/"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, e:
    print "Strange error creating socket: %s"%e
    sys.exit(1)
    
try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(textport, "tcp")
    except socket.error, e:
        print "Couldnot find your port: %s"%e
        sys.exit(1)
        
try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Address-related error connecting to server: %s"%e
    sys.exit(1)
except socket.error, e:
    print "Connection error: %s"%e
    sys.exit(1)
    
fd = s.makefile("rw",0)
    
print "sleeping..."
time.sleep(10)
print "continuing."

try:
    fd.write("Get %s HTTP/1.0\r\n\r\n"%filename)
except socket.error, e:
    print "Error sending data: %s"%e
    sys.exit(1)

try:
    fd.flush()
except socket.error, e:
    print "Error sending data(detected by flush): %s"%e
    sys.exit(1)
    
#try:
#    s.sendall("Get %s HTTP/1.0\r\n\r\n" % filename)
#except socket.error, e:
#    print "Error sending data: %s"%e
#    sys.exit(1)

    
try:
    s.shutdown(1)
except socket.error, e:
    print "Error sending data (detected by shutwodn): %s"%e
    sys.exit(1)
    
while 1:
    try:
        #buf = s.recv(2048)
        buf = fd.read(2048)
    except socket.error, e:
        print "Error receiving data: %s"%e
        sys.exit(1)
        
    if not len(buf):
        break
    sys.stdout.write(buf)

