# coding: utf-8
import re
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import meizi_series_getpage


#同样的，这里是加载链接防超时，和上一节一样
def loadurl(url):
    try:
        conn = urlopen(url, timeout=5)
        html = conn.read()
        return html
    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

def nextpage(url,path):
    #获取首页尾部标签
    nextweibu = re.split("/",url)
    # 获取头部文件
    nexthead = re.split("/a/",url)
    nexthead = nexthead[0] + "/a/"


    # 创建首页路径
    path = path+"\\"+nextweibu[-1].split(".",1)[0]
    # 获取html
    while True:
        html = loadurl(url)
        if html == '':
            print('load', url,'error')
            continue
        else:
            break


    # 获取子标签
    mnvtp = BeautifulSoup(html)
    taglists = mnvtp.findAll("div",{"id":"wp_page_numbers"})
    taglists = re.findall('<a.*?href="(.*?)".*?>','%s'%taglists)
    taglists = sorted(list(set(taglists)))
    if taglists == []:
        taglists = [nextweibu[-1]]

    # 获取单个首页所有标签完整url路径
    print("正在获取首页所有子标签Url:%s"%url)
    completeurl = []
    for i in taglists:
        url = nexthead + i
        completeurl.append(url)
    completeurl = sorted(completeurl)
    for i in completeurl:
        print("正在获取子标签下所有图片url路径")
        meizi_series_getpage.tag_series(i,path)
if __name__ == '__main__':
    urllist = ['http://www.meizitu.com/a/xinggan.html', 'http://www.meizitu.com/a/mote.html', 'http://www.meizitu.com/a/bijini.html', 'http://www.meizitu.com/a/nvshen.html', 'http://www.meizitu.com/a/xiaoqingxin.htm', 'http://www.meizitu.com/a/oumei.html', 'http://www.meizitu.com/a/baobei.html', 'http://www.meizitu.com/a/rihan.html', 'http://www.meizitu.com/a/qingchun.html', 'http://www.meizitu.com/a/meizi.html', 'http://www.meizitu.com/a/sifang.html', 'http://www.meizitu.com/a/wangluo.html', 'http://www.meizitu.com/a/luoli.html', 'http://www.meizitu.com/a/qizhi.html']
    urllist = ['http://www.meizitu.com/a/oumei.html']
    path = 'D:\\MeiZi\\'
    for url in urllist:
        nextpage(url,path)