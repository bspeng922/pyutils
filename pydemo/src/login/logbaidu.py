import urllib
import urllib2
import cookielib
import os
import sys
import socket
import re

debug= True

pageStr = """var PagerInfo = {allCount:'(\d+)',pageSize:'(\d+)',curPage:'\d+'}"""
pageObj = re.compile(pageStr, re.DOTALL)

login_tokenstr = """bdPass.api.params.login_token='(.*?)';"""
login_tokenObj = re.compile(login_tokenstr,re.DOTALL)

blogstr = r'''<div class="hide q-username"><a href=".*?" class=a-normal target=_blank>.*?</a></div><a href="(.*?)" class="a-incontent a-title" target=_blank>(.*?)</a></div><div class=item-content>'''
blogObj = re.compile(blogstr, re.DOTALL)

class Baidu():
    def __init__(self, user="", passwd="",blog=""):
        self.user = user
        self.pwd = passwd
        self.blog = blog
        
        if not user or not passwd or not blog:
            if debug: print "please ensure you have inputed all params"
            sys.exit(0)
            
        if not os.path.exists(self.user):
            os.mkdir(self.user)
        
        self.cookiename= "baidu%s.cookie"%self.user
        self.token=""
        self.allCount = 0
        self.pageSize= 10
        self.totalpage = 0
        self.logined = False
        
        self.cj = cookielib.LWPCookieJar()
        try:
            self.cj.revert(self.cookiename)
            self.logined=True
            if debug: print "User(%s) logined..."%self.user
        except Exception, e:
            if debug: print e
            
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        self.opener.addheaders = [('User-agent','Opera/9.23')]
        urllib2.install_opener(self.opener)
        
        socket.setdefaulttimeout(30)
        
    def login(self):
        if not self.logined:
            if debug: print "please login"
            qurl = """https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=false"""
            r = self.opener.open(qurl)
        
        
        

