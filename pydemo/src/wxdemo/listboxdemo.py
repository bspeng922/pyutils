import wx

ID_NEW = 1
ID_RENAME = 2
ID_CLEAR = 3
ID_DELETE = 4

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        panel = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        self.listbox = wx.ListBox(panel, -1)
        hbox.Add(self.listbox, 1, wx.EXPAND|wx.ALL, 20)
        
        btnpanel = wx.Panel(panel, -1)
        vbox= wx.BoxSizer(wx.VERTICAL)
        newbtn = wx.Button(btnpanel, ID_NEW, "New", size=(90,30))
        rnbtn = wx.Button(btnpanel, ID_RENAME, "Rename", size=(90,30))
        clrbtn = wx.Button(btnpanel, ID_CLEAR, "Clear", size=(90,30))
        delbtn = wx.Button(btnpanel, ID_DELETE, "Delete", size=(90,30))
        
        self.Bind(wx.EVT_BUTTON, self.NewItem, id=ID_NEW)
        self.Bind(wx.EVT_BUTTON, self.OnRename, id=ID_RENAME)
        self.Bind(wx.EVT_BUTTON, self.OnClear, id=ID_CLEAR)
        self.Bind(wx.EVT_BUTTON, self.OnDelete, id=ID_DELETE)
        self.Bind(wx.EVT_LISTBOX_DCLICK, self.OnRename)
        
        vbox.Add((-1,20))
        vbox.Add(newbtn)
        vbox.Add(rnbtn, 0, wx.TOP, 5)
        vbox.Add(clrbtn, 0, wx.TOP, 5)
        vbox.Add(delbtn, 0, wx.TOP, 5)
        btnpanel.SetSizer(vbox)
        
        hbox.Add(btnpanel, 0.6, wx.EXPAND|wx.RIGHT, 20)
        panel.SetSizer(hbox)
    
    def NewItem(self, event):
        text = wx.GetTextFromUser("Enter a new item","Insert dialog")
        if text != "":
            self.listbox.Append(text)
            
    def OnRename(self, event):
        sel = self.listbox.GetSelection()
        text = self.listbox.GetString(sel)
        renamed = wx.GetTextFromUser("Rename Item","Rename dialog", text)
        
        if renamed != "":
            self.listbox.Delete(sel)
            self.listbox.Insert(renamed, sel)
            
    def OnDelete(self, event):
        sel = self.listbox.GetSelection()
        if sel != -1:
            self.listbox.Delete(sel)
            
    def OnClear(self, event):
        self.listbox.Clear()
        
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    Example(None, -1, "Listbox").Show()
    app.MainLoop()
        
        
        