import wx
import wx.html as html

ID_CLOSE = 1
page = '<html><body bgcolor="#8e8e95"><table cellspacing="5" border="0" width="250"> \
<tr width="200" align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;Maximum</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>9000</b></td> \
</tr> \
<tr align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;Mean</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>6076</b></td> \
</tr> \
<tr align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;Minimum</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>3800</b></td> \
</tr> \
<tr align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;Median</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>6000</b></td> \
</tr> \
<tr align="left"> \
<td bgcolor="#e7e7e7">&nbsp;&nbsp;Standard Deviation</td> \
<td bgcolor="#aaaaaa">&nbsp;&nbsp;<b>6076</b></td> \
</tr> \
</body></table></html>'

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        htmlwin = html.HtmlWindow(panel, -1, style=wx.NO_BORDER)
        htmlwin.SetBackgroundColour(wx.RED)
        htmlwin.SetStandardFonts()
        htmlwin.SetPage(page)
        
        vbox.Add((-1,10),0)
        vbox.Add(htmlwin, 1, wx.EXPAND|wx.ALL, 9)
        
        bitmap = wx.StaticBitmap(panel, -1, wx.Bitmap("secure.ico"))
        hbox.Add(bitmap, 1, wx.LEFT|wx.BOTTOM|wx.TOP, 10)
        btnok = wx.Button(panel, ID_CLOSE, 'OK')
        
        self.Bind(wx.EVT_BUTTON, self.OnClose, id=ID_CLOSE)
        
        hbox.Add((100,-1), 1, wx.EXPAND|wx.ALIGN_RIGHT)
        hbox.Add(btnok, flag=wx.TOP|wx.BOTTOM|wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)
        
        panel.SetSizer(vbox)
        
    def OnClose(self, event):
        self.Close()
        
                
if __name__ == "__main__":
    app = wx.PySimpleApp()
    Example(None, -1, "Listbox").Show()
    app.MainLoop()
        