#-*- coding:utf-8 -*-
'''
Created on 2013-1-30

@author: wang_peng
'''
import os
import zipfile

filename = "E:\\test.zip"
currdir = "E:\\vpn\\"

os.chdir(currdir)

#tfile = zipfile.ZipFile(filename, 'w')
#files = os.listdir(currdir)
#for f in files:
#    #print f     # it is a string
#    tfile.write(f)
#    
#for f in tfile.namelist():
#    print "added %s"%f
#    
#tfile.close()

print zipfile.is_zipfile(filename)

tfile = zipfile.ZipFile(filename, 'r')
for file in tfile.namelist():
    print file

tinfo = tfile.getinfo("privatetunnel.msi")
print tinfo.comment
print tinfo.compress_size
print tinfo.date_time
print tinfo.file_size
print tinfo.compress_type
print tinfo.filename

buffer = tfile.read("SerialsNum.txt")
print buffer

tfile.close()