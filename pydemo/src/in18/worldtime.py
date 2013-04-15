import wx
import time

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#000000")
        font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Georgia")
        
        self.dt = wx.DateTime()
        
        self.tokyo = wx.StaticText(self.panel, -1, self.dt.FormatTime(),(20,20))
        self.tokyo.SetForegroundColour("#23f002")
        self.tokyo.SetFont(font)
        
        self.moscow = wx.StaticText(self.panel, -1, self.dt.FormatTime(),(20,70))
        self.moscow.SetForegroundColour("#23f002")
        self.moscow.SetFont(font)
        
        self.budapest = wx.StaticText(self.panel, -1, self.dt.FormatTime(),(20,120))
        self.budapest.SetForegroundColour("#23f002")
        self.budapest.SetFont(font)
        
        self.london = wx.StaticText(self.panel, -1, self.dt.FormatTime(),(20,170))
        self.london.SetForegroundColour("#23f002")
        self.london.SetFont(font)
        
        self.newyork = wx.StaticText(self.panel, -1, self.dt.FormatTime(),(20,220))
        self.newyork.SetForegroundColour("#23f002")
        self.newyork.SetFont(font)
        
        self.OnTimer(None)
        self.timer = wx.Timer(self)
        self.timer.Start(1000)
        self.Bind(wx.EVT_TIMER, self.OnTimer)
        
    def OnTimer(self, event):
        now = self.dt.Now()
        
        self.tokyo.SetLabel("Tokyo: "+str(now.Format(('%s %T'), wx.DateTime.GMT_9)))
        self.tokyo.SetLabel("moscow: "+str(now.Format(('%s %T'), wx.DateTime.MSD)))
        self.tokyo.SetLabel("budapest: "+str(now.Format(('%s %T'), wx.DateTime.CEST)))
        self.tokyo.SetLabel("london: "+str(now.Format(('%s %T'), wx.DateTime.WEST)))
        self.tokyo.SetLabel("newyork: "+str(now.Format(('%s %T'), wx.DateTime.EDT)))

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()        
