'''
Created on 2013-1-4

@author: wang_peng
'''
import ConfigParser

iniFile = "mail.ini"

cfg = ConfigParser.ConfigParser()
cfg.read(iniFile)

for item in cfg.items("MAIL"):
    print item[1]
    
'''get items'''
print cfg.items("MAIL")[0][1]

print cfg.sections()
print cfg.options("MAIL")
print cfg.get("MAIL", "sender")


'rewrite'
cfg.set('MAIL','sender','wang_peng@csm.com.cn')
cfg.write(open('mail.ini','w'))