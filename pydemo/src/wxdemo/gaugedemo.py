import wx

class GuageFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Guage Frame", size=(300,400))
        panel = wx.Panel(self)
        
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimeChange, self.timer)
        self.timer.Start(1000)
        self.timecount = 0
        
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimeOut, self.timer2)
        self.timer2.Start(10000)
        
        self.gauge = wx.Gauge(panel, -1, 50, (20,50),(250,20))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        
    def OnTimeChange(self, event):
        self.timecount += 1
        self.gauge.SetValue(self.timecount*5)
    
    def OnTimeOut(self, event):
        self.timecount = 0

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = GuageFrame(None, -1)
    frame.Show()
    app.MainLoop()