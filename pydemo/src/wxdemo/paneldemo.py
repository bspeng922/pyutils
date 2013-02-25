import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "test panel, size=(600,300)")
        panel = wx.Panel(self)
        button = wx.Button(panel, label="close", pos=(150,60), size=(100,60))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        
    def OnCloseMe(self, event):
        self.Close(True)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()