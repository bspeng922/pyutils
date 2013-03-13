#-*- coding:utf-8 -*-

import wx
import sys
import os

debug = True

class ConvertFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Opera Bookmark Convert",size=(600,400), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU)
        self.Center()
        self.SetIcon(wx.Icon("secure.ico", wx.BITMAP_TYPE_ICO))
        panel = wx.Panel(self)
        
        #set menu bar
        self.SetMenuBar(self.CreateMenubar())
                
        #bookmark button
        self.textctrl_bm = wx.TextCtrl(panel, -1, "", size=(400,20))
        self.button_bm = wx.Button(panel, -1, "Choose Bookmark File")
        self.Bind(wx.EVT_BUTTON, self.OnBMBtnClick, self.button_bm)
        self.textctrl_bm.Bind(wx.EVT_LEFT_DCLICK, self.OnBMBtnClick)
        
        #save path
        self.textctrl_sp = wx.TextCtrl(panel, -1, "", size=(400,20))
        self.button_sp = wx.Button(panel, -1, "Save To")
        self.Bind(wx.EVT_BUTTON, self.OnSPBtnClick, self.button_sp)
        self.textctrl_sp.Bind(wx.EVT_LEFT_DCLICK, self.OnSPBtnClick)
        
        #start convert
        self.button_start = wx.Button(panel, -1, "Start Convert")
        self.Bind(wx.EVT_BUTTON, self.OnSCBtnClick, self.button_start)
        
        #log text info
        self.textctrl_log = wx.TextCtrl(panel, -1, "")
        
        #status bar
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-4,-2])
        
    def CreateMenubar(self):
        #menu bar
        menubar = wx.MenuBar()
        
        menu_file = wx.Menu()
        menubar.Append(menu_file, "&File")
        
        menu_help = wx.Menu()
        menubar.Append(menu_help, "&Help")
        
        menu_open = menu_file.Append(wx.NewId(), "&Open Bookmark","Open an opera...")
        menu_path = menu_file.Append(wx.NewId(), "&Save To","Save bookmark To...")
        menu_file.AppendSeparator()
        menu_exit = menu_file.Append(wx.ID_EXIT,"&Exit","Exit this application.")
                
        menu_doc = menu_help.Append(wx.NewId(),"&Help Contents","Manual about this application.")
        menu_about = menu_help.Append(wx.ID_ABOUT,"&About","This is a free software.")
        
        self.Bind(wx.EVT_MENU, self.OnOpenBookmark, menu_open)
        self.Bind(wx.EVT_MENU, self.OnSavepath, menu_path)
        self.Bind(wx.EVT_MENU, self.OnAbout, menu_about)
        self.Bind(wx.EVT_MENU, self.OnExit, menu_exit)
        
        return menubar
        
    def OnBMBtnClick(self, event):
        self.OnOpenBookmark(event)    
        
    def OnSPBtnClick(self, event):
        self.OnSavepath(event)
        
    def OnSCBtnClick(self, event):
        if self.textctrl_bm.GetValue() and self.textctrl_sp.GetValue():
            self.StartConvert()
        else:
            errdlg = wx.MessageBox("Information needs to be complete","Error")
            event.Skip()
    
    def OnSavepath(self, event):
        dirdlg = wx.DirDialog(self, "Choose path...",  os.getcwd())
        
        if dirdlg.ShowModal() == wx.ID_OK:
            savepath = dirdlg.GetPath()
            self.textctrl_sp.SetValue(savepath)
            if debug:
                print "Save To: %s"%savepath
        
        dirdlg.Destroy()
    
    def OnOpenBookmark(self, event):
        operabmfile = "Opera Bookmark File(*.adr)|*.adr|All files(*.*)|*.*"
        opendlg = wx.FileDialog(self, "Open opera bookmark...",os.getcwd(), style=wx.OPEN, wildcard=operabmfile)
        
        if opendlg.ShowModal() == wx.ID_OK:
            bmpath = opendlg.GetPath()
            self.textctrl_bm.SetValue(bmpath)
            if debug:
                print "Bookmark: %s"%bmpath
            
        opendlg.Destroy()
    
    def OnAbout(self, event):
        msgbox = wx.MessageBox("This is a bookmark convert application","About Me")
        
    def OnExit(self, event):
        self.Destroy()
        
    def StartConvert(self, bmfile, sppath):
        pass
        
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = ConvertFrame(None, -1)
    frame.Show()
    app.MainLoop()
