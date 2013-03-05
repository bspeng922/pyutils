import wx
import os
import cPickle

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
        wx.Frame.__init__(self, parent, id, "Painter", size=(600,300))
        self.paint = PaintWindow(self, -1)
        
        self.paint.Bind(wx.EVT_MOTION, self.OnPaintMotion)
        self.InitStatusBar()
        
        self.CreateMenuBar()
        self.filename =""
        
    def InitStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-3,-2,-1])
        
    def OnPaintMotion(self, event):
        self.statusbar.SetStatusText("Mouse Position: %s"%str(event.GetPositionTuple()), 0)
        self.statusbar.SetStatusText("Line length: %s"%len(self.paint.curLine), 1)
        self.statusbar.SetStatusText("Line Count: %s"%len(self.paint.lines), 2)
        
        event.Skip()
    
    def MenuData(self):
        return [("&File",(
                          ("&New","New paint file", self.OnNew),
                          ("&Open","Open paint file", self.OnOpen),
                          ("&Save","Save paint file", self.OnSave),
                          ("","",""),
                          ("&Color",(
                                     ("&Black","", self.OnColor, wx.ITEM_RADIO),
                                     ("&Red","",self.OnColor, wx.ITEM_RADIO),
                                     ("&Green","",self.OnColor, wx.ITEM_RADIO),
                                     ("&Blue","",self.OnColor, wx.ITEM_RADIO),
                                     ("","","", wx.ITEM_SEPARATOR),
                                     ("&Others","",self.OnOtherColor, wx.ITEM_NORMAL)
                                     )),
                          ("","",""),
                          ("&Quit","quit program", self.OnCloseWindow)                          
                          ))
                ]
        
    def CreateMenuBar(self):
        menuBar = wx.MenuBar()
        for eachMenuData in self.MenuData():
            menuLabel = eachMenuData[0]
            menuItems = eachMenuData[1]
            menuBar.Append(self.CreateMenu(menuItems), menuLabel)
        self.SetMenuBar(menuBar)
        
    def CreateMenu(self, menuData):
        menu = wx.Menu()
        for eachItem in menuData:
            if len(eachItem) == 2:
                label = eachItem[0]
                subMenu = self.CreateMenu(eachItem[1])
                menu.AppendMenu(wx.NewId(),label, subMenu)
            else:
                self.CreateMenuItem(menu, *eachItem)
        return menu
    
    def CreateMenuItem(self, menu, label, status, handler, kind=wx.ITEM_NORMAL):
        if not label:
            menu.AppendSeparator()
            return
        menuItem = menu.Append(-1, label, status, kind)
        self.Bind(wx.EVT_MENU, handler, menuItem)
        
    def OnNew(self, event):
        pass
    
    def OnOpen(self, event):
        file_wildcard = "Paint files(*.paint)|*.paint|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "Open paint file...", os.getcwd(), style=wx.OPEN, wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetPath()
            self.ReadFile()
            self.SetTitle(self.Title+" -- "+self.filename)
        dlg.Destroy()
        
    def ReadFile(self):
        if self.filename:
            try:
                f = open(self.filename,"r")
                data = cPickle.load(f)
                f.close()
                self.paint.SetLinesData(data)
            except cPickle.UnpicklingError:
                wx.MessageBox("%s is not a paint file ."%self.filename, "Error tips", style=wx.OK | wx.ICON_EXCLAMATION)
    
    def OnSave(self, event):
        if not self.filename:
            self.OnSaveAs(event)
        else:
            self.SaveCurFile()
            
    def OnSaveAs(self, event):
        file_wildcard = "Paint files(*.paint)|*.paint|Image files(*.jpg)|*.jpg|All files(*.*)|*.*"
        dlg = wx.FileDialog(self, "save paint as ...", os.getcwd(), style=wx.SAVE|wx.OVERWRITE_PROMPT, wildcard=file_wildcard)
        if dlg.ShowModal() == wx.ID_OK:
            filename = dlg.GetPath()
            if not os.path.splitext(filename[1]):
                #filename += ".paint"
                filename += ".jpg"
            self.filename = filename
            #self.SaveCurFile()
            self.SaveAsImageFile()
            self.SetTitle(self.Title + " -- " + self.filename)
        dlg.Destroy()
        
    def SaveCurFile(self):
        if self.filename:
            data = self.paint.GetLinesData()
            f = open(self.filename, "w")
            cPickle.dump(data, f)
            f.close
            
    def SaveAsImageFile(self):
        if self.filename:
            #self.showbmp = wx.StaticBitmap(self)
            img = self.paint.get.GetBitmap()
            img.SaveFile(self.filename, wx.BITMAP_TYPE_JPEG)
    
    def OnColor(self, event):
        menubar = self.GetMenuBar()
        itemid = event.GetId()
        item = menubar.FindItemById(itemid)
        color = item.GetLabel()
        self.paint.SetColor(color)
        
    def OnOtherColor(self, event):
        dlg = wx.ColourDialog(self)
        dlg.GetColourData().SetChooseFull(True)
        if dlg.ShowModal() == wx.ID_OK:
            self.paint.SetColor(dlg.GetColourData().GetColour())
        dlg.Destroy()
        
    def OnCloseWindow(self, event):
        self.Destroy()    
        

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = PaintFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()