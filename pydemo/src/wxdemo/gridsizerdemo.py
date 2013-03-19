import wx

class Example(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Calculator", size=(300,250))
        
        self.InitUI()
        self.Center()
        
    def InitUI(self):
        menubar = wx.MenuBar()
        filemenu = wx.Menu()
        menubar.Append(filemenu, "&File")
        self.SetMenuBar(menubar)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, style=wx.TE_RIGHT)
        vbox.Add(self.display, flag=wx.EXPAND|wx.TOP|wx.BOTTOM, border=4)
        
        gs = wx.GridSizer(1,4,5,5)
        
        gs.AddMany([(wx.Button(self, label="Cls"),0, wx.EXPAND),
                    (wx.Button(self, label="Bck"),0, wx.EXPAND),
                    (wx.StaticText(self),wx.EXPAND),
                    (wx.Button(self, label="Close"),0, wx.EXPAND),
                    (wx.Button(self, label="7"),0, wx.EXPAND),
                    (wx.Button(self, label="8"),0, wx.EXPAND),
                    (wx.Button(self, label="9"),0, wx.EXPAND),
                    (wx.Button(self, label="/"),0, wx.EXPAND),
                    (wx.Button(self, label="4"),0, wx.EXPAND),
                    (wx.Button(self, label="5"),0, wx.EXPAND),
                    (wx.Button(self, label="6"),0, wx.EXPAND),
                    (wx.Button(self, label="*"),0, wx.EXPAND),
                    (wx.Button(self, label="1"),0, wx.EXPAND),
                    (wx.Button(self, label="2"),0, wx.EXPAND),
                    (wx.Button(self, label="3"),0, wx.EXPAND),
                    (wx.Button(self, label="-"),0, wx.EXPAND),
                    (wx.Button(self, label="0"),0, wx.EXPAND),
                    (wx.Button(self, label="."),0, wx.EXPAND),
                    (wx.Button(self, label="="),0, wx.EXPAND),
                    (wx.Button(self, label="+"),0, wx.EXPAND),
                    ])
        
        vbox.Add(gs, proportion=1, flag=wx.EXPAND)
        
        self.SetSizer(vbox)
        
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = Example(None, -1)
    frame.Show()
    app.MainLoop()