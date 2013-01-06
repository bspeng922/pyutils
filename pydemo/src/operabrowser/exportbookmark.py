'''
Created on 2013-1-6

@author: wang_peng
'''
#-*- coding:utf-8 -*-
import os
import time
import sys

def convertBookmark(bmpath):
    if not os.path.exists(bmpath):
        print "file not exists !"
        
    bmsavedir = os.path.join(os.getcwd(),"bookmarks")
    if not os.path.exists(bmsavedir):
        os.mkdir(bmsavedir)

    
    currfldPath = ""    #currend directory
    folder = 0
    urlok = 0
    urlerror = 0
    bmfile = open(bmpath, 'r')
        
    while 1:
        bmline = bmfile.readline()
        if len(bmline) == 0:
            break
        #print bmline

        '''create folder'''
        if bmline.find("#FOLDER") <> -1:
            bmfldid = bmfile.readline().split("=")[1]
            bmfldname = bmfile.readline().split("=")[1][:-1].decode('utf8')
            currfldPath = os.path.join(bmsavedir,bmfldname)
            if not os.path.exists(currfldPath):
                os.mkdir(currfldPath)
            folder += 1
            print "\nFOLDER(%s)"%bmfldname

        '''create urls'''
        if bmline.find("NAME") <> -1:
            bmurlname = bmline.split("=")[1][:-1].decode('utf8')            
            bmurlpath = bmfile.readline().split("=")[1][:-1].decode('utf8')

            if generateurllink(currfldPath, bmurlname, bmurlpath) :
                urlok += 1
            else :
                urlerror += 1

    bmfile.close()
    print "\n\nFolder: %d\nFile: OK: %d\tError: %d"%(folder,urlok,urlerror)


def generateurllink(fldpath, urlname, urlpath):
    try:
        urlname = legalfilename(urlname)    #file name may illegal
        
        bmurlfile = open(os.path.join(fldpath, urlname),'w')
        bmurlfile.write(urlpath)
        bmurlfile.close()
        
        print "    URL(%s)"%urlname
        return 1
    except:
        print "    ERROR(%s)"%urlname
        return 0

def legalfilename(filename):
    illegalchars = ['<','>','/','|','\\',':','"','*','?']

    for mychar in illegalchars :
        if filename.find(mychar) <> -1:
            filename = filename.replace(mychar, " ")    #wow
            
    #print filename
    return filename

if __name__ == "__main__":
    if len(sys.argv) == 1 :
        bmpath = raw_input("Please input the bookmark file(*.adr) -> ")
    else :
        bmpath = sys.argv[1]
        print bmpath

    #print bmpath
    convertBookmark(bmpath)
    time.sleep(1)
    os.system(os.path.join(os.getcwd(), "html2urllink.vbs"))
