#-*- coding:utf-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Test panel", size=(600,300))
        
        panel = wx.Panel(self)
        
        button = wx.Button(panel, label="close", pos=(150,60),size=(100,60))
        
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        
    def OnCloseMe(self, event):
        dlg = wx.MessageDialog(None, "message dialog","title", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
        
