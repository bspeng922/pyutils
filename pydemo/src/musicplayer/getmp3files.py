#-*- coding: utf-8 -*-
import os
import glob

fldpath = "E:/MP3"

if os.path.exists(fldpath):
    fs = glob.glob(fldpath + "\\*." + "mp3")
    
    for f in fs:
        print os.path.basename(f).decode("cp936").encode("utf8") 