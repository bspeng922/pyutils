#-*- coding: utf-8 -*-
## 
#  Copyright (C) 
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation.
# 
##
# @file: batchexexutesql.py
# @author: moose
# @blog: http://www.pystack.org
# @mail: admin@pystack.org
# @QQ: 852354673
# @date: 2013-3-25
# 
import wx
import os
import sys
import MySQLdb
import base64
import ConfigParser
from subprocess import Popen, PIPE

debug = True
dbconfigfile = "dbuser.ini"

class FileDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window
    
    def OnDropFiles(self, x, y, filenames):
        self.window.SetValue(str(filenames[0]))

class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Execute SQLs", size=(400,600))
        self.Center()
        self.SetIcon(wx.Icon("convert.ico",wx.BITMAP_TYPE_ICO))
        panel = wx.Panel(self)
        
        #create menubar
        self.SetMenuBar(self.InitMenuBar())
        
        #create ip textctrl and bind event
        self.textctrl_ip = wx.TextCtrl(panel, -1, "", size=(396,26))
        self.button_ip = wx.Button(panel, -1, "Load IP File",size=(-1,40))
        self.textctrl_ip.Bind(wx.EVT_LEFT_DCLICK, self.OnSelectIpaddress)
        self.Bind(wx.EVT_BUTTON, self.OnSelectIpaddress, self.button_ip)
        droptarget = FileDrop(self.textctrl_ip)
        self.textctrl_ip.SetDropTarget(droptarget)
        
        #create sql textctrl and bind event
        self.textctrl_sql = wx.TextCtrl(panel, -1, "")
        self.button_sql = wx.Button(panel, -1, "Load SQL File", size=(-1,40))
        self.textctrl_sql.Bind(wx.EVT_LEFT_DCLICK, self.OnSelectSqlFile)
        self.Bind(wx.EVT_BUTTON, self.OnSelectSqlFile, self.button_sql)
        droptarget = FileDrop(self.textctrl_sql)
        self.textctrl_sql.SetDropTarget(droptarget)
        
        #create start button and bind event
        self.button_run = wx.Button(panel, -1, "Execute All", size=(-1,40))
        self.Bind(wx.EVT_BUTTON, self.OnExecuteAll, self.button_run)
        
        self.textctrl_log = wx.TextCtrl(panel, -1, "", style=wx.TE_MULTILINE, size=(396,200))
        
        #create status bar
        self.CreateStatusBar()
        
        #set position
        framesizer = wx.BoxSizer(wx.VERTICAL)
        
        framesizer.Add(self.textctrl_ip,0,wx.ALL|wx.EXPAND,2)
        framesizer.Add(self.button_ip, 0, wx.CENTER)
        framesizer.Add((-1,10))
        framesizer.Add(self.textctrl_sql,0,wx.ALL|wx.EXPAND, 2)
        framesizer.Add(self.button_sql, 0, wx.CENTER)
        framesizer.Add((-1,10))
        framesizer.Add(self.button_run, 0, wx.CENTER)
        framesizer.Add(self.textctrl_log, 1, wx.ALL|wx.EXPAND, 2)
        
        panel.SetSizer(framesizer)
        framesizer.Fit(self)
        
        #load dbuser and dbpassword
        self.dbuser, self.dbpasswd = self.GetDbUserandPasswd(dbconfigfile)
        self.dbcharset = "utf8"
        self.hostcount = 0
        self.errorhost = 0
        
        
    def InitMenuBar(self):
        """init menubar"""
        menubar = wx.MenuBar()
        
        menu_file = wx.Menu()
        menubar.Append(menu_file, "&File")
        
        menu_help = wx.Menu()
        menubar.Append(menu_help, "&Help")
        
        menu_ip = menu_file.Append(wx.NewId(), "Load &IP","load ip address...")
        menu_sql = menu_file.Append(wx.NewId(), "Load &SQL","load ip address...")
        menu_export = menu_file.Append(wx.NewId(), "&Export Log","Export execute log...")
        menu_file.AppendSeparator()
        menu_exit = menu_file.Append(wx.ID_EXIT, "E&xit", "Exit this application.")
        
        menu_doc = menu_help.Append(wx.NewId(), "Help &Contents","This program doesnot has a help file.")
        menu_file.AppendSeparator()
        menu_about = menu_help.Append(wx.NewId(), "&About Me", "Http://www.pystack.org")
        
        self.Bind(wx.EVT_MENU,self.OnSelectIpaddress,menu_ip)
        self.Bind(wx.EVT_MENU,self.OnSelectSqlFile,menu_sql)
        self.Bind(wx.EVT_MENU,self.OnExportLog,menu_export)
        self.Bind(wx.EVT_MENU,self.OnExit,menu_exit)
        self.Bind(wx.EVT_MENU,self.OnHelpContent,menu_doc)
        self.Bind(wx.EVT_MENU,self.OnAbout,menu_about)        
        
        return menubar
    
    
    def OnSelectIpaddress(self, event):
        """when menu 'Load IP' clicked, run this function"""
        wildcard_ip = "IP File(*.txt)|*.txt|All Files(*.*)|*.*"
        filedlg = wx.FileDialog(self, "Select your IP file...", os.getcwd(), style=wx.OPEN, wildcard=wildcard_ip)
        
        if filedlg.ShowModal() == wx.ID_OK:
            filepath_ip = filedlg.GetPath()
            self.textctrl_ip.SetValue(filepath_ip)
            if debug: print "Ip File: %s"%filepath_ip
            self.textctrl_log.AppendText("Ip File: %s\n"%filepath_ip)
        
        filedlg.Destroy()
        
    
    def OnSelectSqlFile(self, event):
        """when menu 'Load SQL' clicked, run this function"""
        wildcard_sql = "SQL File(*.sql)|*.sql|All Files(*.*)|*.*"
        filedlg = wx.FileDialog(self, "Select SQL File...",os.getcwd(), style=wx.OPEN, wildcard=wildcard_sql)
        
        if filedlg.ShowModal() == wx.ID_OK:
            filepath_sql = filedlg.GetPath()
            self.textctrl_sql.SetValue(filepath_sql)
            if debug: print "SQL File: %s"%filepath_sql
            self.textctrl_log.AppendText("SQL File: %s\n"%filepath_sql)
        
        filedlg.Destroy()
        
    
    def OnExportLog(self, event):
        """when menu 'export log' clicked, run this function"""
        wildcard_log = "Log File(*.log)|*.log|All Files(*.*)|*.*"
        filedlg = wx.FileDialog(self, "Save Log To...", os.getcwd(), style=wx.SAVE|wx.OVERWRITE_PROMPT, wildcard=wildcard_log)
        
        if filedlg.ShowModal() == wx.ID_OK:
            filepath_log = filedlg.GetPath()
            
            if not os.path.splitext(filepath_log[1]):
                filepath_log += ".log"
                
            logfile = open(filepath_log, 'w')
            logfile.write(self.textctrl_log.GetValue())
            logfile.close()
            
        filedlg.Destroy()
    
    
    def OnExit(self, event):
        """when menu 'exit' clicked, run this function"""
        self.Destroy()
        
        
    def OnHelpContent(self, event):
        """when menu 'help contents' clicked, run this function"""
        pass
    
        
    def OnAbout(self, event):
        """when menu 'about me' clicked, run this function"""
        info = wx.AboutDialogInfo()
        info.Name = "SQL Executer"
        info.Version = "0.0.1"
        info.Copyright = "(C) 2013 - 3015  PyStack"
        info.SetDescription("SQL Executer is a program for you to automatic execute sql in different servers .")
        info.WebSite = ("http://www.pystack.org")
        info.Developers = ["Moose"]
        info.License = "Nothing to tell"
        
        wx.AboutBox(info)
        
        
    def OnExecuteAll(self, event):
        """Start to execute sql in all servers"""
        filepath_ip = self.textctrl_ip.GetValue()
        filepath_sql = self.textctrl_sql.GetValue()
        
        if os.path.exists(filepath_ip) and os.path.exists(filepath_sql):
            #read ip from ip file
            file_ip = open(filepath_ip, 'r')
            
            for str_ip in file_ip.readlines():                    
                self.ExecuteSqlFileOnServer(str_ip.strip(), filepath_sql)
            
            file_ip.close()
            
            self.textctrl_log.AppendText("\nHostCount: %s    HostError: %s\n"%(self.hostcount, self.errorhost))
            self.textctrl_log.AppendText("All sql executed !\n\n")
        else:
            if debug: print "Ip File or SQL File not found ! Please check your input..."
            self.textctrl_log.AppendText("Ip File or SQL File not found ! Please check your input...\n\n")
    
    
    def ExecuteSqlFileOnServer(self, ipaddr, sqlfile):
        if debug: "+ Executing sql on server (%s)\n"%ipaddr
        self.textctrl_log.AppendText("+ Executing sql on server (%s)\n"%ipaddr)
        self.hostcount += 1
        
        #check if the db connectable.
        try :
            conn = MySQLdb.connect(host=ipaddr, user=self.dbuser, passwd=self.dbpasswd) 
            conn.close()          
            
            #execute sql file 
            process = Popen('mysql -h%s -u%s -p%s --default-character-set=%s' \
                            %(ipaddr, self.dbuser, self.dbpasswd, self.dbcharset), stdout=PIPE, stdin=PIPE, shell=True)
            output = process.communicate('source '+sqlfile)
        except MySQLdb.Error, e:
            self.errorhost += 1
            if debug: print "? Unreachable host: %s"%ipaddr
            self.textctrl_log.AppendText("  - Unreachable host: %s\n"%ipaddr)
    
    
    def GetDbUserandPasswd(self, dbcfgfile):
        """get db connection info from dbuser.ini, username & password should be encoded 3 times by base64"""
        if os.path.exists(dbcfgfile):
            cfg = ConfigParser.ConfigParser()
            cfg.read(dbcfgfile)
            
            try:
                username = cfg.get("USER", "username").strip()
                password = cfg.get("USER", "password").strip()
            except ConfigParser.NoSectionError, ConfigParser.NoOptionError:
                if debug: print "illegal ini file..."
                self.textctrl_log.AppendText("illegal ini file...\n")
            
            #check if username & password has been encoded
            try:
                username = base64.b64decode(base64.b64decode(base64.b64decode(username)))
            except TypeError:
                if debug: "Your username not encoded !"
                self.textctrl_log.AppendText("Your username not encoded !\n")
            try:
                password = base64.b64decode(base64.b64decode(base64.b64decode(password))) 
            except TypeError:
                if debug: "Your password not encoded !"
                self.textctrl_log.AppendText("Your password not encoded !\n")
                
            #if debug: print "Username: %s    Password: %s"%(username, password)   
             
            return username, password
        else:
            if debug: print "Missing configure file !"
            self.textctrl_log.AppendText("Missing configure file !")    
        

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MainFrame(None, -1)
    frame.Show()
    app.MainLoop()