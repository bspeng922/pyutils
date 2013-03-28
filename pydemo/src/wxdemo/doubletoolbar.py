import wx

class Example(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "No title")
        self.Center()
        self.InitUI()
    
    def InitUI(self):
        toolbar1 = wx.ToolBar(self)
        toolbar1.AddLabelTool(wx.ID_ANY, "", wx.Bitmap("convert.ico"))
        toolbar1.Realize()
        
        toolbar2 = wx.ToolBar(self)
        toolbar2.AddLabelTool(wx.ID_ANY, "", wx.Bitmap("secure.ico"))
        toolbar2.Realize()
        
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(toolbar1, 0, wx.EXPAND)
        vbox.Add((-1,5))
        vbox.Add(toolbar2, 0, wx.EXPAND)
        self.SetSizer(vbox)
        
        

if __name__ == "__main__":
    app = wx.App()
    Example(None, -1).Show()
    app.MainLoop()