# coding: utf-8
import time
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib import request
import os
import re

# 图片下载的主逻辑函数，获取图片链接，然后传给pic_list()，等结果(其实也没结果，就是等退出)
def picurl(url,path):
    if os.path.exists(path):
        print(path,'目录已存在')
    else:
        print("正在创建目录:%s"%path)
        os.makedirs(path)
    # 获取套图url（图片）地址
    html = ''
    while True:
        html = loadurl(url)
        if html == '':
            continue
        else:
            break
    rePicContent1 = '<div.*?id="picture.*?>.*?<p>(.*?)</p>'
    rePicContent2 = '<div.*?class="postContent.*?>.*?<p>(.*?)</p>'
    rePicList = '<img.*?src="(.*?)".*?>'
    #这里对re.S做个介绍，re.S是可以不添加的，加上之后，它的作用就是能忽略换行符，将两条作为一条来匹配。html代码碰上换行的概率是很高的，所以我一致采用re.S(下文有配图)
    picContent = re.findall(rePicContent1,"%s"%html,re.S)
    if len(picContent) <=0:
        picContent = re.findall(rePicContent2, "%s"%html,re.S)
    if len(picContent) <=0:
        print('无法匹配到对应的图片url')
        return False
    else:
        picList = re.findall(rePicList,"%s"%picContent[0],re.S)
        pic_list(picList,path)

# #这个函数，相当于一个中介，我只是把for循环代码提出就得到了这个函数
def pic_list(picList,path):
    for picurl in picList:
        print("获取图片地址：%s"%picurl)
        save_pic(picurl,path)

#保存图片的逻辑代码块
def save_pic(url,path):
    searchname = '.*/(.*?.jpg)'
    name = re.findall(searchname,url)
    filename = path +'\\'+ name[0]

    print(filename + ':start') #控制台显示信息

    #定义了在下载图片时遇到错误的重试次数
    tryTimes = 3

    #当重试次数没有用完时，则尝试下载
    while tryTimes != 0:
        tryTimes -= 1
        if os.path.exists(filename):
            print(filename,'已存在,跳过')
            return True
        elif os.path.exists(filename):
            os.mknod(filename)
        if download(url,filename):
            break

    if tryTimes != 0:
        print(filename + ": over")
    else:
        print(url + " ：Failed to download")
    #控制台显示信息

#这里是图片保存的代码被调函数，timeout=5设置超时时间，一个500k不到的图片，5秒时间算长的了，超时的话，返回失败

def download(url,filename):

    try:
        send_headers = {
        'Host':'mm.howkuai.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        }
        req = request.Request(url,headers=send_headers)
        conn = urlopen(req,timeout=5)
        f = open(filename,'wb')
        f.write(conn.read())
        f.close()
        return True
    except HTTPError as e:
        print(e)
        return False
    except Exception as e:
        print(e)

def loadurl(url):

    try:
        conn = urlopen(url,timeout=5)
        html = conn.read()
        return html
    except HTTPError as e:
        return ''
    except Exception as e:
        print("unkown exception in conn.read()")
        return ''
