import wx

class MyPanel(wx.Panel):
    def __init__(self, *args, **kw):
        wx.Panel.__init__(self, *args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        
    def OnButtonClicked(self, event):
        print "event reached panel class"
        event.Skip()
        
class MyButton(wx.Button):
    def __init__(self, *args, **kw):
        wx.Button.__init__(self, *args, **kw)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked)
        
    def OnButtonClicked(self, event):
        print "event reached button class"
        event.Skip()
        
class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        mpnl = MyPanel(self)
        mybtn = MyButton(mpnl, label="OK", pos=(15, 15))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick)
        
    def OnButtonClick(self, event):
        print "event reached from class"
        #event.Skip()


if __name__ == "__main__":
    app = wx.PySimpleApp()
    #If we provide -1 or wx.ID_ANY for the id parameter, we let the wxPython automatically create an id for us.
    Example(None, -1, "hello").Show()    
    app.MainLoop()
    
#    when we click on the button. The event travels from the button to the panel and to the frame.