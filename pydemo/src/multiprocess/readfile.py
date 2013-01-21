'''
Created on 2013-1-17

@author: wang_peng
'''
import time
from multiprocessing import Process

def hello(str,times):
    print times

if __name__ == "__main__":
    starttime = time.time()
    for i in range(1,100):
        p = Process(target=hello, args=("hello ",i))
        p.start()
        
    p.join()
        
    endtime = time.time()
    print "TimeUsed: ",(endtime-starttime)