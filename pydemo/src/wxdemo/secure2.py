# -*- coding: utf-8 -*-

import wx
import random
import time, datetime

__version__ = "0.1"
debug = True    #print debug info
username=""
gender = ""
inputtimeslimit = 100    #times limit
expiretime = 5000    #expire time + 1s

class ValidateFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300,400), style=wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU)
        self.Center()
        self.SetIcon(wx.Icon("secure.ico", wx.BITMAP_TYPE_ICO))
        
        self.panel = wx.Panel(self)
        self.numberoftimes = 1
        self.cmpcount = 0.0
        self.secondscount = 0.0
        self.starttime = datetime.datetime.now()    #use frame start time as starttime
        self.randomset = []
        
        #log file
        self.logfile = open(title.replace(",","_")+".log",'w')
        self.logfile.write(title+"\n")
        
        #random code on the frame
        self.label_random = wx.StaticText(self.panel, -1, self.randcode(), pos=(75, 20))
        self.label_random.SetForegroundColour("Red")
        self.label_random.SetFont(wx.Font(28,wx.DEFAULT,wx.NORMAL, wx.BOLD))
        
        #count of times on the frame
        self.label_numberoftimes = wx.StaticText(self.panel, -1, "The 1th Time", pos=(105, 100))
        
        #clock on the frame
        self.label_timer = wx.StaticText(self.panel, -1, "", pos=(120, 130))
        
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimeChange, self.timer2)
        self.timer2.Start(1000)
        
        #expire time set
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnTimeExpired, self.timer1)
        self.timer1.Start(expiretime)
        
        #gauge on the frame
        self.gauge = wx.Gauge(self.panel, -1, (expiretime-1000)/100, (75,160), (150,20))
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.gaugecount = 0
        
        #textctrl of user input on the frame
        self.textctrl_password = wx.TextCtrl(self.panel, -1, "", pos=(75, 200), size=(150,30), style=wx.PASSWORD)
        
        #numernic button on the frame
        self.button1 = wx.Button(self.panel, -1, "1", pos=(100,234), size=(30,30))
        self.button2 = wx.Button(self.panel, -1, "2", pos=(132,234), size=(30,30))
        self.button3 = wx.Button(self.panel, -1, "3", pos=(164,234), size=(30,30))
        self.button4 = wx.Button(self.panel, -1, "4", pos=(100,266), size=(30,30))
        self.button5 = wx.Button(self.panel, -1, "5", pos=(132,266), size=(30,30))
        self.button6 = wx.Button(self.panel, -1, "6", pos=(164,266), size=(30,30))
        self.button7 = wx.Button(self.panel, -1, "7", pos=(100,298), size=(30,30))
        self.button8 = wx.Button(self.panel, -1, "8", pos=(132,298), size=(30,30))
        self.button9 = wx.Button(self.panel, -1, "9", pos=(164,298), size=(30,30))
        self.buttonr = wx.Button(self.panel, -1, "r", pos=(100,330), size=(30,30))
        self.button0 = wx.Button(self.panel, -1, "0", pos=(132,330), size=(30,30))
        self.buttonc = wx.Button(self.panel, -1, "c", pos=(164,330), size=(30,30))
        
        #bind button event
        self.Bind(wx.EVT_BUTTON, self.OnClearBtnClick, self.buttonr)
        self.Bind(wx.EVT_BUTTON, self.OnDelBtnClick, self.buttonc)
                
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button2)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button3)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button4)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button5)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button6)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button7)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button8)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button9)
        self.Bind(wx.EVT_BUTTON, self.OnNumBtnClick, self.button0)
        
        #bind textctrl event
        self.textctrl_password.Bind(wx.EVT_CHAR, self.KeyPress)
        
    #generate random code
    def randcode(self):
        randomint = random.randint(100000,999999)
        
        if randomint in self.randomset:
            self.randcode()
        else:
            self.randomset.append(randomint)        
            return str(randomint)    
    
    #when seconds change, update the clock
    def OnTimeChange(self, event):
        self.gaugecount += 1
        
        t = time.localtime(time.time())
        st = time.strftime("%I:%M:%S", t)
        self.label_timer.SetLabel(st)
        
        self.gauge.SetValue(self.gaugecount * 10)
        
    #when time expired >4s
    def OnTimeExpired(self, event):
        #check data inputed with random code
        #if debug : print "Time expired"
        currdata = self.textctrl_password.GetValue()
        
        #if current inputed char less than 6 then append space char
        if len(currdata) < 6:
            #if self.starttime == ""  : self.starttime = datetime.datetime.now()
            self.textctrl_password.AppendText(" "*(6-len(currdata)))
        
        self.CheckData()
    
    def BeforeRestart(self):
        #update gauge
        self.gauge.SetValue(0)
        self.gaugecount = 0
        
        #update random code
        self.label_random.SetLabel(self.randcode())
        self.label_numberoftimes.SetLabel("The %sth Time"%self.numberoftimes) 
        self.textctrl_password.SetValue("")
        
        #reset timer
        self.starttime = datetime.datetime.now()  #use restart time as starttimr
        self.timer1.Start(expiretime)
        self.timer2.Start(1000)
        
    
    #when numernic button clicked 
    def OnNumBtnClick(self, event):
        btnchar = event.GetEventObject().GetLabel()    #get label of button
        self.textctrl_password.AppendText(btnchar)
        self.CheckData()
    
    #check user's input  
    def CheckData(self):
        #if len>6 then go next loop
        self.currentvalue = self.textctrl_password.GetValue()
        
        
        if len(self.currentvalue) >= 6:
            self.endtime = datetime.datetime.now()
            self.secondscount += self.DateDiffInSeconds(self.starttime, self.endtime)
                
            #if myinput cmpare random text , count++
            if self.label_random.GetLabel() == self.currentvalue:
                self.cmpcount += 1 
                self.iscmp = "Yes"
            else:
                self.iscmp = "No"
            infostr = "times:%s  --  starttime:%s  --  endtime:%s  --timeused:%ss  --  randomchar:%s  --  mychar:%s  --  iscmp:%s  --  currrate:%s "%(self.numberoftimes, self.starttime, self.endtime,self.DateDiffInSeconds(self.starttime, self.endtime), self.label_random.GetLabel(), self.currentvalue, self.iscmp, self.cmpcount/self.numberoftimes)
                
            if debug : print infostr
            self.logfile.write(infostr + "\n")    
            
            #all data inputed
            if self.numberoftimes < inputtimeslimit:                 
                self.numberoftimes += 1 #number of time plus 1
                #self.label_random.SetLabel(self.randcode()) 
            else:
                totalstr = "avg time: %.5ss    cmp rate: %.5s "%(self.secondscount/self.numberoftimes, self.cmpcount/self.numberoftimes)
                
                #close log file
                self.logfile.write(totalstr)
                self.logfile.close()
                
                #stop the timer
                self.timer1.Stop()
                self.timer2.Stop()
                
                #show message dialog
                msgbox = wx.MessageDialog(None, totalstr,"Statistical information",wx.OK | wx.ICON_INFORMATION)
                if msgbox.ShowModal() == wx.ID_OK:
                    self.Destroy()
            
            #restart a new round        
            self.BeforeRestart()
        else:
            pass   
       
    #get seconds between two times
    def DateDiffInSeconds(self, stime, etime):
        timedelta = etime - stime
        return timedelta.days*24*3600 + timedelta.seconds - 1
    
    #when r button clicked
    def OnClearBtnClick(self, event):
        self.textctrl_password.SetValue("")
    
    #when c button clicked
    def OnDelBtnClick(self, event):
        numinputed = self.textctrl_password.GetValue()
        self.textctrl_password.SetValue(numinputed[:-1])
    
    #get user input
    def KeyPress(self, event):
        keycode = event.GetKeyCode()
        
        if 32<= keycode <= 126:
            self.textctrl_password.AppendText(chr(keycode))
            self.CheckData()
        else:
            #self.textctrl_password.AppendText("")
            event.Skip()


class LoginFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Please Login", size=(300, 200), style=wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU)
        self.Center()
        self.SetIcon(wx.Icon("secure.ico", wx.BITMAP_TYPE_ICO))
        
        self.panel = wx.Panel(self)
        
        #add text label
        self.label_username = wx.StaticText(self.panel, -1, "UserName: ", pos=(30, 30))
        self.label_gender = wx.StaticText(self.panel, -1, "Gender: ", pos=(30, 70))
        
        #add username input box
        self.textctrl_username = wx.TextCtrl(self.panel, -1, "", pos=(100, 30))
        
        #add radio box of gender
        self.genderlist = ['Mr','Mrs']
        self.radio_gender = wx.RadioBox(self.panel, -1,"", (100, 55), wx.DefaultSize, self.genderlist, 2, wx.RA_SPECIFY_COLS)
        self.radio_gender.SetSelection(0)    #the first selected
        
        #add login button and reset button
        self.button_login = wx.Button(self.panel, -1, "Login", pos=(50, 120))
        self.button_reset = wx.Button(self.panel, -1, "Reset", pos=(150, 120))
        
        #bind button event
        self.Bind(wx.EVT_BUTTON, self.OnLoginBtnClick, self.button_login)
        self.Bind(wx.EVT_BUTTON, self.OnResetBtnClick, self.button_reset)
        
        '''not used !'''
        #self.button_login.Disable()    #if username is null, login button will disable
        #self.textctrl_username.Bind(wx.EVT_KEY_DOWN, self.OnKeyPressed)
    
    #when login button clicked
    def OnLoginBtnClick(self, event):
        username = self.textctrl_username.GetValue()    #get username
        gender = self.genderlist[self.radio_gender.GetSelection()]   #get gender 
        
        if debug : print "User info: %s <--> %s"%(username,gender)
        
        #if username not null, show validate frame
        if username <> "" :             
            #show validate frame
            frame2 = ValidateFrame(None, -1, "Welcome, %s %s"%(gender,username))
            frame2.Show()
            
            self.Destroy()    #if username not null
    
    #when user press the keyboard
    def OnKeyPressed(self, event):
        #if debug : print "Key pressed"
        keycode = event.GetKeyCode()
        
        if 32< keycode < 126:
            self.button_login.Enable()
            self.textctrl_username.AppendText(chr(keycode))
    
    #when reset button clicked   
    def OnResetBtnClick(self, event):
        self.textctrl_username.SetValue("")
        if debug : print "reset username"
        self.Refresh()

        
        
if __name__ == "__main__":    
    app = wx.PySimpleApp()
    
    frame = LoginFrame(None, -1)
    frame.Show()
    
    app.MainLoop()