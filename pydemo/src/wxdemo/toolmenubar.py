import wx
import wx.py.images

class ToolbarFrame(wx.Frame):
    def __init__(self,parent, id):
        wx.Frame.__init__(self, parent, id, "Toolbars", size=(300,200))
        
        panel = wx.Panel(self)
        panel.SetBackgroundColour('white')
        
        statusBar = self.CreateStatusBar()
        
        toolBar = self.CreateToolBar()
        toolBar.AddSimpleTool(wx.NewId(), wx.py.images.getPyBitmap(),"New","Long help for new")
        toolBar.AddSimpleTool(wx.NewId(), wx.py.images.getPyBitmap(),"Edit","Long help for edit")
        toolBar.Realize()
        
        menuBar = wx.MenuBar()
        
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "C&ut", "")
        menu2.Append(wx.NewId(), "Paste","")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...","Display options")
        menuBar.Append(menu2, "&Eidt")
        
        self.SetMenuBar(menuBar)
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = ToolbarFrame(parent=None, id=-1)
    frame.Show()
    
    app.MainLoop()
