'On error resume next
Set args = WScript.Arguments
set fs = createobject("scripting.filesystemobject")

bmurlstrs = readUtf8File(args(0))
bmstrs = Split(bmstrs, Chr(10))
WScript.Echo TypeName(bmurlstrs)

For Each bmstr In bmstrs
	If InStr(bmstr, "|*|") >=0 Then 
		urlstrs = Split(bmstr, "|*|")
		GenerateUrl urlstrs(0),urlstrs(1)
	End If 
Next

'close file
fs.DeleteFile args(0)


Function GenerateUrl(bmurl, bmpath)
	Set scut = ws.CreateShortcut(bmpath)
	scut.TargetPath=bmurl  
	scut.Save
End Function 

Function readUtf8File(fname)	
	Set ados = CreateObject("adodb.stream")
	With ados
		.Charset = "utf-8"
		.Type = 2
		.Open
		.LoadFromFile fname
		readUtf8File = .ReadText
		.Close
	End With 
	Set ados = Nothing 
End Function 