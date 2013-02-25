#-*- coding:utf-8 -*-

import wx

class MyFrame(wx.Frame):
    def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title=u"Hello world"):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
        
class MyApp(wx.App):
    def OnInit(self):
        image = wx.Image('Desert.jpg',wx.BITMAP_TYPE_JPEG)
        self.frame = MyFrame(image)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        
        return True
    
def main():
    app = MyApp()
    app.MainLoop()
    
if __name__ == "__main__":
    main()
        
