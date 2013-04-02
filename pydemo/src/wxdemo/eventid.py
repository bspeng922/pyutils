import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        pnl = wx.Panel(self)
        exitbtn = wx.Button(pnl, wx.ID_ANY, "exit",(10,10))
        self.Bind(wx.EVT_BUTTON, self.OnExit, id=exitbtn.GetId())
        
    def OnExit(self, event):
        self.Close()
    
if __name__ == "__main__":
    app = wx.PySimpleApp()
    #If we provide -1 or wx.ID_ANY for the id parameter, we let the wxPython automatically create an id for us.
    Example(None, -1, "hello").Show()    
    app.MainLoop()