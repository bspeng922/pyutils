import wx
import wx.html as html

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        toolbar = self.CreateToolBar()
        toolbar.AddLabelTool(1, "Exit", wx.Bitmap("convert.ico"))
        toolbar.AddLabelTool(2, "Help", wx.Bitmap("secure.ico"))
        toolbar.Realize()
        
        self.splitter = wx.SplitterWindow(self, -1)
        
        self.panelleft = wx.Panel(self.splitter, -1, style=wx.BORDER_SUNKEN)
        self.panelright = wx.Panel(self.splitter, -1)
        
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        header = wx.Panel(self.panelright, -1, size=(-1,20))
        header.SetBackgroundColour("#6f6a59")
        header.SetForegroundColour("White")
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        st = wx.StaticText(header, -1, "Help", (5,5))
        font = st.GetFont()
        font.SetPointSize(9)
        st.SetFont(font)
        hbox.Add(st, 1, wx.TOP|wx.BOTTOM|wx.LEFT, 5)
        
        close = wx.BitmapButton(header, -1, wx.Bitmap("convert.ico", wx.BITMAP_TYPE_ICO), style=wx.NO_BORDER)
        close.SetBackgroundColour("#6f6a59")
        hbox.Add(close, 0)
        header.SetSizer(hbox)
        
        vbox2.Add(header, 0, wx.EXPAND)
        help = html.HtmlWindow(self.panelright, -1, style=wx.NO_BORDER)
        help.LoadPage("help.html")
        vbox2.Add(help, 1, wx.EXPAND)
        self.panelright.SetSizer(vbox2)
        self.panelleft.SetFocus()
        
        self.splitter.SplitVertically(self.panelleft, self.panelright)
        self.splitter.Unsplit()
        
        self.Bind(wx.EVT_BUTTON, self.CloseHelp, id=close.GetId())
        self.Bind(wx.EVT_TOOL, self.OnClose, id=1)
        self.Bind(wx.EVT_TOOL, self.OnHelp, id=2)
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)
        self.CreateStatusBar()
        
    def OnClose(self, event):
        self.Close()
        
    def OnHelp(self, event):
        self.splitter.SplitVertically(self.panelleft, self.panelright)
        self.panelleft.SetFocus()
        
    def CloseHelp(self, event):
        self.splitter.Unsplit()
        self.panelleft.SetFocus()
        
    def OnKeyPressed(self, event):
        keycode = event.GetKeyCode()
        
        if keycode == wx.WXK_F1:
            self.splitter.SplitVertically(self.panelleft, self.panelright)
            self.panelleft.SetFocus()
            
                            
if __name__ == "__main__":
    app = wx.PySimpleApp()
    Example(None, -1, "Listbox").Show()
    app.MainLoop()
        
