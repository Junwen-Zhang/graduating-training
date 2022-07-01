#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: if_name_main.py
import gzip
import json
from io import BytesIO

import pandas as pd
import requests
import xlrd
from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作
from http.cookiejar import MozillaCookieJar


def main():
    datalist=readdata()
    dataWithflink=spiderSecondPage(datalist)
    datalist2=getData1(dataWithflink)
    # print(datalist)
    # datalist = matcharea(datalist,USA_list,other_list)
    savepath = 'F:/summer_project/douban/spider/douban/b站番剧汇总3.xls'
    saveData(datalist,savepath)

#一个功能对应一个函数
#爬取网页
findText = re.compile(r'<!DOCTYPE html><html lang="zh-Hans"><head><meta charset="utf-8"><title></title><meta name="description" content="(.*?)">',re.S)
def getData1(dataWithflink):
    print("spider third page")
    flg = 0
    for lk in dataWithflink:
        url = "https://" + lk[-1] + "?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2"
    # url = "https://www.bilibili.com/bangumi/media/md78172/?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2"
        print(url)
        html = askURL2(url)
        f=open('picfile',encoding='UTF-8')
        content=f.read()
        f.close()
        text=" "
        text = re.findall(findText, content)[0]
        otext = text.replace("\n", "")  # 去掉无关的符号
        print(otext)
        dataWithflink[flg].append(otext)
        print(dataWithflink[flg])
        flg = flg + 1

    return dataWithflink

#影片详情链接的规则
findLink = re.compile(r'<a class="media-title" href="//(.*)" target.*>')     #创建正则表达式对象，表示规则（字符串的模式）r:忽视所有的特殊符号


def spiderSecondPage(datalist):
    print("spider second page")
    flg=0
    # flink=[]
    for data in datalist:
        link = data[2]
        # print(link)
        html = askURL(link)
        # print(html)
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        souptmp = soup.find('a', attrs={'class': 'media-title'})
        # print(souptmp)
        final_link = re.findall(findLink,str(souptmp))[0]
        flg = flg + 1
        print(flg)
        print(final_link)
        data.append(final_link)
        # flink.append(final_link)
    return datalist

#得到指定一个URL的网页内容
def askURL(url):
    head={
        "Referer": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/91.0.864.67",
        "Accept-Encoding": "gzip, deflate",
    }
                            #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url,headers=head)  #使用request封装url和头部信息
    html = ""
    #异常处理
    try:
        response = urllib.request.urlopen(request)
        data = response.read()
        # html=data.decode('utf-8')
        if ('Content-Encoding', 'gzip') in response.headers._headers:

            buff = BytesIO(data)
            f = gzip.GzipFile(fileobj=buff)
            html = f.read().decode('utf-8')
        else:
            html = data.decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    # print(html)
    return html


#得到指定一个URL的网页内容
def askURL2(url):
    head={
        "Referer": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",

    }
                            #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    # request = urllib.request.Request(url,headers=head)  #使用request封装url和头部信息

    html = ""
    html = requests.get(url=url, headers=head)
    # html=html.json()
    with open('picfile','wb') as f:
        f.write(html.content)
    f.close()
    # print(html.content)
    #异常处理
    try:
        print()
        # response = urllib.request.urlopen(request)
        # data = response.read()
        # # html=data.decode('utf-8')
        # if ('Content-Encoding', 'gzip') in response.headers._headers:
        #
        #     buff = BytesIO(data)
        #     f = gzip.GzipFile(fileobj=buff)
        #     html = f.read().decode('utf-8')
        # else:
        #     html = data.decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    # print(html)
    return html

def readdata():
    print("reading....")
    readpath = r'F:/summer_project/douban/spider/douban/b站番剧汇总2.xls'
    # getdata=pd.read_excel(r'F:/summer_project/douban/spider/douban/b站番剧汇总.xls',sheet_name='b站番剧汇总')
    datalist=xlrd.open_workbook(readpath)
    table=datalist.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols

    r=[]
    for i in range(1,nrows):
        row_value=table.row_values(i)[0:]
        r.append(row_value)

    return r

def matcharea(datalist,USA_list,other_list):
    print("match....")
    dt_list=datalist
    # usa_count=0
    # other_count=0
    for data in dt_list:
        if data[0] in USA_list:
            # usa_count=usa_count+1
            data.append("American")
            # print(usa_count," : ",data[0],data[-1])
        elif data[0] in other_list:
            # other_count=other_count+1
            data.append("other")
            # print(other_count," : ",data[0], data[-1])
        else:
            data.append("Japan")
    # print(dt_list)
    return dt_list
#保存数据
def saveData(datalist,savepath):
    print("saving....")

    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('b站番剧汇总3',cell_overwrite_ok=True)    #创建工作表
    col = ("剧名", "副标题", "番剧链接", "番剧图片", "追番人数/万", "全话", "评分", "标签", "上映时间", "总播放量","地区","详情页连接","简介")
    for i in range(0, 13):
        sheet.write(0, i, col[i])  # 列名
    print(len(datalist))
    for i in range(0, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 13):
            sheet.write(i + 1, j, data[j])  # 数据

    book.save(savepath)       #保存


if __name__ == "__main__":          #当程序执行时
#调用函数
    main()
    print("爬取完毕！")



