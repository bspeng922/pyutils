#-*- coding: utf-8 -*-

import wx
import sys
import os
import win32com.client

debug = True
vbsfile = os.path.join(os.getcwd(),"createurllink.vbs")
#vbsfile = "createurllink.vbs"

class ConvertFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Opera Bookmark Convert",size=(400,600))
        self.Center()
        self.SetIcon(wx.Icon("convert.ico", wx.BITMAP_TYPE_ICO))
        
        panel = wx.Panel(self)
        
        #set menu bar
        self.SetMenuBar(self.CreateMenubar())
        
        #sizer     
        framesizer = wx.BoxSizer(wx.VERTICAL)   
        
        #bookmark button
        self.textctrl_bm = wx.TextCtrl(panel, -1, "", size=(380,26))
        self.button_bm = wx.Button(panel, -1, "Choose Bookmark File",size=(-1,40))
        self.Bind(wx.EVT_BUTTON, self.OnBMBtnClick, self.button_bm)
        self.textctrl_bm.Bind(wx.EVT_LEFT_DCLICK, self.OnBMBtnClick)
        
        #save path
        self.textctrl_sp = wx.TextCtrl(panel, -1, "", size=(380,26))
        self.button_sp = wx.Button(panel, -1, "Save To",size=(-1,40))
        self.Bind(wx.EVT_BUTTON, self.OnSPBtnClick, self.button_sp)
        self.textctrl_sp.Bind(wx.EVT_LEFT_DCLICK, self.OnSPBtnClick)        
        
        #start convert
        self.button_start = wx.Button(panel, -1, "Start Convert",size=(-1,40))
        self.Bind(wx.EVT_BUTTON, self.OnSCBtnClick, self.button_start)        
        
        #log text info
        self.textctrl_log = wx.TextCtrl(panel, -1, "", style=wx.TE_MULTILINE,size=(-1,160))
        
        #layout
        framesizer.Add(self.textctrl_bm,0,wx.ALL|wx.EXPAND,2)
        framesizer.Add(self.button_bm,0,wx.CENTER)
        framesizer.Add((-1,10))
        framesizer.Add(self.textctrl_sp,0,wx.ALL|wx.EXPAND,2)
        framesizer.Add(self.button_sp,0,wx.CENTER)
        framesizer.Add((-1,10))
        framesizer.Add(self.button_start,0,wx.CENTER)
        framesizer.Add((-1,10))
        framesizer.Add(self.textctrl_log,1,wx.ALL|wx.EXPAND,2)   #1 for auto size
        
        #status bar
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([-4,-2])
        
        panel.SetSizer(framesizer)
        framesizer.Fit(self)
        
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
        currbm = self.textctrl_bm.GetValue()
        currsp = self.textctrl_sp.GetValue()
        
        if currbm:
            if not currsp:
                currsp = os.path.basename(currbm)
                self.textctrl_log.AppendText("Url links save to: %s"%currsp)
            self.StartConvert(currbm, currsp)
        else:
            self.textctrl_log.AppendText("Error: Information needs to be complete\n")
            event.Skip()
    
    def OnSavepath(self, event):
        dirdlg = wx.DirDialog(self, "Choose path...",  os.getcwd())
        
        if dirdlg.ShowModal() == wx.ID_OK:
            savepath = dirdlg.GetPath()
            self.textctrl_sp.SetValue(savepath)
            if debug:
                print "Save To: %s"%savepath
            self.textctrl_log.AppendText("Save To: %s\n"%savepath)
        
        dirdlg.Destroy()
    
    def OnOpenBookmark(self, event):
        operabmfile = "Opera Bookmark File(*.adr)|*.adr|All files(*.*)|*.*"
        opendlg = wx.FileDialog(self, "Open opera bookmark...",os.getcwd(), style=wx.OPEN, wildcard=operabmfile)
        
        if opendlg.ShowModal() == wx.ID_OK:
            bmpath = opendlg.GetPath()
            self.textctrl_bm.SetValue(bmpath)
            if debug:
                print "Bookmark: %s"%bmpath
            self.textctrl_log.AppendText("Bookmark: %s\n"%bmpath)
            
        opendlg.Destroy()
    
    def OnAbout(self, event):
        msgbox = wx.MessageBox("This is a bookmark convert application\nAuthor: www.pystack.org\nVersion: 1.0","About Me")
        
    def OnExit(self, event):
        self.Destroy()
        
    def StartConvert(self, bmfile, sppath):
        self.textctrl_log.AppendText("Running...\n")
        if os.path.exists(vbsfile):
            if os.path.exists(bmfile) and os.path.exists(sppath):                
                #read bookmark file
