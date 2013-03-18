'On error resume next
Set args = WScript.Arguments
Set ws = CreateObject("wscript.shell")

GenerateUrl args(0),args(1)

Function GenerateUrl(bmurl, bmpath)
	Set scut = ws.CreateShortcut(bmpath)
	scut.TargetPath=bmurl  
	scut.Save
End Function 