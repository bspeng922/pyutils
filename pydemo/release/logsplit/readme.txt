根据传入的关键字，然后提取出包含关键字的那一行，并写入新的文件中。

命令行：
AnalysisLog-r2-x64.exe [keyword[|keyword]]

例如：> AnalysisLog-r2-x64.exe java|python&2.7
就会找出包含java的行，并写入java.log文件中；还会找出包含python并且包含2.7关键字的行，并写入python&2.7.log的文件中
