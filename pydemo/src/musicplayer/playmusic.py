#-*- coding: utf-8 -*-

import os
import ctypes
import time

mciSendString = ctypes.windll.winmm.mciSendStringA

class Mp3Player():
    def __init__(self, filename, alias):
        self.filename = filename
        self.alias = alias
        self.buffer = ctypes.c_buffer(255)
        mciSendString('open "%s" alias %s'%(self.filename,self.alias), self.buffer, 254, 0)
        mciSendString('set %s time format milliseconds'%self.alias, self.buffer, 254, 0)
        
    def play(self):
        print "Now playing..."
        time.sleep(2000)
        mciSendString("play %s"%self.alias, self.buffer, 254, 0)
        
    def stop(self):
        mciSendString("stop %s"%self.alias, self.buffer, 254, 0)
        mciSendString("seek %s to start"%self.alias, self.buffer, 254, 0)
    
    def seconds(self):
        return int(mciSendString("status %s length"%self.alias))
        
    def __del__(self):
        mciSendString("close %s"%self.alias, self.buffer, 254, 0)
        

if __name__ == "__main__":
    mp3 = Mp3Player(r'C:\Users\Public\Music\Sample Music\Kalimba.mp3',"mysong1")
    print mp3.seconds()
    mp3.play()
    #print "Done"
    
    time.sleep(mp3.seconds()*1000)
    mp3.stop()