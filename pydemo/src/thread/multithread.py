import time
import urllib2
import HTMLParser
import threading
import Queue
from bs4 import BeautifulSoup

hosts = ["http://www.baidu.com", "http://www.amazon.com","http://www.ibm.com","http://www.pystack.org",
         "http://www.python.org","http://www.microsoft.com"]

def read(host):
    try:
        context = urllib2.urlopen(host, timeout=6)
    except urllib2.URLError:
        print "Load %s failure."%host
        return 
        
    try:
        title = BeautifulSoup(context).title.string
    except HTMLParser.HTMLParseError:
        print "parser %s title failure."%host
        return
    
    print "%s : %s"%(host, title)
    
class Reader(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.setDaemon(True)
        
    def run(self):
        while 1:
            host = self.queue.get()
            print "------"+host
            read(host)
            self.queue.task_done()
            
def concuryRead():
    start = time.time()
    queue = Queue.Queue()
    threads = []
    for i in range(30):
        for host in hosts:
            queue.put(host)
            threads.append(Reader(queue))
    [t.start() for t in threads]
    queue.join()
    end = time.time()
    
    print "Elapsed Time: %d"%(end-start)
    
if __name__ == "__main__":
    concuryRead()