import time
import urllib2
import HTMLParser
from bs4 import BeautifulSoup

hosts = ["http://www.baidu.com", "http://www.amazon.com","http://www.ibm.com","http://www.pystack.org",
         "http://www.python.org","http://www.microsoft.com"]

def read(host):
    try:
        context = urllib2.urlopen(host, timeout=5)
    except urllib2.URLError:
        print "load %s failure."%host
        return 
    
    try:
        title = BeautifulSoup(context).title.string
    except HTMLParser.HTMLParseError:
        print "parser %s title failure"%host
        return
    
    print "%s : %s"%(host, title)
    
def singleRead():
    start = time.time()
    
    for i in range(2):
        for host in hosts:
            read(host)
    
    end = time.time()
    
    print "Elapsed time: %d"%(end-start)
    
if __name__ == "__main__":
    singleRead()