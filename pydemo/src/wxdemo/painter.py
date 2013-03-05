import wx

class PaintWindow(wx.Window):
    def __init__(self, parent, id):
        wx.Window.__init__(self, parent, id)
        self.SetBackgroundColour("white")
        self.color="Black"
        self.thickness = 2
        
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
        self.lines = []
        self.curLine = []
        self.pos = (0, 0)
        self.InitBuffer()
        
        self.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP, self.OnLeftUp)
        self.Bind(wx.EVT_MOTION, self.OnMotion)
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_IDLE, self.OnIdle)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        
    def InitBuffer(self):
        size = self.GetClientSize()
        self.buffer = wx.EmptyBitmap(size.width, size.height)
        dc = wx.BufferedDC(None, self.buffer)
        
        dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
        dc.Clear()
        self.DrawLines(dc)
        self.reInitBuffer = False
        
    def GetLinesData(self):
        return self.lines[:]
    
    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()
        
    def OnLeftDown(self, event):
        self.curLine = []
        
        self.pos = event.GetPositionTuple()
        self.CaptureMouse()
        
    def OnLeftUp(self, event):
        if self.HasCapture():
            self.lines.append((self.color, self.thickness, self.curLine))
            self.curLine = []
            self.ReleaseMouse()
            
    def OnMotion(self,event):
        if event.Dragging() and event.LeftIsDown():
            dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
            self.drawMotion(dc, event)
        event.Skip()
        
    def drawMotion(self, dc, event):
        dc.SetPen(self.pen)
        newPos = event.GetPositionTuple()
        coords = self.pos + newPos
        self.curLine.append(coords)
        dc.DrawLine(*coords)
        self.pos = newPos
        
    def OnSize(self,event):
        self.reInitBuffer = True
        
    def OnIdle(self, event):
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)
            
    def OnPaint(self, event):
        dc = wx.BufferedPaintDC(self, self.buffer)
            
    def DrawLines(self, dc):
        for colour, thickness, line in self.lines:
            pen = wx.Pen(colour, thickness, wx.SOLID)
            dc.SetPen(pen)
            for coords in line:
                dc.DrawLine(*coords)
                
    def SetColor(self, color):
        self.color = color
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
        
    def SetThickness(self, num):
        self.thickness = num
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
        
class PaintFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Painter Pad", size=(800,600))
        self.paint = PaintWindow(self, -1)
        
        self.paint.Bind(wx.EVT_MOTION, self.OnPaintMotion)
        self.statusBar = self.CreateStatusBar()
        
        self.statusBar.SetFieldsCount(3)
        self.statusBar.SetStatusWidths([-3,-2,-1])
        
    def OnPaintMotion(self, event):
        self.statusBar.SetStatusText("Mouse postion: "+ str(event.GetPositionTuple()), 0)
        self.statusBar.SetStatusText("Current Line: %s"%len(self.paint.curLine),1)
        self.statusBar.SetStatusText("Line Count: %s"%len(self.paint.lines),2)
        
        event.Skip()
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = PaintFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
    
        
        
        
            
        
        
