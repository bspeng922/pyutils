import wx
import sys

class TestFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Full Screen Test")
        
        self.ShowFullScreen(True, style=wx.FULLSCREEN_ALL)
        self.InitUI()
        
    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#555")
        sizer = wx.GridBagSizer(5,5)
        
        self.mutebtn = wx.Button(panel, -1, "Mute")
        sizer.Add(self.mutebtn, pos=(0,3), flag = wx.TOP, border=7)
        
        self.closebtn = wx.Button(panel, -1, "Close")
        sizer.Add(self.closebtn, pos=(0,4), flag = wx.RIGHT | wx.TOP, border=7)
        
        self.timelabel = wx.StaticText(panel, -1, "Rest for 3 mins")
        sizer.Add(self.timelabel, pos=(2, 0), span=(1,5), flag=wx.ALIGN_CENTER | wx.LEFT | wx.RIGHT, border=7)
        
        self.timeProcess = wx.StaticText(panel, -1, "00:00")
        font = wx.Font(20, wx.ROMAN, wx.NORMAL, wx.BOLD, True)
        self.timeProcess.SetFont(font)
        sizer.Add(self.timeProcess, pos=(3,0), span=(1,5), flag=wx.ALIGN_CENTER|wx.LEFT|wx.RIGHT, border=7)
        
        self.footLabel = wx.StaticText(panel, -1, "have a good rest")
        sizer.Add(self.footLabel, pos=(5,4), flag=wx.RIGHT|wx.BOTTOM, border=7)
        
        sizer.AddGrowableRow(1)
        sizer.AddGrowableRow(4)
        sizer.AddGrowableCol(0)
        panel.SetSizerAndFit(sizer)
        
        self.Bind(wx.EVT_BUTTON, sys.exit, self.closebtn)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = TestFrame(None, -1)
    frame.Show()
    app.MainLoop()
        