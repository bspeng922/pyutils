'''
Created on 2013-1-29

@author: wang_peng
'''
import urllib

debug = True

class Utility:
    @staticmethod
    def ToGB(str):
        if debug : print str
        return str.decode('gb2312')
    
class StockInfo:
    '''get stock information'''

    @staticmethod
    def GetStockStrByNum(num):
        f = urllib.urlopen('http://hq.sinajs.cn/list='+ str(num))
        if debug : print f.geturl()
        if debug : print f.info()
        
        return f.readline()
    
    @staticmethod
    def ParseResultStr(resultstr):
        if debug : print resultstr
        slist = resultstr.split(',')
        name = slist[0][-4:]
        yesterdayendprice = slist[2]
        todaystartprice = slist[1]
        nowprice = slist[3]
        upgraderate = (float(nowprice)-float(yesterdayendprice))/float(yesterdayendprice)
        upgraderate *= 100
        dateandtime = slist[30] + " " + slist[31] 
        
        print "*"*16
        print 'name is : ',name
        print 'yesterday end price is :',yesterdayendprice
        print 'today start price is :',todaystartprice
        print 'now price is :', nowprice
        print 'upgrade rate is :', upgraderate
        print 'date and time is :', dateandtime
        print "*"*16
    
    @staticmethod
    def GetStockInfo(num):
        str = StockInfo.GetStockStrByNum(num)
        strGB = Utility.ToGB(str)
        StockInfo.ParseResultStr(strGB)
        
def Main():
    stocks = ['sh600547', 'sh600151', 'sz000593']

    for stock in stocks:
        StockInfo.GetStockInfo(stock)
        
Main()
        
