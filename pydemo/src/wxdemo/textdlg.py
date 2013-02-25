import wx

class MyFrame(wx.Frame):
    def __init__(self,parent, id):
        wx.Frame.__init__(self, parent, id, "Test panel", size=(600,300))
        panel = wx.Panel(self)
        button = wx.Button(panel, label="close", pos=(150,60), size=(100,60))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        
    def OnCloseMe(self, event):
        dlg = wx.TextEntryDialog(None, "Please input text","title","default")
        if dlg.ShowModal() == wx.ID_OK:
            message = dlg.GetValue()
            dlg_tip  = wx.MessageDialog(None, message, "title", wx.OK | wx.ICON_INFORMATION)
            
            if dlg_tip.ShowModal() == wx.ID_OK:
                self.Close(True)
            dlg_tip.Destroy()
        dlg.Destroy()
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()