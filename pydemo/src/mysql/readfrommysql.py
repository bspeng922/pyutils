'''
Created on 2013-2-22

@author: wang_peng
'''
import sys
import MySQLdb
import MySQLdb.cursors

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
    
    try: 
        #return as a set , so we can visit it by its name
        conn = MySQLdb.connect(host=dbhost,user=dbuser, passwd=dbpasswd, db=dbname, port=dbport, cursorclass = MySQLdb.cursors.DictCursor)
        sql = "select * from %s"%tablename
        
        cur = conn.cursor()
        rowsreturn = cur.execute(sql)
        
        rs = cur.fetchall()
        
        for row in rs:
            if debug : print "cn: %s"%row["cn"]
            if debug : print "company: %s"%row["company"]
            if debug : print "localtion: %s"%row["localtion"]
            if debug : print "department: %s"%row["department"]
            if debug : print "name: %s"%row["name"]
            if debug : print "displayname: %s"%row["displayname"]
            if debug : print "sAMAccountName: %s"%row["sAMAccountName"]
            if debug : print "mail: %s"%row["mail"]
            if debug : print "title: %s"%row["title"]
            if debug : print "ipPhone: %s"%row["ipPhone"]
            if debug : print "mobile: %s"%row["mobile"]
            if debug : print "ADsPath: %s"%row["ADsPath"]
            if debug : print "whenCreated: %s"%row["whenCreated"]
            if debug : print "lastLogonTimestamp: %s"%row["lastLogonTimestamp"]
            if debug : print "logonCount: %s"%row["logonCount"]
            if debug : print "pwdLastSet: %s"%row["pwdLastSet"]
            if debug : print "badPasswordTime: %s"%row["badPasswordTime"]
            if debug : print "badPwdCount: %s"%row["badPwdCount"]
            if debug : print "whenChanged: %s"%row["whenChanged"]
            if debug : print "userWorkstations: %s"%row["userWorkstations"]
            if debug : print "accountExpires: %s"%row["accountExpires"]
            if debug : print "userAccountControl: %s"%row["userAccountControl"]
            if debug : print "userGroup: %s"%row["userGroup"]
            if debug : print ""
            if debug : print "="*80
            
        if debug : print "%s row(s) returned"%rowsreturn
    except MySQLdb.Error,e:
        if debug : print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        cur.close()
        conn.close()
        if debug : print "finish"
        
    if debug : print "Done"      
    
    

