import wx
import sys
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

packages = [('abiword', '5.8M', 'base'), ('adie', '145k', 'base'),
    ('airsnort', '71k', 'base'), ('ara', '717k', 'base'), ('arc', '139k', 'base'),
    ('asc', '5.8M', 'base'), ('ascii', '74k', 'base'), ('ash', '74k', 'base')]

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT|wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)
        
class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        
        panel = wx.Panel(self)
        
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        leftpanel = wx.Panel(panel)
        rightpanel = wx.Panel(panel)
        
        self.log = wx.TextCtrl(rightpanel, -1, style=wx.TE_MULTILINE)
        self.list = CheckListCtrl(rightpanel)
        self.list.InsertColumn(0, "Package", width=140)
        self.list.InsertColumn(1, "Size")
        self.list.InsertColumn(2, "Repository")
        
        for i in packages:
            index = self.list.InsertStringItem(sys.maxint, i[0])
            self.list.SetStringItem(index,1, i[1])
            self.list.SetStringItem(index,2, i[2])
            
        vbox2 = wx.BoxSizer(wx.VERTICAL)
        sel = wx.Button(leftpanel, -1, "Select All", size=(100,-1))
        des = wx.Button(leftpanel, -1, "Deselect All", size=(100,-1))
        apply = wx.Button(leftpanel, -1, "Apply", size=(100,-1))
        
        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id=sel.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDeSelectAll, id=des.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnApply, id=apply.GetId())
        
        vbox2.Add(sel, 0, wx.TOP, 5)
        vbox2.Add(des)
        vbox2.Add(apply)
        
        leftpanel.SetSizer(vbox2)
        
        vbox.Add(self.list, 1, wx.EXPAND|wx.TOP, 3)
        vbox.Add((-1,10))
        vbox.Add(self.log, 0.5, wx.EXPAND)
        vbox.Add((-1,10))
        
        rightpanel.SetSizer(vbox)
        
        hbox.Add(leftpanel, 0, wx.EXPAND|wx.RIGHT, 5)
        hbox.Add(rightpanel, 1, wx.EXPAND)
        hbox.Add((3,-1))
        
        panel.SetSizer(hbox)
        
    def OnSelectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i)
            
    def OnDeSelectAll(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            self.list.CheckItem(i, False)
            
    def OnApply(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            if i == 0: self.log.Clear()
            if self.list.IsChecked(i):
                self.log.AppendText(self.list.GetItemText(i)+"\n")
                
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()

