import wx

class Example(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "No title")
        self.InitUI()
        
    def InitUI(self):
        menubar = wx.MenuBar()
        
        fmenu = wx.Menu()
        vmenu = wx.Menu()
        
        self.showsb = vmenu.Append(wx.ID_ANY, "Show statusBar", "Show status bar", kind=wx.ITEM_CHECK)
        self.showtb = vmenu.Append(wx.ID_ANY, "Show Toolbar", "Show tool bar", kind=wx.ITEM_CHECK)
        
        vmenu.Check(self.showsb.GetId(), True)
        vmenu.Check(self.showtb.GetId(), True)
        
        self.Bind(wx.EVT_MENU, self.ToggleStatusbar, self.showsb)
        self.Bind(wx.EVT_MENU, self.ToggleToolbar, self.showtb)
        
        menubar.Append(fmenu, "&File")
        menubar.Append(vmenu, "&View")
        
        self.SetMenuBar(menubar)
        
        self.toolbar = self.CreateToolBar()
        qtool = self.toolbar.AddLabelTool(1,"Quti",wx.Bitmap("convert.ico"))
        self.toolbar.Realize()
        
        self.Bind(wx.EVT_TOOL, self.OnClose, qtool)
        
        
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Ready")
        
    def ToggleStatusbar(self, event):
        if self.showsb.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()
            
    def ToggleToolbar(self, event):
        if self.showtb.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()
            
    def OnClose(self, event):
        self.Destroy()
        
def main():
    app = wx.App()
    Example(None, -1).Show()
    app.MainLoop()        

if __name__ == "__main__":
    main()