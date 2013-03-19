#-*- coding:cp936 -*-

import win32com.client

bmurl = "http://www.sunxin.org/forum/"
bmpath = "C:\Users\wang_peng\Desktop\bm\技术论坛\论坛首页 - 欢迎来到程序员之家论坛.url"

vbs = win32com.client.Dispatch("ScriptControl") 
vbs.language = "vbscript" 
scode="""Function GenerateUrl(bmurl, bmpath) 
set ws = createobject("wscript.shell")
scut = ws.CreateShortcut(bmpath)
scut.TargetPath=bmurl  
scut.Save()
End Function 
""" 
vbs.addcode(scode) 
vbs.eval("GenerateUrl(bmurl, bmpath)") 