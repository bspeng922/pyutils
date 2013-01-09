import os, sys
import binascii
import time

def convertfile(infile, outfile):
    
    fread = open(infile, "rb")  
    findedstr = ""
    
    while 1:
        strpart = fread.read(8192).encode('hex')

        '''if at the end or less than 32 char'''
        if strpart == "" or len(strpart) < 32 :
            break

        strposition = strpart.find("11111111222222223333333344444444")
        if strposition <> -1:
            '''if pos at end'''
            remainstrlen = len(strpart)-strposition - 32
            if remainstrlen < 64:
                findedstr = strpart[strposition+32:] + fread.read((64-remainstrlen)/2).encode('hex')
            else:
                findedstr = strpart[strposition+32:strposition+64]
                
            break
        
        '''get top32 char and end32 char'''
        prepartendstr = strpart[-64:]

        '''read next 64 char'''
        nextpartstartstr = fread.read(64).encode('hex')
        joinstr = prepartendstr + nextpartstartstr

        strposition = joinstr.find("11111111222222223333333344444444")
        if strposition <> -1:
            remainstrlen = len()-strposition-32
            if remainstrlen < 64:
                findedstr = strpart[strposition+32:] + fread.read((64-remainstrlen)/2).encode('hex')
            else:
                findedstr = strpart[strposition+32:strposition+64]
        
            break

        fread.seek(-64,1)
        
    fread.close()    
    print "String find: %s"%findedstr

    '''reread and write to new file'''
    reread = open(infile, "rb")
    fwrite = open(outfile, "wb")
    partcount = 1

    while 1:
        instr = reread.read(8192)   
        if instr == "" :
            break
        
        if partcount <> 1:
            fwrite.write(instr)
        else:
            instr = instr.encode('hex')
            instr = instr[:32] + findedstr + instr[64:]
            instr = instr[:72] + "08" + instr[74:]
            fwrite.write(instr.decode('hex'))
            
        partcount += 1

    fwrite.close()
    reread.close()    



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
    
    starttime = time.time()    
    print "Running..."
    convertfile(infilepath, outfilepath)
    print "Done ."    
    endtime = time.time()
    print "Time used: ",(endtime - starttime)," s"


