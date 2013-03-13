import socket
import sys

port = 70
#host = sys.argv[1]
host = "quux.org"
#filename = sys.argv[2]
filename = "/"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except socket.gaierror, e:
    print "Error connecting to server: %s"%e
    sys.exit(1)

fd = s.makefile("rw", 0)
fd.write(filename + "\r\n")

for line in fd.readlines():
    sys.stdout.write(line)
#s.sendall(filename + "\r\n")
#
#while 1:
#    buf = s.recv(2048)
#    if not len(buf):
#        break
#    sys.stdout.write(buf)
