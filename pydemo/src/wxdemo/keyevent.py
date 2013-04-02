import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        pnl = wx.Panel(self)
        pnl.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        pnl.SetFocus()
        
    def OnKeyDown(self, event):
        key = event.GetKeyCode()
        
        if key == wx.WXK_ESCAPE:
            dlg = wx.MessageDialog(None, "Are you sure to quit?","Question",wx.YES_NO|wx.NO_DEFAULT)
            
            if dlg.ShowModal() == wx.YES:
                self.Destory()
            
            
if __name__ == "__main__":
    app = wx.PySimpleApp()
    #If we provide -1 or wx.ID_ANY for the id parameter, we let the wxPython automatically create an id for us.
    Example(None, -1, "hello").Show()    
    app.MainLoop()