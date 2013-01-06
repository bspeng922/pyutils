# -*- coding: utf8 -*-
import urllib
import re,os,sys,time


def articleDownload(username,pageCount):
    #判断传入的参数是否合法
    if username == "" : username = "bspeng922"
    if pageCount == "" or int(pageCount)<0 :
        pageCount = 0
    else:
        pageCount = int(pageCount) + 1
    print "Blog: http://hi.baidu.com/new/%s"%username

    #文件保存目录，可修改
    saveDrive = "E:\\test"  #directory to save html files

    #html文件保存目录
    if not os.path.exists(saveDrive) :
        os.mkdir(saveDrive)
    
    mydrive = os.path.join(saveDrive,username)
    if not os.path.exists(mydrive) :
        os.mkdir(mydrive)
        
    #图片保存目录
    imgDir = "img"
    imgPath = os.path.join(saveDrive,username,imgDir)
    if not os.path.exists(imgPath):
        os.mkdir(imgPath)

    #判断传入的页数是否为0，为0则全部下载
    if pageCount == 0 :
        fstbaidu = urllib.urlopen("http://hi.baidu.com/new/%s"%username)    
        totalRecord,pagesize=0,0
    
        for fstline in fstbaidu:        
            if fstline.find("allCount")>0:  #only one tag
                totalRecord = int(fstline[fstline.index("'")+1:fstline.rindex("'")])
            if fstline.find("pageSize")>0:
                pagesize = int(fstline[fstline.index("'")+1:fstline.rindex("'")])
    
            if pagesize != 0 and totalRecord != 0:
                pageCount = totalRecord/pagesize
                if totalRecord / float(pagesize) > totalRecord/pagesize:
                    pageCount = pageCount + 2
        
        fstbaidu.close()
    print "Page Count: ",pageCount - 1 


    
    #根据文章ID获得文章实际链接
    articleCount = 0    
    sumHtmlPath = os.path.join(saveDrive,"%s.html"%username)
    sumfile = open(sumHtmlPath,"w") #the sum file
    aTagCmp = re.compile("""<a href="/%s/item/([\w]*?)" class="a-incontent a-title cs-contentblock-hoverlink" target=_blank>(.*?)</a>"""%username)

    for page in range(1,pageCount):
        thisPageUrl = urllib.urlopen("http://hi.baidu.com/new/%s?page=%d"%(username,page))
        print "Page: ",page
    
        for line in thisPageUrl:
            if line.find("a-incontent a-title")>0 :
                articleCount += 1    #博客文章数目
                linefind = aTagCmp.findall(line)
                #print linefind
            
                for line in linefind :

                    #文章的ID和名称
                    myurl = line[0]
                    mytitle = line[1]
                    sumfile.write("""<a href='%s\\%s.html' target='blank'>%s</a><br>"""%(username,myurl,mytitle))

                    #获得真实的文章，并保存
                    thispath = os.path.join(mydrive,"%s.html"%myurl)
                    thisfile = open(thispath,'w')
                    
                    thisArticle = urllib.urlopen("http://hi.baidu.com/%s/item/%s"%(username,myurl))

                    for thisline in thisArticle:
                        imgCount = 0
                        badImg = 0
                        
                        if thisline.find("content-head clearfix")>0:    #只取正文
                            #匹配图片标签
                            imgTagCmp = re.compile("""<img.*?src="(.*?)".*?>""")
                            imglist = imgTagCmp.findall(thisline)

                            for imglink in imglist :
                                imageNewPath = ""
                                #print imglink

                                if imglink.find("""://""")>0:    #只下载http开头的图片，相对路径的不下载
                                    imageName = imglink[imglink.rindex("/")+1:]

                                    #下载图片
                                    try:
                                        urllib.urlretrieve(imglink,os.path.join(imgPath,imageName))
                                        imgCount += 1
                                    except :    #不能下载则报错
                                        print "cannot download this image: "+imageName

                                    #替换图片链接
                                    imageNewPath = """<img src="%s/%s" />"""%(imgDir,imageName)
                                    thisImgCmp = re.compile("""<img width="\d{1,4}" height="\d{1,4}" src="http://.*?/%s" />|<img src="http://.*?/%s" small="0" />|<img src="http://.*?/%s" />|<img small="0" src="http://.*?/%s" />"""%(imageName,imageName,imageName,imageName))
                                    #print imageNewPath
                                    
                                    try:
                                        #print thisImgCmp.findall(thisline)
                                        thisline = thisImgCmp.sub(imageNewPath,thisline) #每次都对当前图片标签进行替换
                                        #print thisline
                                    except:
                                        print "UnExpect error"

                                else:
                                    badImg += 1
                                    
                            #删除多余的内容
                            pos = thisline.find("mod-post-info clearfix")
                            if pos>0 :
                                thisline = thisline[0:pos-12]

                            thisfile.write(thisline.strip())                

                    thisfile.close()
                    thisArticle.close()
                    #print "Image Count: %d  Bad Image: %d"%(imgCount, badImg)
        thisPageUrl.close()
    sumfile.close()

    print "Article Count: ",articleCount

if __name__ == "__main__":
    st = time.time()

    #获得命令行参数
    if len(sys.argv) == 2:
        uname = sys.argv[1]
        pages = 0
    elif len(sys.argv)>2:
        uname = sys.argv[1]
        pages = int(sys.argv[2])+1
    else:
        uname = raw_input("Username -> ")
        pages = raw_input("Page -> ")

    
    articleDownload(uname,pages)
    et = time.time()
    print "Time used: %0.2fs"%(et-st)
    

