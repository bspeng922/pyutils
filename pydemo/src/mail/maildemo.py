import wx

debug = True 

class MailFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "New Mail...", size=(300,400))
        self.panel = wx.Panel(self)
        
        self.Label_to = wx.StaticText(self.panel, -1, "To: ", pos=(5,10))
        self.Label_from = wx.StaticText(self.panel, -1, "From: ", pos=(5,30))
        self.label_subject = wx.StaticText(self.panel, -1, "Subject: ", pos=(5,50))
        self.Label_message = wx.StaticText(self.panel, -1, "Message: ", pos=(5,70))
        self.Label_info = wx.StaticText(self.panel, -1, "", pos=(5,230))
        
        self.txtstrl_to = wx.TextCtrl(self.panel, -1, "", pos=(80,10), size=(200,20))
        self.txtctrl_from = wx.TextCtrl(self.panel, -1, "", pos=(80,30), size=(200,20))
        self.txtctrl_subject = wx.TextCtrl(self.panel, -1, "", pos=(80,50), size=(200,20))
        self.txtctrl_message = wx.TextCtrl(self.panel, -1, "", pos=(80,70), size=(200,80),style=wx.MULTIPLE|wx.TE_RICH2)
        
        self.btn_sendmail = wx.Button(self.panel, -1, "Send Mail", pos=(5,180))
        self.Bind(wx.EVT_BUTTON, self.OnSendClick, self.btn_sendmail)
        
    def OnSendClick(self, event):
        info = self.txtstrl_to.GetValue() , self.txtctrl_from.GetValue(), self.txtctrl_subject.GetValue()
        if debug : print info
        if debug : print self.txtctrl_message.GetValue()
        
        self.Label_info.SetLabel(" ".join(info))
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MailFrame(None, -1)
    frame.Show()
    app.MainLoop()
        
        
