# coding: utf-8
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

import meizi_page_download


def loadurl(url):
    # 依旧的，防超时和循环加载
    try:
        conn = urlopen(url,timeout=10)
        html = conn.read()
        return html
    except HTTPError as e:
        print(e)
    except Exception as e:
        print("%s"%e)

#这个函数，简单点就是根据套图链接和传入的路径，得到套图文件夹路径，再传给上一节的图片下载模板
def oneOfSeries(urllist,path):
    searchname = '.*/(.*?).html'
    for url in urllist:
        try:
            name = re.findall(searchname,'%s'%url,re.S)
            current_path = path + '\\' + name[0]
            print("获取套图url本地路径",current_path)
            meizi_page_download.picurl(url,current_path)
        except HTTPError as e:
            print(e)
        except Exception as e:
            print(e)

#传入标签的第n页和文件夹路径，获取所有套图url链接，和分析出对应的文件夹路径，传给我们底层的图片下载模板（也就是上一节啦）
def tag_series(url,path):
    #这里是直接匹配出套图的链接，直接，注意是直接，最好是将结果和源码对下结果，防止遗漏和多出
    reSeriesList = '<div .*?class="pic".*?>.*?<a.*?href="(.*?)".*?target.*?>'
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            continue
        else:
            break
    Pageurl = re.findall(reSeriesList,'%s'%html,re.S)
    if len(Pageurl) ==0:
        pass
    else:
        print("已获取到套图url",Pageurl)
        oneOfSeries(Pageurl,path)