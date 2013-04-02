import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        wx.FutureCall(5000, self.ShowMessage)
        
    def ShowMessage(self):
        wx.MessageBox("Download complete","info", wx.OK|wx.ICON_INFORMATION)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    #If we provide -1 or wx.ID_ANY for the id parameter, we let the wxPython automatically create an id for us.
    Example(None, -1, "hello").Show()    
    app.MainLoop()
        