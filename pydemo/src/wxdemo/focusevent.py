import wx

#The wx.EVT_SET_FOCUS event, which is generated when a widget receives focus. 
#The wx.EVT_KILL_FOCUS is generated, when the widget looses focus. 

class MyWindow(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.color = "green"
        
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)
        
    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(self.color))
        x,y = self.GetSize()
        dc.DrawRectangle(0,0,x,y)
        
    def OnSize(self, e):
        self.Refresh()
        
    def OnSetFocus(self, e):
        self.color = "red"
        self.Refresh()
        
    def OnKillFocus(self, e):
        self.color = "blue"
        self.Refresh()
        
class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        grid = wx.GridSizer(2,2,10,10)
        grid.AddMany([(MyWindow(self),0,wx.EXPAND|wx.TOP|wx.LEFT, 5),
                      (MyWindow(self),0,wx.EXPAND|wx.TOP|wx.RIGHT, 5),
                      (MyWindow(self),0,wx.EXPAND|wx.BOTTOM|wx.LEFT, 5),
                      (MyWindow(self),0,wx.EXPAND|wx.BOTTOM|wx.RIGHT, 5),
                      ])
        
        self.SetSizer(grid)
        
    def OnMove(self, e):
        print e.GetEventObject()
        x,y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    #If we provide -1 or wx.ID_ANY for the id parameter, we let the wxPython automatically create an id for us.
    Example(None, -1, "hello").Show()    
    app.MainLoop()
        