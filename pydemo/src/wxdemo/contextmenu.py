import wx

class MyPopupMenu(wx.Menu):
    def __init__(self, parent):
        wx.Menu.__init__(self)
        self.parent = parent
        
        mmi = wx.MenuItem(self, wx.NewId(), "Minize")
        self.AppendItem(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinize, mmi)
        
        cmi = wx.MenuItem(self, wx.NewId(), "Close")
        self.AppendItem(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)
        
    def OnMinize(self, event):
        self.parent.Iconize()
        
    def OnClose(self, event):
        self.parent.Destroy()
        
class Example(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Content Menu")
        self.InitUI()
        
    def InitUI(self):
        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        self.SetSize((250,200))
        self.SetTitle("Context Menu")
        self.Center()
        
    def OnRightDown(self, event):
        #To get the actual mouse position, we call the GetPosition() method of the supplied event object.
        self.PopupMenu(MyPopupMenu(self), event.GetPosition())
        
if __name__ == "__main__":
    app = wx.App()
    Example(None, -1).Show()
    app.MainLoop()