import wx
from wx.lib import sheet

class MySheet(sheet.CSheet):
    def __init__(self, parent):
        sheet.CSheet.__init__(self, parent)
        self.row = self.col = 0
        self.SetNumberRows(55)
        self.SetNumberCols(25)
        
        for i in range(55):
            self.SetRowSize(i, 20)
        
    def OnGridSelectCell(self, event):
        self.row, self.col = event.GetRow(), event.GetCol()
        control = self.GetParent().GetParent().position
        value = self.GetColLabelValue(self.col) + self.GetRowLabelValue(self.row)
        control.SetValue(value)
        event.Skip()
        
    

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        fonts = ['Times New Roman', 'Times', 'Courier', 'Courier New', 'Helvetica',
                'Sans', 'verdana', 'utkal', 'aakar', 'Arial']
        font_sizes = ['10', '11', '12', '14', '16']
        
        box = wx.BoxSizer(wx.VERTICAL)
        self.SetMenuBar(self.InitMenu())
        
        toolbar1 = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL)
        toolbar1.Realize()
        toolbar2 = wx.ToolBar(self, wx.TB_HORIZONTAL|wx.TB_TEXT)
        self.position = wx.TextCtrl(toolbar2)
        font = wx.ComboBox(toolbar2, -1, value="Times", choices=fonts, size=(100,-1))
        font_height = wx.ComboBox(toolbar2, -1, value="10", choices=font_sizes, size=(50,-1), style=wx.CB_DROPDOWN)
        toolbar2.AddControl(self.position)
        toolbar2.AddSeparator()
        toolbar2.AddControl(font)
        toolbar2.AddControl(font_height)
        
        box.Add(toolbar1, border=5)
        box.Add((5,5), 0)
        box.Add(toolbar2)
        box.Add((5,10),0)
        
        toolbar2.Realize()
        self.SetSizer(box)
        
        notebook = wx.Notebook(self, -1, style=wx.RIGHT)
        sheet1 = MySheet(notebook)
        sheet2 = MySheet(notebook)
        sheet3 = MySheet(notebook)
        sheet1.SetFocus()
        
        notebook.AddPage(sheet1, "Sheet1")
        notebook.AddPage(sheet2, "Sheet2")
        notebook.AddPage(sheet3, "Sheet3")
        
        box.Add(notebook,1 , wx.EXPAND)
        
        self.CreateStatusBar()
        
    def InitMenu(self):
        filemenu = wx.Menu()
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

        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()            
        