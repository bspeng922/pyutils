import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.SetSize((250,180))
        self.InitUI()
        
    def InitUI(self):
        self.count = 0
        #pnl = wx.Panel(self)
#        grid = wx.GridSizer(3,2)
#        
#        grid.AddMany([(wx.Button(pnl,wx.ID_CANCEL),0,wx.TOP|wx.LEFT, 5),
#                      (wx.Button(pnl,wx.ID_DELETE),0,wx.TOP, 5),
#                      (wx.Button(pnl,wx.ID_SAVE),0,wx.LEFT, 5),
#                      (wx.Button(pnl,wx.ID_EXIT)),
#                      (wx.Button(pnl,wx.ID_STOP),0,wx.LEFT, 5),
#                      (wx.Button(pnl,wx.ID_NEW)),
#                      ])
#
#        self.Bind(wx.EVT_BUTTON, self.OnExit, id=wx.ID_EXIT)
        self.Bind(wx.EVT_PAINT, self.OnRePaint)
#        pnl.SetSizer(grid)
        
    def OnExit(self, event):
        self.Close()
        
    def OnRePaint(self, event):
        self.count += 1
        self.SetTitle(str(self.count))
    
if __name__ == "__main__":
    app = wx.PySimpleApp()
    #If we provide -1 or wx.ID_ANY for the id parameter, we let the wxPython automatically create an id for us.
    Example(None, -1, "hello").Show()    
    app.MainLoop()