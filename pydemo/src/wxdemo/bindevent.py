import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "test panel", size=(600,300))
        self.panel = wx.Panel(self)
        self.button = wx.Button(self.panel, label="Click Me", pos=(150,60), size=(300,60))
        
        #self.Bind(wx.EVT_BUTTON, self.OnClickMe, self.button)
#        self.button.Bind(wx.EVT_ENTER_WINDOW, self.OnEnterWindows)
#        self.button.Bind(wx.EVT_LEAVE_WINDOW, self.OnLeaveWindows)
        self.button.Bind(wx.EVT_LEFT_DOWN, self.OnEnterWindows)
        self.button.Bind(wx.EVT_LEFT_UP, self.OnLeaveWindows)
        
    def OnClickMe(self, event):
        self.panel.SetBackgroundColour('Blue')
        self.panel.Refresh()
        
    def OnEnterWindows(self, event):
        self.panel.SetBackgroundColour("Red")
        self.panel.Refresh()
        self.button.SetLabel("on me")
        event.Skip()
        
    def OnLeaveWindows(self, event):
        self.panel.SetBackgroundColour("green")
        self.panel.Refresh()
        self.button.SetLabel("leave me")
        event.Skip()
  
  
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()      