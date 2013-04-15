import ctypes

mciSendString = ctypes.windll.winmm.mciSendStringA
mciGetErrorString = ctypes.windll.winmm.mciGetErrorStringA

lInitCommands = ['set %s bitspersample 8 wait',
                 'set %s channels 1 wait',
                 'set %s bytespersec 8000 wait',
                 'set %s samplespersec 8000 wait',
                 ]
sLevelCmd = "status %s level wait"
sOpenCmd = "open new type waveaudio alias %s wait"
sRecordCmd = "record %s"
sStopCmd = "stop %s wait"
sPauseCmd = "pause %s wait"
sResumeCmd = "resume %s wait"
sCloseCmd = "close %s wait"
sSaveCmd = 'save %s "%s" wait'
sDelCmd = 'delete %s "%s" wait'
sInfoLenCmd = 'status %s length wait'

(eClosed, eOpened, eRecording, ePaused) = range(4)

def send(command):
    command = str(command)
    
    buffer = ctypes.c_buffer(255)
    errorcode = mciSendString(command, buffer, 254, 0)
    
    if errorcode:
        mciGetErrorString(errorcode, buffer, 254)
        
    return errorcode,buffer.value

class MCIError(Exception):
    def __init__(self, err, desc=None):
        self.err = err
        if desc:
            self.desc = desc
        else:
            self.desc = "(No description)"
    
    def __str__(self):
        return "MCI Error %d:%s"%(self.err, self.desc)
    
class Recorder():
    def __init__(self, filename=None):
        self._sDevAlias = hex(id(self))[2:]
        self._sFileName = filename
        self._eStatus = eClosed
        
    def __del__(self):
        try:
            if self._eStatus in (ePaused, eRecording):
                self.Stop()
        except MCIError:
            pass
    
    def Open(self):
        if not self._eStatus == eClosed:
            raise MCIError(0,"Already opened")
        err, desc = send(sOpenCmd % self._sDevAlias)
        if err:
            raise MCIError(err, desc)
        for cmd in lInitCommands:
            err, desc = send(cmd % self._sDevAlias)
            if err:
                try:
                    self.Close()
                except MCIError:
                    pass
                raise MCIError(err, desc)
        self._eStatus = eOpened
        
    def GetAlias(self):
        return self._sDevAlias
    
    def Start(self):
        if self._eStatus == eOpened:
            err, desc = send(sRecordCmd % self._sDevAlias)
            if err:
                raise MCIError(err, desc)
        elif self._eStatus == ePaused:
            self.Resume()
        else:
            raise MCIError(0, "Cannot start in current state")
        
        self._eStatus = eRecording
        
    def Stop(self):
        if not self._eStatus == eRecording:
            raise MCIError(0, "Not recording")
        err, desc = send(sStopCmd%self._sDevAlias)
        if err:
            raise MCIError(err, desc)
        self._eStatus = eOpened
        
    def Pause(self):
        if not self._eStatus == eRecording:
            raise MCIError(0, "Not recording")
        err, desc = send(sPauseCmd % self._sDevAlias)
        if err:
            raise MCIError(err, desc)
        self._eStatus = ePaused
        
    def Close(self):
        if not self._eStatus == eOpened:
            raise MCIError(0, "Not opened or recording")
        err, desc = send(sCloseCmd % self._sDevAlias)
        if err:
            raise MCIError(err, desc)
        self._eStatus = eClosed
        
    def Resume(self):
        if not self._eStatus == ePaused:
            raise MCIError(0, "Not paused")
        err, desc = send(sResumeCmd % self._sDevAlias)
        if err:
            raise MCIError(err, desc)
        self._eStatus = eRecording
        
    def Save(self, filename=None):
        if not self._eStatus == eOpened:
            raise MCIError(0, "Not opened or recording")
        if filename:
            self._sFileName = filename
        if not self._sFileName:
            raise MCIError(0, "Filename not set")
        err, desc = send(sSaveCmd % (self._sDevAlias, self._sFileName))
        if err:
            raise MCIError(err, desc)
        
    def Delete(self, nFrom=0, nTo=None):
        if not self._eStatus == eOpened:
            raise MCIError(0, "Not opened or recording")
        sFrom = "From %d" % nFrom
        sTo = ""
        
        if nTo:
            sTo = "to %d"%nTo
        sCmd = sDelCmd % (self._sDevAlias, " ".join([sFrom, sTo]))
        err, desc = send(sCmd)
        
        if err:
            print "Command: ",sCmd
            print "Length:",
            raise MCIError(err, desc)
        
    def GetLevel(self):
        if self._eStatus == eClosed:
            raise MCIError(0, "Not opened")
        err, desc = send(sLevelCmd % self._sDevAlias)
        if err:
            raise MCIError(err, desc)
        return int(desc)
    
    def GetLength(self):
        if self._eStatus == eClosed:
            raise MCIError(0, "Not opened")
        err, desc = send(sInfoLenCmd % self._sDevAlias)
        if err:
            raise MCIError(err, desc)
        
        return int(desc)
        



