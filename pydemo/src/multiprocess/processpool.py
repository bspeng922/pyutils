'''
Created on 2013-1-17

@author: wang_peng
'''
from multiprocessing import Pool 

def hello(times, me="moose"):
    print times
    return me, times
    
    
if __name__ == "__main__":
    mylist = [i  for i in range(1000)]
    
    pool = Pool(10)
    who = pool.map(hello, mylist)
    
    pool.close()    #close after finish
    pool.join()    #wait for process end
    
    print who

    pool2 = Pool(3)
    result = []
    for i in range(5):
        result.append(pool2.apply(hello, (i, )))
    pool2.close()
    pool2.join()
    print result
    
    print "Done"
