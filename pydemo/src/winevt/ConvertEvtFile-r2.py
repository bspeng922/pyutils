'''
Created on 2013-1-8

@author: wang_peng

那就要看你要查的串有多长了，比如最长的串200字节，那么你除了分块之外，
再将块的分割点的左右200字节，拼起来再查找，就肯定不会漏查啊，
如果你待查的串长度不固定，而又可能非常大的时候，这么搞效率就非常低了

'''

import os, sys
import binascii
import time

def convertfile(infile, outfile):
    
    fread = open(infile, "rb")  #1.67    
    instr = fread.read().encode('hex')  #1.72
    fread.close()    #2.67

    '''find the strings position'''
    placefind = kmp_matcher(instr, "11111111222222223333333344444444")
    newstr = instr[placefind+32:placefind+64]
    print "String find: %s"%newstr    #3 --> 2.67
    
    instr = instr[:32] + newstr + instr[64:]
    instr = instr[:72] + "08" + instr[74:]      
    
    '''write to new file'''
    fwrite = open(outfile, "wb")
    fwrite.write(instr.decode('hex'))    #2.70
    fwrite.close()

def compute_prefix_function(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in xrange(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k - 1]
        if p[k] == p[q]:
            k = k + 1
        pi[q] = k
    return pi

def kmp_matcher(t, p):
    n = len(t)
    m = len(p)
    pi = compute_prefix_function(p)
    q = 0
    for i in xrange(n):
        while q > 0 and p[q] != t[i]:
            q = pi[q - 1]
        if p[q] == t[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return -1


if __name__ == "__main__":
    starttime = time.time()
    if len(sys.argv) == 1 :
        infilepath = raw_input("Please input the path of EVT file -> ")
        outfilepath = infilepath[:infilepath.rfind(".")] + ".new.Evt"
    elif len(sys.argv) == 2 :
        infilepath = sys.argv[1]
        outfilepath = infilepath[:infilepath.rfind(".")] + ".new.Evt"
    elif len(sys.argv) == 3:
        infilepath = sys.argv[1]
        outfilepath = sys.argv[2]
    else:
        print "Error args ."
        raw_input("")
        sys.exit()
        
    print "Running..."
    convertfile(infilepath, outfilepath)
    print "Done ."    #2.70
    endtime = time.time()
    print "Time used: ",(endtime - starttime)," s"


