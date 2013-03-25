import time
import sys
import urllib2
import HTMLParser
from bs4 import BeautifulSoup
import multiprocessing

hosts = ["http://www.baidu.com", "http://www.amazon.com","http://www.ibm.com","http://www.pystack.org",
         "http://www.python.org","http://www.microsoft.com"]

def read(host):
    try:
        context = urllib2.urlopen(host, timeout=6)
    except:
        print "load %s failure"%host
        return
    
    try:
        title = BeautifulSoup(context).title.string
    except HTMLParser.HTMLParseError:
        print "parser %s title failure"%host
        return 
    
    print "%s - %s"%(host, title)
    
class Reader(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue
    
    def run(self):
        while 1:
            host = self.queue.get()
            read(host)
            self.queue.task_done()
            
def concuryread():
    start = time.time()
    queue = multiprocessing.JoinableQueue()
    process = []
    
    for i in range(10):
        for host in hosts:
            queue.put(host)
            process.append(Reader(queue))
            
    [p.start() for p in process]
    queue.join()
    end = time.time()
    
    print "Elapsed Time: %d"%(end-start)
    
if __name__ == "__main__":
    concuryread()