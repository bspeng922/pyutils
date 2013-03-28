import wx
import wx.lib.mixins.listctrl as listmix

musicdata = {
0 : ("Bad English", "The Price Of Love", "Rock"),
1 : ("DNA featuring Suzanne Vega", "Tom's Diner", "Rock"),
2 : ("George Michael", "Praying For Time", "Rock"),
3 : ("Gloria Estefan", "Here We Are", "Rock"),
4 : ("Linda Ronstadt", "Don't Know Much", "Rock"),
5 : ("Michael Bolton", "How Am I Supposed To Live Without You", "Blues"),
6 : ("Paul Young", "Oh Girl", "Rock"),
}

class TestListCtrl(wx.ListCtrl):
    def __init__(self, parent, ID=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.DefaultSize, style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        
class TestListCtrlPanel(wx.Panel, listmix.ColumnSorterMixin):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)
        self.index = 0
        
        #no need TestListCtrl
        self.listctrl = wx.ListCtrl(self, size=(-1,100),style=wx.LC_REPORT|wx.BORDER_SUNKEN|wx.LC_SORT_ASCENDING)
        self.listctrl.InsertColumn(0,"Artist")
        self.listctrl.InsertColumn(1,"Title", wx.LIST_FORMAT_RIGHT)
        self.listctrl.InsertColumn(2,"Genre")
        
        items = musicdata.items()
        index=0
        for key, data in items:
            self.listctrl.InsertStringItem(index, data[0])
            self.listctrl.SetStringItem(index, 1, data[1])
            self.listctrl.SetStringItem(index, 2, data[2])
            self.listctrl.SetItemData(index, key)
            index += 1
            
        self.itemDataMap = musicdata
        listmix.ColumnSorterMixin.__init__(self, 3)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnColClick, self.listctrl)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.listctrl, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer)
        
    def GetListCtrl(self):
        return self.listctrl
    
    def OnColClick(self, event):
        print "colum clicked"
        event.Skip()
        
class MyForm(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "List Control turorial")
        panel = TestListCtrlPanel(self)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = MyForm(None, -1)
    frame.Show()
    app.MainLoop()
    