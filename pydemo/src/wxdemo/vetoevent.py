import wx

class Example(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "")
        self.Center()
        self.InitUI()
    
    def InitUI(self):
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
    def OnCloseWindow(self, event):
        dlg = wx.MessageDialog(None, "Are you want to quit ?","Question",wx.YES_NO|wx.NO_DEFAULT|wx.ICON_QUESTION)
        
        if dlg.ShowModal() == wx.ID_YES:
            self.Destroy()
        else:
#            event.Skip()
            event.Veto()    #Sometimes we need to stop processing an event. To do this, we call the method Veto().
            

if __name__ == "__main__":
    app = wx.App()
    Example(None, -1).Show()
    app.MainLoop()
      
        