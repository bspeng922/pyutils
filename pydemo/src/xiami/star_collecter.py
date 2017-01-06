# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import time
import urllib2

req_timeout = 5
star_url = "http://www.xiami.com/artist/{star_id}"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36 Vivaldi/1.5.658.56"


def get_star(star_id):
    try:
        req = urllib2.Request(star_url.format(star_id=star_id))
        req.add_header('User-Agent', user_agent)
        resp = urllib2.urlopen(req, None, req_timeout)
    except urllib2.HTTPError:
        print "star( %s ) not exists !" % star_id
        return None
    except Exception, e:
        return None
    soup = BeautifulSoup(resp.read(), "html.parser")
    try:
        name = soup.find('div', id='title').text.strip()
    except:
        name = soup.find('div', id='glory-title').find('h1').text.strip()
    region = soup.find('div', id='artist_info').find_all(valign="top")[1].text.strip()
    trend_tag = soup.find('div', id='artist_trends')
    songs = []
    if trend_tag:
        song_tags = trend_tag.find_all("tr")
        for song_tag in song_tags:
            song = song_tag.select('.song_name')[0].find('a').text.strip()
            hot = song_tag.select('.song_hot')[0].text.strip()
            songs.append((song, hot))
            break
    else:
        song = "NULL"
        hot = 0
        album_tag = soup.find('div', id='artist_album')
        if album_tag:
            albums = album_tag.select('.albumBlock_list')[0].find_all("li")
            for album in albums:
                song = album.select('.name')[0].find('a').text.strip()
                hot = 0
                break
    # get star info from web page
    print star_id, "---", name, "---", \
        region, "---", song, ",", hot
    return name, region, songs


def main():
    # results = requests.get("http://www.xiami.com/artist/1", headers={'User-Agent': user_agent})
    # print results.content

    star_pool = Pool(10)
    for i in range(1630, 10000):
        star_pool.apply(get_star, (i, ))
        # print star_pool.apply(get_star, (i, ))
    star_pool.close()
    star_pool.join()



if __name__ == "__main__":
    start_time = time.time()
    main()
    print "Time used: {second}s".format(second=time.time()-start_time)
