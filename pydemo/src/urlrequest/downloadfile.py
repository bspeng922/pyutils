#-*- coding:utf-8 -*-
import urllib

def callbackinfo(down, block, size):  
        '''''回调函数 
        @down: 已经下载的数据块
        @block: 数据块的大小 
        @size: 远程文件的大小 
        '''  
        per = 100.0 * (down * block) / size  
        if per > 100:  
            per = 100  
        print '%.2f%%' % per  
      
url = 'http://www.sina.com.cn'  
local = 'E:\\sina.html'  
urllib.urlretrieve(url, local, callbackinfo)