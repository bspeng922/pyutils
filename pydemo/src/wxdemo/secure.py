import wx
import random

debug = True

class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Validate Frame", size=(300,400), style=wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU)
        #self.SetMaxSize(wx.Size(300,400))
        #self.SetMinSize(wx.Size(300,400))
        
        self.panel = wx.Panel(self)
        
        self.label_random = wx.StaticText(self.panel, -1, self.randcode(), pos=(70, 20))
        self.label_random.SetForegroundColour("Red")
        self.label_random.SetFont(wx.Font(28,wx.DEFAULT,wx.NORMAL, wx.BOLD))
        
        
        '''set time out'''
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.ontimeout, self.timer)
        self.timer.Start(6000)

        self.label_validate = wx.StaticText(self.panel,-1, "Input Your Code",pos=(70, 200))
        self.label_validate.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD))
        
        self.txtctrl_validate = wx.TextCtrl(self.panel, -1, "", pos=(90, 240)) 
        
        self.btn_commit = wx.Button(self.panel, -1, "Validate", pos=(100,270))
        self.Bind(wx.EVT_BUTTON, self.OnBtnClick, self.btn_commit)
        
        self.Label_result = wx.StaticText(self.panel,-1, "",pos=(100, 330))
        self.Label_result.SetForegroundColour("Red")
        
    def OnBtnClick(self, event):
        mycode = self.txtctrl_validate.GetValue()
        if debug : print "Mycode: %s"%mycode
        
        if mycode == self.label_random.GetLabel():
            if debug : print "Ok"
            self.timer.Stop()
            msgbox = wx.MessageDialog(None, "Validate OK !", "Result", wx.OK | wx.ICON_INFORMATION)
            if msgbox.ShowModal() == wx.ID_OK:
                self.Close()
            msgbox.Destroy()
        else:
            if debug : print "No compare"
            self.Label_result.SetLabel("Not compare !")
        
    def randcode(self):
        return str(random.randint(100000,999999))
    
    def ontimeout(self, event):
        self.label_random.SetLabel(self.randcode())
        self.Refresh()


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame(None, -1)
    frame.Show()
    app.MainLoop()