import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        self.Center()
        self.InitUI()
        
    def InitUI(self):
        pnl = wx.Panel(self)
        
        wx.StaticBox(pnl, label="Personal Info", pos=(5,5), size=(240,70))
        cb = wx.CheckBox(pnl, label="Male", pos=(15,30))
        cb.SetValue(False)

        cb.Bind(wx.EVT_CHECKBOX, self.ShowOrHideTitle)
        wx.CheckBox(pnl, label="Married", pos=(15,55))
        wx.StaticText(pnl, label="Age", pos=(15,95))
        wx.SpinCtrl(pnl, value="1", pos=(55,90),min=1, max=120)
        
        slider = wx.Slider(pnl, -1,6,1,100,(15,130),(200,-1),wx.SL_AUTOTICKS|wx.SL_TOP)
        print slider.GetValue()
        #parent id , default value , min value ,max value ,position, size
        slider.Bind(wx.EVT_SLIDER, self.OnSliderMove)
        
        btn = wx.Button(pnl, label="ok", pos=(90,185), size=(60,-1))
        btn.Bind(wx.EVT_BUTTON, self.OnClose)
        
    def OnClose(self, event):
        self.Destroy()
        
    def ShowOrHideTitle(self, event):
        sender = event.GetEventObject()
        ischecked = sender.GetValue()
        
        
        if ischecked:
            self.SetTitle(sender.GetLabel())
        else:
            self.SetTitle("")
            
    def OnSliderMove(self, event):
        
        self.SetTitle(str(event.GetEventObject().GetValue()))
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = Example(None, -1)
    frame.Show()
    app.MainLoop()
    