import wx
import locale

ID_SORT = 1

words = [u'Sund', u'S\xe4bel', u'S\xfcnde', u'Schl\xe4fe', u'Sabotage']

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        panel = wx.Panel(self)
        
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.listbox = wx.ListBox(panel)
        
        for i in words:
            self.listbox.Append(i)
            
        hbox.Add(self.listbox, 1, wx.EXPAND|wx.ALL, 20)
        
        btnpanel = wx.Panel(panel)
        vbox = wx.BoxSizer(wx.VERTICAL)
        new = wx.Button(btnpanel, ID_SORT, "Sort", size=(90,30))
        
        self.Bind(wx.EVT_BUTTON, self.OnSort, id=ID_SORT)
        
        vbox.Add((-1,20))
        vbox.Add(new)
        
        btnpanel.SetSizer(vbox)
        hbox.Add(btnpanel, 0.6, wx.EXPAND|wx.RIGHT, 20)
        panel.SetSizer(hbox)
        
#        locale.setlocale(locale.LC_COLLATE, ("de_DE", "UTF8"))
        locale.setlocale(locale.LC_COLLATE, "")
        
    def OnSort(self, event):
        self.listbox.Clear()
        words.sort(lambda a, b: locale.strcoll(a, b))
        for i in words:
            self.listbox.Append(i)
                         
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()   
        
