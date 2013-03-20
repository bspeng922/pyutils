import wx

class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
        
    def OnDropFiles(self, x, y, filenames):
        self.window.SetValue(str(filenames[0]))

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "My Frame", size=(400,300))
        self.Center()
        
        panel = wx.Panel(self)
        self.filepath = wx.TextCtrl(panel, -1, "", size=(380,-1))
        droptarget = FileDrop(self.filepath)
        self.filepath.SetDropTarget(droptarget)
        
        self.filepath2 = wx.TextCtrl(panel, -1, "", size=(380,-1), pos=(0,50))
        droptarget = FileDrop(self.filepath2)
        self.filepath2.SetDropTarget(droptarget)



if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(None, -1)
    frame.Show()
    app.MainLoop()