
On Error Resume Next 
Const dstfolder = "result"
Const srcfolder = "bookmarks"
Const logfilename = "convert.log"
successcount = 0
failedcount = 0

currvbs = WScript.ScriptFullName
currdir = Left(currvbs, InStrRev(currvbs,"\"))

srcfldpath = currdir & srcFolder
dstfldpath = currdir & dstfolder
logfilepath = currdir & logfilename

Set ws = CreateObject("wscript.shell")
Set fs = CreateObject("scripting.filesystemobject")
Set logfile = fs.OpenTextFile(logfilepath, 8, True)
logfile.WriteLine "************************* "& Now &" *************************"

If Not fs.FolderExists(srcfldpath) Then 
	logfile.WriteLine "["& Now &"] No folder called ("&srcfolder&")"
	MsgBox "No folder called "&srcfolder
	WScript.Quit
End If 

If Not fs.FolderExists(dstfldpath) Then 
	logfile.WriteLine "["& Now &"] Create folder ("&dstfldpath&")"
	fs.CreateFolder(dstfldpath)
End If

Set srcfld = fs.GetFolder(srcfldpath)
For Each subfld In srcfld.SubFolders
	currfld = dstfldpath&"\"&subfld.Name
	If Not fs.FolderExists(currfld) Then 
		fs.CreateFolder(currfld)
		logfile.WriteLine "["& Now &"] Create folder ("&subfld.Name&")"
	End If 
	
	For Each file In subfld.Files
		convert2link file.Path, currfld&"\"&file.Name&".url"
		logfile.WriteLine "["& Now &"] Create link ("&file.Name&")"
	Next		
Next


logfile.WriteBlankLines 1
logfile.WriteLine "["& Now &"] Done ."
logfile.WriteLine "["& Now &"] Success("&successcount&")    Failed("&failedcount&")"
logfile.WriteBlankLines 2
logfile.Close
ws.Popup "Finish convert urls .",2,"Done"



'convert html 2 urllink
Function convert2link(srchtml, destlink)
	On Error Resume Next 
	targetUrl = fs.OpenTextFile(srchtml).ReadLine
	
	If Err.Number <> 0 Then 
		logfile.WriteLine "["& Now &"] Unable to read file("&srchtml&")"
		failedcount = failedcount + 1
		Err.Clear
	Else 	
		Set scut = ws.CreateShortcut(destlink)
		scut.TargetPath = targetUrl
		
		scut.Save
		successcount = successcount + 1
	End If
End Function
