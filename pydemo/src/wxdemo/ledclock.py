import time
import wx
import wx.gizmos as gizmos

class LedClock(wx.Frame):
    def __init__(self, parent, id):
        pos = wx.DefaultPosition
        wx.Frame.__init__(self, parent, id, title="led Clock", pos=pos, size=(350, 100))
        size = wx.DefaultSize
        style = gizmos.LED_ALIGN_CENTER
        self.led = gizmos.LEDNumberCtrl(self, -1, pos, size, style)
        #self.led.SetBackgroundColour("Blue")
        #self.led.SetForegroundColour("Black")
        self.OnTimer(None)
        self.timer = wx.Timer(self, -1)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        
    def OnTimer(self, event):
        current = time.localtime(time.time())
        ts = time.strftime("%H:%M:%S",current)
        self.led.SetValue(ts)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = LedClock(parent=None, id=-1)
    frame.Show()
    app.MainLoop()