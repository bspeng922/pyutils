'''
Created on 2013-2-5

@author: wang_peng
'''
from bs4 import BeautifulSoup
import urllib2


myurl = "http://www.baidu.com"
mypage = urllib2.urlopen(myurl).read()

soup = BeautifulSoup(mypage)
soup.prettify()

print soup.title
soup.title['id'] = 'test'
soup.title['class'] = 'headcss'
print soup.title
print soup.title.attrs

print soup.title.name
print soup.title.string
print soup.title.parent.name

print "*"*30 

print soup.a
print soup.find_all('a')
for link in soup.find_all('a'):
    print link.get('href')

print "*"*30    
headtag = soup.head
print headtag.contents
print headtag.contents[0]
print headtag.contents[0].name
print headtag.contents[0].string

for head in headtag.contents:
    print head
    
print "*"*30

for child in headtag.contents[0].children:
    print child

print "*"*30

for child in headtag.descendants:
    print child
#print soup.get_text()

