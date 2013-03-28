import wx

class Example(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        self.count = 5
        
        self.toolbar = self.CreateToolBar()
        undo = self.toolbar.AddLabelTool(wx.ID_UNDO,"",wx.Bitmap("convert.ico"))
        redo = self.toolbar.AddLabelTool(wx.ID_REDO,"",wx.Bitmap("secure.ico"))
        
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.AddSeparator()
        
        texit = self.toolbar.AddLabelTool(wx.ID_EXIT,"",wx.Bitmap("secure.ico"))
        self.toolbar.Realize()
        
        self.Bind(wx.EVT_TOOL, self.OnUndo, undo)
        self.Bind(wx.EVT_TOOL, self.OnRedo, redo)
        self.Bind(wx.EVT_TOOL, self.OnQuit, texit)
        
    def OnQuit(self, event):
        self.Close()
        
    def OnRedo(self, event):
        if self.count < 5 and self.count >= 1:
            self.count += 1
        
        if self.count == 5:
            self.toolbar.EnableTool(wx.ID_REDO, False)
        
        if self.count == 2:
            self.toolbar.EnableTool(wx.ID_UNDO, True)
            
    def OnUndo(self, event):
        if self.count >1 and self.count <=5:
            self.count -= 1
            
        if self.count == 1:
            self.toolbar.EnableTool(wx.ID_UNDO, False)
            
        if self.count == 4:
            self.toolbar.EnableTool(wx.ID_REDO, True)
            
        
        
if __name__ == "__main__":
    app = wx.App()
    Example(None, -1).Show()
    app.MainLoop()