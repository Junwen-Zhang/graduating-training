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
    #爬取网页
    USA_list = getData1()
    print("USA_list", USA_list)
    other_list = getData2()

    print("other_list",other_list)

    datalist=readdata()
    # print(datalist)
    datalist = matcharea(datalist,USA_list,other_list)
    savepath = 'F:/summer_project/douban/spider/douban/b站番剧汇总2.xls'
    saveData(datalist,savepath)

#一个功能对应一个函数
#爬取网页
def getData1():
    USA_list = []   #将爬取出来的信息临时存放在列表中
    # baseurl=
    for i in range(1,7):       #调用获取页面信息的函数，10次——网页一共有10页，一页25条
        url = "https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=3&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=%d&season_type=1&pagesize=20&type=1"% i     #每一页真正的url
        # print(url)
        html = askURL(url)      #保存获取到的网页源码
        json_html=json.loads(html)
        animelist = json_html['data']['list']
        for item in animelist:
            title = item['title']
            USA_list.append(title)

    return USA_list

def getData2():
    other_list = []
    for j in range(1, 5):
        url = "https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=1%2C4%2C5%2C6%2C7%2C8%2C9%2C10%2C11%2C12%2C13%2C14%2C15%2C16%2C17%2C18%2C19%2C20%2C21%2C22%2C23%2C24%2C25%2C26%2C27%2C28%2C29%2C30%2C31%2C32%2C33%2C34%2C35%2C36%2C37%2C38%2C39%2C40%2C41%2C42%2C43%2C44%2C45%2C46%2C47%2C48%2C49%2C50%2C51%2C52%2C53%2C54%2C55&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page="+str(j)+"&season_type=1&pagesize=20&type=1"
        html = askURL(url)  # 保存获取到的网页源码
        # print(html)
        json_html = json.loads(html)
        # print(json_html)
        animelist = json_html['data']['list']

        for item in animelist:
            # print(item)
            title = item['title']
            other_list.append(title)

    return other_list


#得到指定一个URL的网页内容
def askURL(url):
    head={
        "Referer": "",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",

    }
                            #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url,headers=head)  #使用request封装url和头部信息
    html = ""
    #异常处理
    try:
        response = urllib.request.urlopen(request)
        data = response.read()
        html = data.decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    # print(html)
    return html

def readdata():
    print("reading....")
    readpath = r'F:/summer_project/douban/spider/douban/b站番剧汇总.xls'
    # getdata=pd.read_excel(r'F:/summer_project/douban/spider/douban/b站番剧汇总.xls',sheet_name='b站番剧汇总')
    datalist=xlrd.open_workbook(readpath)
    table=datalist.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols

    r=[]
    for i in range(0,nrows):
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
    sheet = book.add_sheet('b站番剧汇总2',cell_overwrite_ok=True)    #创建工作表
    col = ("剧名", "副标题", "番剧链接", "番剧图片", "追番人数/万", "全话", "评分", "标签", "上映时间", "总播放量","地区")
    for i in range(0, 11):
        sheet.write(0, i, col[i])  # 列名
    print(len(datalist))
    for i in range(1, len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 11):
            sheet.write(i, j, data[j])  # 数据

    book.save(savepath)       #保存


if __name__ == "__main__":          #当程序执行时
#调用函数
    main()
    print("爬取完毕！")



