#-*- coding:utf-8 -*-
import win32com.client

bmurl = unicode(r"http://www.sunxin.org/forum/","utf8")
bmpath = unicode(r"C:\Users\wang_peng\Desktop\bm\技术论坛\论坛首页 - 欢迎来到程序员之家论坛.url","utf8")

ws = win32com.client.Dispatch("wscript.shell")
scut = ws.CreateShortcut(bmpath)
scut.TargetPath=bmurl  
scut.Save
print bmurl,bmpath