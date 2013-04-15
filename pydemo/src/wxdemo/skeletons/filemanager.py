import wx
import os
import time

ID_BUTTON = 100
ID_EXIT = 200
ID_SPLITTER = 300


class MyListCtrl(wx.ListCtrl):
    def __init__(self, parent, id):
        wx.ListCtrl.__init__(self, parent, id, style=wx.LC_REPORT)
        
        files = os.listdir("E:\\soft")
        images = ['../secure.ico','../convert.ico','../secure.ico','../secure.ico','../secure.ico','../secure.ico']
        
        self.InsertColumn(0, "Name")
        self.InsertColumn(1, "Exit")
        self.InsertColumn(2, "Size", wx.LIST_FORMAT_RIGHT)
        self.InsertColumn(3, "Modified")
        
        self.SetColumnWidth(0, 220)
        self.SetColumnWidth(1, 70)
        self.SetColumnWidth(2, 100)
        self.SetColumnWidth(3, 420)
        
        self.il = wx.ImageList(16, 16)
        for i in images:
            self.il.Add(wx.Bitmap(i))
        self.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
        
        j = 1
        self.InsertStringItem(0, "..")
        self.SetItemImage(0, 5)
        
        for i in files:
            (name, ext) = os.path.splitext(i)
            ex = ext[1:]
            #size = os.path.getsize(i)
            size = 10
            sec = time.time()#os.path.getmtime(i)
            
            self.InsertStringItem(j, name)
            self.SetStringItem(j, 1, ex)
            self.SetStringItem(j, 2, str(size)+" B")
            self.SetStringItem(j, 3, time.strftime("%Y-%m-%d %H:%M", time.localtime(sec)))
            
            if os.path.isdir(i):
                self.SetItemImage(j, 1)
            elif ex == "py":
                self.SetItemImage(j, 2)
            elif ex == "jpg":
                self.SetItemImage(j, 3)
            elif ex == "pdf":
                self.SetItemImage(j, 4)
            else:
                self.SetItemImage(j, 0)
                
            if (j % 2):
                self.SetItemBackgroundColour(j, "#e6f1f5")
                
            j += 1    

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        
        self.splitter = wx.SplitterWindow(self, ID_SPLITTER, style=wx.SP_BORDER)
        self.splitter.SetMinimumPaneSize(50)
        
        p1 = MyListCtrl(self.splitter, -1)
        p2 = MyListCtrl(self.splitter, -1)
        self.splitter.SplitVertically(p1, p2)
        
        self.Bind(wx.EVT_SIZE, self.OnSize)
        self.Bind(wx.EVT_SPLITTER_DCLICK, self.OnDoubleClick, id=ID_SPLITTER)
        
        self.SetMenuBar(self.InitMenu())
        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_EXIT)
        
        self.sb = self.CreateStatusBar()
        self.sb.SetStatusText(os.getcwd())
        
        
        
    def InitMenu(self):
        filemenu = wx.Menu()
        filemenu.Append(ID_EXIT, "E&Xit", "Terminate the program")
        editmenu = wx.Menu()
        netmenu = wx.Menu()
        showmenu = wx.Menu()
        configmenu = wx.Menu()
        helpmenu = wx.Menu()
        
        menubar = wx.MenuBar()
        menubar.Append(filemenu, "&File")
        menubar.Append(editmenu, "&Edit")
        menubar.Append(netmenu, "Net")
        menubar.Append(showmenu, "Show")
        menubar.Append(configmenu, "Config")
        menubar.Append(helpmenu, "Help")
        
        return menubar
    
    def OnExit(self, event):
        self.Destroy()
    

    def OnSize(self, event):
        size = self.GetSize()
        self.splitter.SetSashPosition(size.x/2)
        self.sb.SetStatusText(os.getcwd())
        event.Skip()
        
    def OnDoubleClick(self, event):
        size = self.GetSize()
        self.splitter.SetSashPosition(size.x/2)
                    
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()            
