'''
Created on 2013-1-8

@author: wang_peng
'''
import os, sys
import binascii

def convertfile(infile, outfile):
    fread = open(infile, "rb")

    instr = fread.read().encode('hex')
    #print "raw: ",type(instr)
    #print instr[:32]

    '''find the strings position'''
    placefind = kmp_matcher(instr, "11111111222222223333333344444444")
    newstr = instr[placefind+32:placefind+64]
    print "String find: %s"%newstr

    
    instr = instr[:32] + newstr + instr[64:]
    instr = instr[:72] + "08" + instr[74:]  
    
    fread.close()

    '''write to new file'''
    fwrite = open(outfile, "wb")
    fwrite.write(instr.decode('hex'))
    fwrite.close()

def compute_prefix_function(p):
    m = len(p)
    pi = [0] * m
    k = 0
    for q in range(1, m):
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
    for i in range(n):
        while q > 0 and p[q] != t[i]:
            q = pi[q - 1]
        if p[q] == t[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return -1


if __name__ == "__main__":

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
        

    convertfile(infilepath, outfilepath)
    print "Done ."


