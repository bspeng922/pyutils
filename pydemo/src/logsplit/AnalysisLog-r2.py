#-*- coding:utf8 -*-

import os, sys, time


def analysislog(filepath, keyword):
    if not os.path.exists(filepath):
        print "File not found !"
        raw_input("")
        sys.exit()

    keywordlist = keyword.split("|")
    fileobjlist = {}
    for key in keywordlist:
        fileobjlist[key] = open(key+".log", 'w')
    
    logfile = open(filepath, 'r')
    
    while 1:
        logline = logfile.readline()

        if logline == "":
            break

        for key in keywordlist:
            if key.find("&") <> -1:
                andkeylist = key.split("&")
                andflag = 1
                for andkey in andkeylist:
                    if logline.find(andkey) == -1:
                        andflag = 0
                if andflag:
                    #appendtonewfile(logline, key+".log")
                    fileobjlist[key].write(logline)

            else:
                if logline.find(key) <> -1:
                    #appendtonewfile(logline, key+".log")
                    fileobjlist[key].write(logline)
    for key in keywordlist:
        fileobjlist[key].close()


    logfile.close()


def appendtonewfile(logstr, newlogname):
    newlogfile = open(os.path.join(os.getcwd(), newlogname),"a")

    newlogfile.write(logstr)

    newlogfile.close



if __name__ == "__main__":
    if len(sys.argv) == 1 :
        logfilepath = raw_input("Please input the path of the log -> ")
        keywords = raw_input("Please input the keywords(split by |) -> ")
    elif len(sys.argv) == 2 :
        logfilepath = sys.argv[1]
        keywords = raw_input("Please input the keywords(split by |) -> ")
    elif len(sys.argv) == 3 :
        logfilepath = sys.argv[1]
        keywords = sys.argv[2]
    else :
        print "Illegal Parameters...\n    AnalysisLog.py [logpath] [keywords] "
        raw_input("")
        sys.exit()

    
    print "Log Path: %s"%logfilepath
    print "Keywords: %s"%keywords.replace("|", " ")
    
    starttime = time.time()
    analysislog(logfilepath, keywords)
    endtime = time.time()
    print "Time used: ",(endtime - starttime)," s"
        
        
