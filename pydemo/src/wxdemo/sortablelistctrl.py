import wx
import sys
from wx.lib.mixins.listctrl import ColumnSorterMixin

actresses = {
1 : ('jessica alba', 'pomona', '1981'), 
2 : ('sigourney weaver', 'new york', '1949'),
3 : ('angelina jolie', 'los angeles', '1975'), 
4 : ('natalie portman', 'jerusalem', '1981'),
5 : ('rachel weiss', 'london', '1971'), 
6 : ('scarlett johansson', 'new york', '1984') 
}

class SortedListCtrl(wx.ListCtrl, ColumnSorterMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        
        #The ColumnSorterMixin accepts one argument. It is the number of columns to be sorted.
        ColumnSorterMixin.__init__(self, len(actresses))
        
        #We must map our data to be displayed in a list control to the itemDataMap attribute. 
        #The data must be in a dictionary data type.
        self.itemDataMap = actresses
    
    #We must create a GetListCtrl() method. This method returns the wx.ListCtrl widget that is going to be sorted.    
    def GetListCtrl(self):
        return self
    

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        panel = wx.Panel(self)
        
        self.list = SortedListCtrl(panel)
        self.list.InsertColumn(0,"name",width=140)
        self.list.InsertColumn(0,"place",width=130)
        self.list.InsertColumn(0,"year",wx.LIST_FORMAT_CENTER, 90)
        items = actresses.items()
        
        for key, data in items:
            index = self.list.InsertStringItem(sys.maxint, data[0])
            self.list.SetStringItem(index, 1, data[1])
            self.list.SetStringItem(index, 2, data[2])
            
            #We must assosiate each row with a special index. This is done with the SetItemData method.
            self.list.SetItemData(index, key)
        
        hbox.Add(self.list, 1, wx.EXPAND)
        panel.SetSizer(hbox)

                            
if __name__ == "__main__":
    app = wx.PySimpleApp()
    Example(None, -1, "Listbox").Show()
    app.MainLoop()