import wx

rw = 701
rm = 10
rh = 60

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.SetSize((rw+2*rm, 60))
        self.SetWindowStyle(wx.FRAME_NO_TASKBAR|wx.NO_BORDER|wx.STAY_ON_TOP)
        
        self.font = wx.Font(7, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier 10 pitch")
        
        self.Bind(wx.EVT_PAINT, self.OnPaintWindow)
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.Bind(wx.EVT_MOTION, self.OnMouseMove)
        
        self.Center()
        #self.SetTransparent(80)
        
    def OnPaintWindow(self, event):
        dc = wx.PaintDC(self)
        
        brush = wx.BrushFromBitmap(wx.Bitmap("../convert.ico"))
        dc.SetBrush(brush)
        dc.DrawRectangle(0,0,rw+2*rm, rh)
        dc.SetFont(self.font)
        
        dc.SetPen(wx.Pen("#f8ff25"))
        dc.SetTextForeground("#f8ff25")
        
        for i in range(rw):
            if not(i % 100):
                dc.DrawLine(i+rm, 0, i+rm, 10)
                w, h = dc.GetTextExtent(str(i))
                dc.DrawText(str(i), i+rm-w/2, 11)
            elif not(i%20):
                dc.DrawLine(i+rm, 0, i+rm, 8)
            elif not (i%2):
                dc.DrawLine(i+rm, 0, i+rm ,4)
                
    def OnLeftDown(self, event):
        pos = event.GetPosition()
        x, y = self.ClientToScreen(event.GetPosition())
        ox, oy = self.GetPosition()
        dx = x - ox
        dy = y - oy
        self.delta = ((dx, dy))
        
    def OnMouseMove(self, event):
        if event.Dragging() and event.LeftIsDown():
            x, y = self.ClientToScreen(event.GetPosition())
            fp = (x-self.delta[0], y-self.delta[1])
            self.Move(fp)
            
    def OnRightDown(self, event):
        self.Close()
        
    
if __name__ == "__main__":
    app = wx.PySimpleApp()
    Example(None, -1, "Music Player").Show()
    app.MainLoop()

        