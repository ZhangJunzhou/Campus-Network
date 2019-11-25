#!/usr/bin/env python
# coding=utf-8
from urllib import request
from urllib.request import urlopen
import urllib

def logout():
    posturl="http://10.3.8.211/logout"
    header={"User-Agent":"Mozilla/5.0 (compile;MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Referer":"http://10.3.8.211/logout"
        }
    req = request.Request(posturl,headers=header)
    try:
        response = urlopen(req)
        print("Logout success")
    except urllib.error.URLError as e:
        print("Logout failed")

if __name__ == '__main__':
    logout()
