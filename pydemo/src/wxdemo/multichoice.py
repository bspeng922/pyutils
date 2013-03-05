import wx

class MyFrame(wx.Frame):
    def __init__(self,parent, id):
        wx.Frame.__init__(self, parent,id, "No title", size=(600,300))
        panel = wx.Panel(self)
        btn = wx.Button(panel, label="Close Me",pos=(150,160),size=(100,60))
        self.Bind(wx.EVT_BUTTON, self.OnClickMe, btn)
        
    def OnClickMe(self, event):
        mtdlg = wx.MultiChoiceDialog(None, "choose your fruit","choise title",['tomato','banana','apple','orange'])
        mtdlg.SetSelections([1])    #default choice
        
        if mtdlg.ShowModal() == wx.ID_OK:
            message = mtdlg.GetSelections()
            print message    #[2, 3]
            
#            infodlg = wx.MessageDialog(None, message,"no title", wx.ID_OK | wx.ICON_INFORMATION)
#            if infodlg.ShowModal() == wx.ID_OK:
#                self.Close(True)
#            infodlg.Destroy()
        mtdlg.Destroy()
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()

