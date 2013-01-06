'***********************************************************************************
'*
'* File:		ConvertDocToPdf
'* Author:		moose
'* Email:		wang_peng@csm.com.cn
'* Created:		2012/12/20
'* Last Modified:	2012/12/20
'* Version:		0.1
'*
'***********************************************************************************
currVbs = WScript.ScriptFullName
currDir = Left(currVbs, InStrRev(currVbs,"\"))

Set ws = CreateObject("wscript.shell")
Set word = CreateObject("word.application")
Set args = WScript.Arguments


pdfPath = ""  'pdf file path
	
If args.Count = 1 Then   'only input
	docPath = args(0)
ElseIf args.Count = 2 Then   'only output
	docPath = args(0)
	pdfPath = args(1)
Else    'no input and output  | less used
	docPath = GetOpenFileName(currDir, "All files|*.*|Microsoft Word|*.doc|Microsoft Word 2007|*.docx")
End If 

docToPdf docPath, pdfPath 

ws.Popup "Finish convert doc to pdf ...",1,"Done"



'********************************************************************
'*
'* Function docToPdf(input, output)
'* Purpose: 转换doc到pdf
'* Input:   input   :  doc文件路径
'*          output  :  pdf文件路径
'* Output:  
'*
'********************************************************************
Function docToPdf(input, output)
	'默认存放位置与doc文件在同一个目录
	If "" = Trim(input) Then
		WScript.Quit
	End If 
	If "" = Trim(output) Then 
		output = Left(input, InStrRev(input,".")) + "pdf"
	End If 
	
	Set word = CreateObject("word.application")
	Set doc = word.Documents.Open(input,1)
	
	doc.ExportAsFixedFormat pdfPath, 17, 7, 1 '存为pdf文件 
	
	doc.Close
	word.Quit
	Set doc = Nothing 
	Set word = Nothing	
End Function 


'********************************************************************
'*
'* Function GetOpenFileName(dir, filter)
'* Purpose: 打开文件选择对话框
'* Input:   dir    :    开始目录名
'*          filter ：   过滤类型
'* Output:  选择的文件路径
'*
'********************************************************************
Public Function GetOpenFileName(dir, filter)
    Const msoFileDialogFilePicker = 3
 
    If VarType(dir) <> vbString Or dir="" Then
        dir = CreateObject( "WScript.Shell" ).SpecialFolders( "Desktop" )
    End If
 
    If VarType(filter) <> vbString Or filter="" Then
        filter = "All files|*.*"
    End If
 
    Dim i,j, objDialog, TryObjectNames
    TryObjectNames = Array( _
        "UserAccounts.CommonDialog", _
        "MSComDlg.CommonDialog", _
        "MSComDlg.CommonDialog.1", _
        "Word.Application", _
        "SAFRCFileDlg.FileOpen", _
        "InternetExplorer.Application" _
        )
 
    On Error Resume Next
    Err.Clear
 
    For i=0 To UBound(TryObjectNames)
        Set objDialog = WSH.CreateObject(TryObjectNames(i))
        If Err.Number<>0 Then
        Err.Clear
        Else
        Exit For
        End If
    Next
 
    Select Case i
        Case 0,1,2
        ' 0. UserAccounts.CommonDialog XP Only.
        ' 1.2. MSComDlg.CommonDialog MSCOMDLG32.OCX must registered.
        If i=0 Then
            objDialog.InitialDir = dir
        Else
            objDialog.InitDir = dir
        End If
        objDialog.Filter = filter
        If objDialog.ShowOpen Then
            GetOpenFileName = objDialog.FileName
        End If
        Case 3
        ' 3. Word.Application Microsoft Office must installed.
        objDialog.Visible = False
        Dim objOpenDialog, filtersInArray
        filtersInArray = Split(filter, "|")
        Set objOpenDialog = _
            objDialog.Application.FileDialog( _
                msoFileDialogFilePicker)
            With objOpenDialog
            .Title = "Open File(s):"
            .AllowMultiSelect = False
            .InitialFileName = dir
            .Filters.Clear
            For j=0 To UBound(filtersInArray) Step 2
                .Filters.Add filtersInArray(j), _
                     filtersInArray(j+1), 1
            Next
            If .Show And .SelectedItems.Count>0 Then
                GetOpenFileName = .SelectedItems(1)
            End If
            End With
            objDialog.Visible = True
            objDialog.Quit
        Set objOpenDialog = Nothing
        Case 4
        ' 4. SAFRCFileDlg.FileOpen xp 2003 only
        ' See http://www.robvanderwoude.com/vbstech_ui_fileopen.php
        If objDialog.OpenFileOpenDlg Then
           GetOpenFileName = objDialog.FileName
        End If
        Case 5
 
        Dim IEVersion,IEMajorVersion, hasCompleted
        hasCompleted = False
        Dim shell
        Set shell = CreateObject("WScript.Shell")
        ' 下面获取IE版本
        IEVersion = shell.RegRead( _
            "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\Version")
        If InStr(IEVersion,".")>0 Then
            ' 获取主版本号
            IEMajorVersion = CInt(Left(IEVersion, InStr(IEVersion,".")-1))
            If IEMajorVersion>7 Then
                ' 如果版本号大于7，也就是大于IE7，则采取MSHTA方案
                ' Bypasses c:\fakepath\file.txt problem
                ' http://pastebin.com/txVgnLBV
                Dim fso
                Set fso = CreateObject("Scripting.FileSystemObject")
 
                Dim tempFolder : Set tempFolder = fso.GetSpecialFolder(2)
                Dim tempName : tempName = fso.GetTempName()
                Dim tempFile : Set tempFile = tempFolder.CreateTextFile(tempName & ".hta")
                Dim tempBaseName
                tempBaseName = tempFolder & "\" & tempName
                tempFile.Write _
                    "<html>" & _
                    "  <head>" & _
                    "    <title>Browse</title>" & _
                    "  </head>" & _
                    "  <body>" & _
                    "    <input type='file' id='f'>" & _
                    "    <script type='text/javascript'>" & _
                    "      var f = document.getElementById('f');" & _
                    "      f.click();" & _
                    "      var fso = new ActiveXObject('Scripting.FileSystemObject');" & _
                    "      var file = fso.OpenTextFile('" & _
                              Replace(tempBaseName,"\", "\\") & ".txt" & "', 2, true);" & _
                    "      file.Write(f.value);" & _
                    "      file.Close();" & _
                    "      window.close();" & _
                    "    </script>" & _
                    "  </body>" & _
                    "</html>"
                tempFile.Close
                Set tempFile = Nothing
                Set tempFolder = Nothing
                shell.Run tempBaseName & ".hta", 1, True
                Set tempFile = fso.OpenTextFile(tempBaseName & ".txt", 1)
                GetOpenFileName = tempFile.ReadLine
                tempFile.Close
                fso.DeleteFile tempBaseName & ".hta"
                fso.DeleteFile tempBaseName & ".txt"
                Set tempFile = Nothing
                Set fso = Nothing
                hasCompleted = True ' 标记为已完成
            End If
        End If
        If Not hasCompleted Then
            ' 5. InternetExplorer.Application IE must installed
            objDialog.Navigate "about:blank"
            Dim objBody, objFileDialog
            Set objBody = _
                objDialog.document.getElementsByTagName("body")(0)
            objBody.innerHTML = "<input type='file' id='fileDialog'>"
            while objDialog.Busy Or objDialog.ReadyState <> 4
                WScript.sleep 10
            Wend
            Set objFileDialog = objDialog.document.all.fileDialog
                objFileDialog.click
                GetOpenFileName = objFileDialog.value
        End If
        objDialog.Quit
        Set objFileDialog = Nothing
        Set objBody = Nothing
        Set shell = Nothing
        Case Else
        ' Sorry I cannot do that!
    End Select
 
    Set objDialog = Nothing
End Function