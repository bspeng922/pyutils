import ConfigParser
import os
import sys

debug = True

class MainConfig():
    def __init__(self):
        conf_file = "conf.ini"
        
        if not os.path.exists(conf_file):
            sys.exit(True)
        
        self.cfg = ConfigParser.ConfigParser()
        self.cfg.read(conf_file)
        
    def geticon(self):
        iconpath = ""
        try:
            iconpath = self.cfg.get("MusicPlayer", "icon").strip()
        except ConfigParser.NoSectionError, ConfigParser.NoOptionError:
            if debug: print "  Illegal configure file !"
        finally:
            return iconpath
        
    def getlang(self):
        langcfgpath = ""
        try:
            langcfgpath = self.cfg.get("MusicPlayer","lang").strip()
        except ConfigParser.NoSectionError, ConfigParser.NoOptionError:
            if debug: print "  Illegal configure file !"
        finally:
            return langcfgpath

class MenuConfig():
    def __init__(self):
        conf_menu = ""