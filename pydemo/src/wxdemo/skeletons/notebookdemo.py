import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        
        panel1 = wx.Panel(self)
        sc = wx.StaticText(panel1, -1, "No Label", pos=(10,20))
        panel2 = wx.Panel(self)
        tc = wx.TextCtrl(panel2, -1, "OK", pos=(10,50))
        
        #notebook = wx.Notebook(self, -1, style=wx.RIGHT)
        
        panel1.SetFocus()
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()            
