#-*- coding : utf-8 -*-
import wx

class MyFrame(wx.Frame):
    def __init__(self,image, parent=None, id=-1, pos=wx.DefaultPosition, title=u"Hello Python"):
        temp = image.ConvertToBitMap()
        size = temp.GetWidth(), temp.GetHeight()
        wx.Frame.__init__(self, parent, id, title, pos, size)
        self.bmp = wx.StaticBitmap(parent=self, bitmap = temp)
        
def main():
    app = wx.PySimpleApp()
    image = wx.Image("Desert.jpg", wx.BITMAP_TYPE_JPEG)
    frame = MyFrame(image)
    frame.Show()
    app.MainLoop()
    
if __name__ == "__main__":
    main() 

