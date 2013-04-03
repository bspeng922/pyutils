import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        pnl = wx.Panel(self)
        
        self.rb1 = wx.RadioButton(pnl, label="Value1", pos=(10,10))
        self.rb2 = wx.RadioButton(pnl, label="Value2", pos=(10,30))
        self.rb3 = wx.RadioButton(pnl, label="Value3", pos=(10,50))
        
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, self.rb1)
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, self.rb2)
        self.Bind(wx.EVT_RADIOBUTTON, self.SetVal, self.rb3)
        
        distros = ['ubuntu','arch','fedora','debian','mint']
        cb = wx.ComboBox(pnl, pos=(10,100), choices=distros, style=wx.CB_READONLY)
        
        self.st = wx.StaticText(pnl, label="", pos=(10,140))
        cb.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        
        self.sb = self.CreateStatusBar(3)
        
    def OnSelect(self, event):
        self.st.SetLabel(event.GetString())
        
    def SetVal(self, event):
        self.sb.SetStatusText(str(self.rb1.GetValue()), 0)
        self.sb.SetStatusText(str(self.rb2.GetValue()), 1)
        self.sb.SetStatusText(str(self.rb3.GetValue()), 2)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = Example(None, -1)
    frame.Show()
    app.MainLoop()