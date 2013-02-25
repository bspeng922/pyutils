#-*- coding : cp936 -*-

import sys
import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        print "Frame对象初始化  frame __init__"
        wx.Frame.__init__(self, parent, id, title)
        
class MyApp(wx.App):
    def __init__(self, redirect=True, filename=None):
        print "App Init"
        wx.App.__init__(self, redirect, filename)
    
    def OnInit(self):
        print "app object oninit"
        self.frame = MyFrame(parent=None, id=-1, title="测试wx输出重定向")
        self.frame.Show()
        self.SetTopWindow(self.frame)
        
        print >> sys.stderr, "输出到标准错误控制台"
        return True
    
    def OnExit(self):
        print "app 对象 onexit"
        
def main():
    app = MyApp(redirect=True)
    print "begin mainloop"
    app.MainLoop()
    print "after mainloop"
    
if __name__ == "__main__":
    main()