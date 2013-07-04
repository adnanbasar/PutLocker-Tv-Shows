from flask import Flask,request


from parse_rest.connection import register
from parse_rest.datatypes import Object
from bs4 import BeautifulSoup
import urllib2
import sys,os
reload(sys)
sys.setdefaultencoding('utf-8')


def video(link,name):
    try:
        f= urllib2.urlopen(link)
    except urllib2.URLError:
        return False
    x=f.read()
    soup = BeautifulSoup(x)
    try:
        print name,soup.iframe['src']
    except TypeError:
        pass

def tv_show(link):
    try:
        f= urllib2.urlopen(link)
    except urllib2.URLError:
        return False
    x=f.read()
    soup = BeautifulSoup(x)
    for i in soup.find_all('a'):
        if i['class'][0]=='la' and '/watch/' in i['href']:
            name=i['href'].split('/')[-2]+' '+i['href'].split('/')[-1].replace('.html','')
            link='http://streamallthis.ch'+i['href'].replace(i['href'].split('/')[-1],'i/'+i['href'].split('/')[-1])
            video(link,name)



def tv_shows(link):
    try:
        f= urllib2.urlopen(link)
    except urllib2.URLError:
        return False
    x=f.read()
    soup = BeautifulSoup(x)
    for i in soup.find_all('a'):
        if i['class'][0]=='lc':
            tv_show('http://streamallthis.ch'+i['href'])
            


    
tv_shows('http://streamallthis.ch/tv-shows-list.html')





    


    








