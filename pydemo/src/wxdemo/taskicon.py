import wx

class TaskBarIcon(wx.TaskBarIcon):
    id_about = wx.NewId()
    id_minshow = wx.NewId()
    id_maxshow = wx.NewId()
    id_closeshow = wx.NewId()
    
    def __init__(self, frame):
        wx.TaskBarIcon.__init__(self)
        self.frame = frame
        
        self.SetIcon(wx.Icon(name="secure.ico", type=wx.BITMAP_TYPE_ICO), "System demo")
        
        self.Bind(wx.EVT_MENU, self.OnAbout, id=self.id_about)
        self.Bind(wx.EVT_MENU, self.OnMinShow, id=self.id_minshow)
        self.Bind(wx.EVT_MENU, self.OnMaxShow, id=self.id_maxshow)
        self.Bind(wx.EVT_MENU, self.OnCloseShow, id=self.id_closeshow)
        
        self.Bind(wx.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDClick)
        
    def OnTaskBarLeftDClick(self,event):
        if self.frame.IsIconized() : 
            self.frame.Iconize(False)
        if not self.frame.IsShown():
            self.frame.Show(True)
            
        self.frame.Raise()
        
    def OnAbout(self, event):
        wx.MessageBox("This is a wxpython demo .","About")
        
    def OnMinShow(self, event):
        self.frame.Iconize()
        
    def OnMaxShow(self, event):
        self.OnTaskBarLeftDClick()
        self.frame.Maximize(True)
        
    def OnCloseShow(self,event):
        self.frame.Close(True)
        
    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(self.id_minshow, "Mini")
        menu.Append(self.id_maxshow, "Max")
        menu.Append(self.id_about, "About")
        menu.Append(self.id_closeshow, "Close")
        
        return menu
        

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Mini size", (300,400))
        self.SetIcon(wx.Icon("secure.ico", wx.BITMAP_TYPE_ICO))
        
        panel = wx.Panel(self)
        statictext = wx.StaticText(panel, -1, "Hello world", (50,30))
        
        self.taskbaricon = TaskBarIcon(self)
        
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_ICONIZE, self.OnIconfiy)
        
    def OnClose(self, event):
        self.taskbaricon.Destroy()
        self.Destroy()
        
    def OnIconfiy(self, event):
        self.Hide()
        event.Skip()
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(None, -1)
    frame.Show()
    app.MainLoop()