#                tempfilename = "opera.temp"
#                tempfilepath = os.path.join(sppath, tempfilename)
                bmfile = open(bmfile, 'r')
#                tempfile = open(tempfilepath,'w')
                issubfld = 0
                bmfldpath = ""
                bmfldname = ""
                foldercount = 0
                urlcount = 0
                urlok = 0
                
                while 1:
                    bmline = bmfile.readline()
                    if len(bmline) == 0:
                        break
                    
                    if bmline.strip() == "-":
                        issubfld = 0
                    elif bmline.find("#FOLDER") <> -1:
                        bmfldid = bmfile.readline().split("=")[1]
                        if issubfld:
                            bmfldname = os.path.join(bmfldname, unicode(bmfile.readline().split("=")[1].strip(),"utf-8"))
                        else:
                            bmfldname = unicode(bmfile.readline().split("=")[1].strip(),"utf-8")
                        
                        bmfldpath = os.path.join(sppath, bmfldname)
                        if not os.path.exists(bmfldpath):
                            os.mkdir(bmfldpath)
                            if debug : print "+ Create folder: %s"%bmfldpath
                            self.textctrl_log.AppendText("+ Create folder: %s\n"%bmfldpath)
                        foldercount += 1
                        issubfld=1
                    elif bmline.find("#URL") <> -1:
                        urlcount += 1
                        bmurlid = bmfile.readline().split("=")[1]
                        bmurlname = unicode(bmfile.readline().split("=")[1].strip(),"utf-8")
                        bmurlurl = unicode(bmfile.readline().split("=")[1].strip(),"utf-8")
                        
                        bmurlname = self.LegalFileName(bmurlname)
                        bmurlpath = os.path.join(bmfldpath,bmurlname+".url")
                        
                        if not os.path.exists(bmurlpath):
                            self.GenerateUrlLink(bmurlurl, bmurlpath)
                            #tempfile.write(bmurlurl+"|*|"+bmurlpath+"\n")
                            if debug: print "  + Create Url (%s)"%bmurlname
                            self.textctrl_log.AppendText("  + Create Url (%s)\n"%bmurlurl)
                            urlok += 1
                        else:
                            if debug: print "Url exists ! (%s)"%bmurlname
                            self.textctrl_log.AppendText("Url exists ! (%s)\n"%bmurlurl)
                        
#                tempfile.close()    
                bmfile.close()
#                self.textctrl_log.AppendText("\nConverting Urls...\n")
#                self.GenerateUrlLink(tempfilepath)
                self.textctrl_log.AppendText("\nFolderCount: %s    UrlCount: %s    UrlCreated: %s\n"%(foldercount, urlcount, urlok))
                self.textctrl_log.AppendText("Finish convert.\n\n")
            else:
                self.textctrl_log.AppendText("Error: Bookmark file not exists !\nPlease check you input...\n\n")
        else:
            self.textctrl_log.AppendText("Missing files, Please reinstall the program...\n\n")
            
    def LegalFileName(self, fname):
        illegalchars = ['<','>','/','|','\\',':','"','*','?']
        for illchar in illegalchars:
            if fname.find(illchar) <> -1:
                fname = fname.replace(illchar, " ")
                
        return fname
    
    def GenerateUrlLink(self, bmurl, bmpath):        
        if debug: print 'Exec: "%s" "%s"'%(bmurl, bmpath)
        
        #use py win32
        ws = win32com.client.Dispatch("wscript.shell")
        scut = ws.CreateShortcut(bmpath)
        scut.TargetPath=bmurl  
        scut.Save
        
if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = ConvertFrame(None, -1)
    frame.Show()
    app.MainLoop()
