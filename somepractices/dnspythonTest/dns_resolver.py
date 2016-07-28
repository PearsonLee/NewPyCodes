#! /usr/bin/env python
# -*- coding: utf-8 -*-

import dns.resolver
import os
import httplib

iplist = []
appdomain = "www.google.com.hk"

def get_iplist(domain=""):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception, e:
        print "dns resolver error: " + str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            iplist.append(j.address)
    return True

def checkip(ip):
    checkurl = ip + ":80"
    getcontent = ""
    httplib.socket.setdefaulttimeout(5)  # 定义http连接超时时间5s
    conn = httplib.HTTPConnection(checkurl)  # 创建http连接对象
    try:
        conn.request("GET", "/", headers = {"Host": appdomain})  #发起url请求，添加host主机头

        r = conn.getresponse()
        getcontent = r.read(15)  # 获取url页面前15个字符，以便做可用性校验
    finally:
        if getcontent == "<!doctype html>":  # 监控URL页的内容一般是事先定义好的，比如“http 200”等
            print ip + " [ok]"
        else:
            print ip + " [error]"  # 此处可放告警程序，可以是邮件、短信通知

if __name__ == "__main__":
    if get_iplist(appdomain) and len(iplist) > 0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."

