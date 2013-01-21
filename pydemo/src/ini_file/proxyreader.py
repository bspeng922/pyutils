'''
Created on 2013-1-21

@author: wang_peng
'''
import ConfigParser

inifile = "proxy.ini"
cfg = ConfigParser.ConfigParser()
cfg.read(inifile)

print cfg.sections()
print cfg.get(cfg.sections()[0], "host")