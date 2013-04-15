import wx

class Example(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        
        panel = wx.Panel(self)
        
        mylocale = wx.Locale()
        mylocale.AddCatalogLookupPathPrefix(".")
        mylocale.AddCatalog("simple_de")
        
        _ = wx.GetTranslation
        wx.StaticText(panel, -1, _("Hello"), (10,10))
        wx.StaticText(panel, -1, wx.GetTranslation("Hello"), (10,30))
        
                         
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame  = Example(None, -1)
    frame.Show()
    app.MainLoop()           