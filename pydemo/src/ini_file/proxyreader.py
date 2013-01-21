'''
Created on 2013-1-16

@author: wang_peng
'''
import ConfigParser, os

def getNewProxy(flag):
    proxyinifile = "proxy.ini"
        
    proxycfg = ConfigParser.ConfigParser()
    proxycfg.read(proxyinifile)
    
    sections = proxycfg.sections()
    print sections
    if flag > len(sections) : flag %= len(sections)
    
    return proxycfg.get(sections[flag], "host"),proxycfg.get(sections[flag], "port"),proxycfg.get(sections[flag], "user"),proxycfg.get(sections[flag], "pass")
    
print getNewProxy(1)