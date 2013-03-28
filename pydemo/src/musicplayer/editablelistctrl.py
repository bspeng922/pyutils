import wx
import wx.lib.mixins.listctrl as listmix

class EditableListCtrl(wx.ListCtrl, listmix.TextEditMixin):
    def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.TextEditMixin.__init__(self)
        
class MyPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        rows = [("Ford", "Taurus", "1996", "Blue"),
                ("Nissan", "370Z", "2010", "Green"),
                ("Porche", "911", "2009", "Red")
                ]
        self.listctrl = EditableListCtrl(self, style=wx.LC_REPORT)
        self.listctrl.InsertColumn(0, "Make")
        self.listctrl.InsertColumn(1, "Model")
        self.listctrl.InsertColumn(2, "Year")
        self.listctrl.InsertColumn(3, "Color")
        
        index = 0
        for row in rows:
            self.listctrl.InsertStringItem(index, row[0])
            self.listctrl.SetStringItem(index, 1, row[1])
            self.listctrl.SetStringItem(index, 2, row[2])
            self.listctrl.SetStringItem(index, 3, row[3])
            index += 1
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.listctrl, 1, wx.ALL|wx.EXPAND, 5)
        self.SetSizer(sizer)
        
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "OK")
        panel = MyPanel(self)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(None, -1)
    frame.Show()
    app.MainLoop()
