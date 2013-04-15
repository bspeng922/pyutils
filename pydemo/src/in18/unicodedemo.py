import wx

text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\
\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439 \n\
\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Bind(wx.EVT_PAINT, self.OnPaintDown)
        
    def OnPaintDown(self, event):
        dc = wx.PaintDC(self)
        dc.DrawText(text, 50,50)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()