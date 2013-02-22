'''
Created on 2013-2-22

@author: wang_peng
'''
import sys
import xlwt
import MySQLdb

debug = True




if __name__ == "__main__":
    dbhost = "localhost"
    dbname = "csm"
    dbuser = "root"
    dbpasswd = "1"
    dbport = 3306
    dbcharset = "utf-8"
    tablename = "domainuser"
    conn = ""
    cur = ""
    resultpath = "E:\\inof.xls"
    currentrow = 1
    
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("domain info")
    #sheet.write()
    
    try: 
        #return as a set , so we can visit it by its name
        conn = MySQLdb.connect(host=dbhost,user=dbuser, passwd=dbpasswd, db=dbname, port=dbport)
        sql = "select * from %s"%tablename
        
        cur = conn.cursor()
        rowsreturn = cur.execute(sql)
        
        rs = cur.fetchall()
        
        for row in rs:
            if debug : print "cn: %s"%row[0]
            if debug : print "company: %s"%row[1]
            if debug : print "localtion: %s"%row[2]
            if debug : print "department: %s"%row[3]
            if debug : print "name: %s"%row[4]
            if debug : print "displayname: %s"%row[5]
            if debug : print "sAMAccountName: %s"%row[6]
            if debug : print "mail: %s"%row[7]
            if debug : print "title: %s"%row[8]
            if debug : print "ipPhone: %s"%row[9]
            if debug : print "mobile: %s"%row[10]
            if debug : print "ADsPath: %s"%row[11]
            if debug : print "whenCreated: %s"%row[12]
            if debug : print "lastLogonTimestamp: %s"%row[13]
            if debug : print "logonCount: %s"%row[14]
            if debug : print "pwdLastSet: %s"%row[15]
            if debug : print "badPasswordTime: %s"%row[16]
            if debug : print "badPwdCount: %s"%row[17]
            if debug : print "whenChanged: %s"%row[18]
            if debug : print "userWorkstations: %s"%row[19]
            if debug : print "accountExpires: %s"%row[20]
            if debug : print "userAccountControl: %s"%row[21]
            if debug : print "userGroup: %s"%row[22]
            if debug : print ""
            if debug : print "="*80
            
            for i in range(0,23):
                sheet.write(currentrow, i, row[i])
            
            currentrow += 1
            
        if debug : print "%s row(s) returned"%rowsreturn
    except MySQLdb.Error,e:
        if debug : print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        cur.close()
        conn.close()
        wb.save(resultpath)
        if debug : print "finish"
        
    if debug : print "Done"      
    
    

