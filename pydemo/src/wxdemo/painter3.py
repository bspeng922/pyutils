import wx
import os
import cPickle
import wx.lib.buttons

class PaintWindow(wx.Window):
    def __init__(self, parent, id):
        wx.Window.__init__(self, parent, id)
        self.SetBackgroundColour("White")
        self.color= "black"
        self.thickness = 2
        
        #create a pen
        self.pen = wx.Pen(self.color, self.thickness, wx.SOLID)
        self.lines = []
        self.curLine = []
        self.pos = (0,0)
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
        
    def OnLeftDown(self, event):
        self.curLine = []
        self.pos = event.GetPositionTuple()
        self.CaptureMouse()
    
    def OnLeftUp(self, event):
        if self.HasCapture():
            self.lines.append((self.color, self.thickness, self.curLine))
            self.curLine = []
            self.ReleaseMouse()
    
    def OnMotion(self, event):
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
        
    def OnSize(self, event):
        self.reInitBuffer = True
        
    def OnIdle(self, event):
        if self.reInitBuffer:
            self.InitBuffer()
            self.Refresh(False)
            
    def OnPaint(self,event):
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
            
    def GetLinesData(self):
        return self.lines[:]
    
    def SetLinesData(self, lines):
        self.lines = lines[:]
        self.InitBuffer()
        self.Refresh()        
      

class PaintFrame(wx.Frame):
    def __init__(self, parent, id):
        self.title = "My Painter Frame"
        wx.Frame.__init__(self, parent, id, self.title, sizer=(800,600))
        self.paint = PaintWindow(self, -1)
        
        self.paint.Bind(wx.EVT_MOTION, self.OnPaintMotion)
        self.InitStatusBar()        
        self.CreateMenuBar()
        self.filename = ""
        self.CreatePanel()
        
    def CreatePanel(self):
        controlPanel = ControlPanel(self, -1, self.paint)
        
        
class ControlPanel(wx.Panel):
    BMP_SIZE = 16
    BMP_BORDER = 3
    NUM_COLS = 4
    SPACING = 4
    colorList = ('Black', 'Yellow', 'Red', 'Green', 'Blue', 'Purple',  
                 'Brown', 'Aquamarine', 'Forest Green', 'Light Blue',  
                 'Goldenrod', 'Cyan', 'Orange', 'Navy', 'Dark Grey',  
                 'Light Grey')
    maxThickness = 16
    
    def __init__(self, parent, ID, paint):
        wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
        self.paint = paint
        buttonSize = (self.BMP_SIZE+2* self.BMP_BORDER, self.BMP_SIZE+2*self.BMP_BORDER)
        
        

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = PaintFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
