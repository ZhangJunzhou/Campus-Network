#!/usr/bin/env python
# coding=utf-8
from urllib import parse
from urllib import request
from urllib.request import urlopen
import urllib
import getpass

def login(username,password):
    posturl="http://10.3.8.211/"
    header={"User-Agent":"Mozilla/5.0 (compile;MSIE 10.0; Windows NT 6.1; Trident/6.0)",
    "Referer":"http://10.3.8.211/"
        }
    postdata={
    "user":username,
    "pass":password,
    "savePWD":"0",
    "0MKKey":""
        }
    postData = parse.urlencode(postdata).encode("utf-8")
    req = request.Request(posturl,postData,header)
    try:
        response = urlopen(req)
        print("Login success")
    except urllib.error.URLError as e:
        print("Login Failed")
if __name__ == '__main__':
    name = input("please input the username:")
    password = getpass.getpass("Password:")
    name = name.strip()
    login(name,password)
