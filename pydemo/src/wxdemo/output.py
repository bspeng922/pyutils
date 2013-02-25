#-*- coding : cp936 -*-

import sys
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        print "Frame�����ʼ��  frame __init__"
        wx.Frame.__init__(self, parent, id, title)
        
class MyApp(wx.App):
    def __init__(self, redirect=True, filename=None):
        print "App Init"
        wx.App.__init__(self, redirect, filename)
    
    def OnInit(self):
        print "app object oninit"
        self.frame = MyFrame(parent=None, id=-1, title="����wx����ض���")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        
        print >> sys.stderr, "�������׼�������̨"
        return True
    
    def OnExit(self):
        print "app ���� onexit"
        
def main():
    app = MyApp(redirect=True)
    print "begin mainloop"
    app.MainLoop()
    print "after mainloop"
    
if __name__ == "__main__":
    main()