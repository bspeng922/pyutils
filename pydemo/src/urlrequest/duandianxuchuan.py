import urllib2

handler = urllib2.HTTPHandler()
request = urllib2.Request(url='http://ftp.ubuntu.com/')
request.headers['Range'] = 'bytes=%s-%s' % (0, 667)
f = urllib2.urlopen(request)
print f.read()

print f.headers.values()  
print f.headers['content-length']