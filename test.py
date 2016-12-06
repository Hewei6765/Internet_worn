#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
import urllib
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'}
img_url = 'http://www.xiaohuar.com/d/file/20161128/0f13f6d6eec25bbe944d3a130db017ef.jpg'
req = urllib.request.Request(url=img_url, headers=headers)
f = open("hua.jpg",'wb')
f.write(urllib.request.urlopen(req).read())
f.close()