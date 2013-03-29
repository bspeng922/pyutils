import wx

class Example(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "", size=(320,130))
        self.InitUI()
        
    def InitUI(self):
        panel = wx.Panel(self)
        
        text = wx.StaticText(panel, label="Rename To")
        tc = wx.TextCtrl(panel)
        btnok = wx.Button(panel, label="OK", size=(90,28))
        btnclose = wx.Button(panel, label="Close", size=(90,28))
        
        sizer = wx.GridBagSizer(4,4)
        
        sizer.Add(text, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(tc, pos=(1,0), span=(1,5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        sizer.Add(btnok, pos=(3,3))
        sizer.Add(btnclose, pos=(3,4), flag=wx.RIGHT|wx.BOTTOM, border=5)
        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        
        panel.SetSizer(sizer)
        
if __name__ == "__main__":
    app = wx.App()
    Example(None, -1).Show()
    app.MainLoop()
