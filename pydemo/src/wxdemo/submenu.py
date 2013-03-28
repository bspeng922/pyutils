import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "This is a aub menu demo")
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        menubar = wx.MenuBar()
        
        fmenu = wx.Menu()
        fmenu.Append(wx.ID_NEW, "&New")
        fmenu.Append(wx.ID_OPEN, "&Open")
        fmenu.Append(wx.ID_SAVE, "&Save")
        fmenu.AppendSeparator()
        
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, "Import newsfeed list...")
        imp.Append(wx.ID_ANY, "Import bookmarks...")
        imp.Append(wx.ID_ANY, "Import mails...")
        
        fmenu.AppendMenu(wx.ID_ANY, "&Import", imp)
        qmi = wx.MenuItem(fmenu, wx.ID_EXIT, "&Quit\tCtrl+Q")
        fmenu.AppendItem(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        menubar.Append(fmenu, "&File")
        self.SetMenuBar(menubar)
        
    def OnQuit(self, event):
        self.Destroy()
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    MyFrame(None, -1).Show()
    app.MainLoop()
        
        