import wx
import os
import confighelper

btnimgs = ["images/stop.png",
           "images/start.png",
           "images/pause.png",
           "images/pre.png",
           "images/next.png",
           "images/foward.png",
           "images/back.png"
           ]

class MusicPlayer(wx.Frame):
    def __init__(self, *args, **kw):
        wx.Frame.__init__(self, *args, **kw)
        maincfg = confighelper.MainConfig()
        iconpath = maincfg.geticon()
        if iconpath:
            if os.path.exists(iconpath): self.SetIcon(wx.Icon(iconpath, type=wx.BITMAP_TYPE_ICO))
        self.Center()
        self.SetMenuBar(self.InitMenuBar())
        self.InitToolBar()
        panel = wx.Panel(self)
        
        
        
        
        self.CreateStatusBar()
        
    def InitMenuBar(self):
        #menu file
        menu_file = wx.Menu()
        menu_file.Append(wx.NewId(),"&Open", "Open a music file")
        menu_file.AppendSeparator()
        
        
        #menu edit
        menu_edit = wx.Menu()
        
        #menu view
        menu_view = wx.Menu()
        
        #menu playback
        menu_playback = wx.Menu()
        
        #menu library
        menu_library = wx.Menu()
        
        #menu help
        menu_help = wx.Menu()
        
        
        menubar = wx.MenuBar()
        menubar.Append(menu_file,"&File")
        menubar.Append(menu_edit,"&Edit")
        menubar.Append(menu_view,"&View")
        menubar.Append(menu_playback,"&Playback")
        menubar.Append(menu_library,"&Library")
        menubar.Append(menu_help,"&Help")
        
        return menubar
    
    def InitToolBar(self):
        toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL)
        
        self.btn_stop = wx.BitmapButton(toolbar, -1, wx.Bitmap(btnimgs[0]), size=(25,25),style=wx.BU_EXACTFIT|wx.BU_ALIGN_MASK)
        self.btn_start = wx.BitmapButton(toolbar, -1, wx.Bitmap(btnimgs[1]))
        self.btn_pause = wx.BitmapButton(toolbar, -1, wx.Bitmap(btnimgs[2]), size=(20,20),style=wx.BU_EXACTFIT|wx.BU_ALIGN_MASK)
        self.btn_pre = wx.BitmapButton(toolbar, -1, wx.Bitmap(btnimgs[3]), size=(20,20))
        self.btn_next = wx.BitmapButton(toolbar, -1, wx.Bitmap(btnimgs[4]), size=(20,20))
        self.btn_foward = wx.BitmapButton(toolbar, -1, wx.Bitmap(btnimgs[5]), size=(20,20))
        self.btn_back = wx.BitmapButton(toolbar, -1, wx.Bitmap(btnimgs[6]), size=(20,20))
        self.volume = wx.Slider(toolbar, -1, 50, 0, 100, size=(100,-1))
        self.timeline = wx.Slider(toolbar, -1, 0, 0, 100, size=(200,-1))
        
        
        
        toolbar.AddControl(self.btn_stop)
        toolbar.AddControl(self.btn_start)
        toolbar.AddControl(self.btn_pause)
        toolbar.AddControl(self.btn_pre)
        toolbar.AddControl(self.btn_next)
        toolbar.AddControl(self.btn_foward)
        toolbar.AddControl(self.btn_back)
        toolbar.AddSeparator()
        toolbar.AddControl(self.volume)
        toolbar.AddSeparator()
        toolbar.AddControl(self.timeline)
        
        #display tools
#        tbsizer = wx.BoxSizer(wx.HORIZONTAL)
#        tbsizer.AddMany([(self.btn_stop, 0),
#                         (self.btn_start, 0, wx.LEFT, 5),
#                         (self.btn_pause, 0, wx.LEFT, 5),
#                         (self.btn_pre, 0, wx.LEFT, 5),
#                         (self.btn_next, 0, wx.LEFT, 5),
#                         (self.btn_foward, 0, wx.LEFT, 5),
#                         (self.btn_back, 0, wx.LEFT, 5),
#                         (self.volume, 0, wx.LEFT, 5),
#                         (self.timeline, 0, wx.LEFT, 5)
#                         ])
#        tbsizer.Add(self.btn_stop, 0)
#        tbsizer.Add(self.btn_start, 0, wx.LEFT, 5)
#        tbsizer.Add(self.btn_pause, 0, wx.LEFT, 5)
#        tbsizer.Add(self.btn_pre, 0, wx.LEFT, 5)
#        tbsizer.Add(self.btn_next, 0, wx.LEFT, 5)
#        tbsizer.Add(self.volume, 0, wx.LEFT, 5)
#        tbsizer.Add(self.timeline, 0, wx.LEFT, 5)
#        toolbar.SetSizer(tbsizer)
#        tbsizer.Fit(toolbar)
        
        #bing event
        toolbar.Realize()
    
    
if __name__ == "__main__":
    app = wx.PySimpleApp()
    MusicPlayer(None, -1, "Music Player",size=(600,400)).Show()
    app.MainLoop()
        