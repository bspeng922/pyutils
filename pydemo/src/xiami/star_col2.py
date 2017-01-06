# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from multiprocessing import Pool
import requests
import time

req_timeout = 5
pool_size = 10
page_url = "http://i.xiami.com/musician/artists?page={page_id}"
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 " \
             "(KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36"


def get_star(star_url):
    resp = requests.get(star_url, headers={'User-Agent': user_agent})
    soup = BeautifulSoup(resp.content, "html.parser")

    name_tag = soup.find('div', id='title') or \
               soup.find('div', id='glory-title')
    if not name_tag:
        print "Unable to get user by url %s" % star_url
        return
    name = name_tag.find('h1').text.strip()

    region = soup.find('div', id='artist_info').find_all(valign="top")[1].text.strip()

    # get artist most popular song
    trend_tag = soup.find('div', id='artist_trends')
    if trend_tag:
        song_tags = trend_tag.find_all("tr")
        for song_tag in song_tags:
            song = song_tag.select('.song_name')[0].find('a').text.strip()
            hot = song_tag.select('.song_hot')[0].text.strip()
            href = song_tag.select('.song_name')[0].find('a')['href']
            break
    else:
        song = "NULL"
        hot = 0
        album_tag = soup.find('div', id='artist_album')
        if album_tag:
            albums = album_tag.select('.albumBlock_list')[0].find_all("li")
            for album in albums:
                song = album.select('p.name')[0].find('a').text.strip()
                href = album.select('p.name')[0].find('a')['href']
                hot = 0
                break

    print name, "---", region, "---", song, "---", hot, "---", href
    return name, region, song, hot


def get_page_stars(page_id):
    artists = []
    resp = requests.get(page_url.format(page_id=page_id),
                        headers={'User-Agent': user_agent})
    soup = BeautifulSoup(resp.content, "html.parser")
    artists_tag = soup.select(".artists .info a")
    for artist_tag in artists_tag:
        print artist_tag['title'], artist_tag['href']
        artists.append((artist_tag['title'], artist_tag['href']))
    next_page = True if soup.select(".content .loadr a") else False

    return artists, next_page


def main():
    page_id = 1
    artist_pool = Pool(pool_size)
    while 1:
        print "Current page: %s , processing..." % page_id
        artists, has_next = get_page_stars(page_id)
        for artist in artists:
            artist_pool.apply(get_star, (artist[1], ))
        if not has_next:
            break
        page_id += 1
    artist_pool.close()
    artist_pool.join()
    print "total page: %s " % page_id


if __name__ == "__main__":
    start_time = time.time()
    main()
    print "Time used: {second}s".format(second=time.time()-start_time)
