import gopherlib, sys

host = ""
file = ""

f = gopherlib.send_selector(file, host)

for line in f.readlines():
    sys.stdout.write(line)
