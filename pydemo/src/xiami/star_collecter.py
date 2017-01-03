# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import time
import urllib2

star_url = "http://www.xiami.com/artist/{star_id}"
req_header = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Accept-Language":"zh-CN,zh;q=0.8",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Host":"www.xiami.com",
    "Pragma":"no-cache",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36 Vivaldi/1.5.658.56"
}


def get_star(star_id):
    name = song = play_count = ""
    req_timeout = 5
    req = urllib2.Request(star_url.format(star_id=star_id), None, req_header)
    resp = urllib2.urlopen(req, None, req_timeout)
    soup = BeautifulSoup(resp.read())
    soup.find(id='artist_trends')
    # get star info from web page

    return name, song, play_count


def main():
    star_id = 1
    while 1:
        star_info = get_star(star_id)
        if not star_info:
            break
        print star_info
        star_id += 1


if __name__ == "__main__":
    start_time = time.time()
    main()
    print "Time used: {second}s".format(second=time.time()-start_time)
