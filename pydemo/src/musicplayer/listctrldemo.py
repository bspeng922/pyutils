#-*- coding: utf-8 -*-
import wx, os, glob

debug = True
mp3folder = "E:\\MP3"

class Mp3Frame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Music Player", size=(400,300))
        self.Center()
        panel = wx.Panel(self)
        
        self.index = 0
        self.listctrl_mc = wx.ListCtrl(panel, -1, size=(-1,200), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.listctrl_mc.InsertColumn(0, "ID")
        self.listctrl_mc.InsertColumn(1, "Title")
        self.listctrl_mc.InsertColumn(2, "Player")
        
        btn = wx.Button(panel, -1, "Add Line")
        btn.Bind(wx.EVT_BUTTON, self.AddLine)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.listctrl_mc, 0, wx.ALL|wx.EXPAND, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)
        
    def AddLine(self, event):
        if os.path.exists(mp3folder):
            fs = glob.glob(mp3folder+"\\*.mp3")
            
            for f in fs:
                line = "%s"%self.index
                self.listctrl_mc.InsertStringItem(self.index, line)
                self.listctrl_mc.SetStringItem(self.index, 1, os.path.basename(f).decode("cp936").encode("utf8") )
                self.listctrl_mc.SetStringItem(self.index, 2, "USA")
                self.index += 1
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = Mp3Frame(None, -1)
    frame.Show()
    app.MainLoop()