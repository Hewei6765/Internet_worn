# coding: utf-8

import re
import threading
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import meizi_series_nextpage


def loadurl(url):
    try:
        conn = urlopen(url)
        html = conn.read()
        return html
    except HTTPError as e:
        return e
    except Exception as e:
        print("unkown exception in conn.read() %s "%e)
        return ''

def meizi(url,path):
    # 获取首页标签
    print('start open meizitu')
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            print('load', url,'error')
            continue
        else:
            break
    mnvtp = BeautifulSoup(html)
    taglists = mnvtp.findAll("div",{"class":"tags"})
    taglistss = re.findall('<a.*?href="(.*?)".*?>','%s'%taglists)
    #print(list(set(taglistss)))
    #print(len(list(set(taglistss))))
    #print('open meiziwang over')
    #meizi_series_nextpage.nextpage(url,path)
    threads = []
    for url in list(set(taglistss)):
        t =threading.Thread(target=meizi_series_nextpage.nextpage, args=(url, path))
        threads.append(t)
    for t in threads:
        t.start()
    for t in threads:
        t.join()
if __name__ == '__main__':
    meizi('http://www.meizitu.com','D:\\MeiZi\\')
    print ('Spider Stop')
    #meizi_series_nextpage.nextpage('http://www.meizitu.com','D:\\MeiZi\\')