#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: if_name_main.py
import gzip
import json
from io import BytesIO

import requests
from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作
from http.cookiejar import MozillaCookieJar


def main():
    #爬取网页
    datalist = getData()
    savepath = 'F:/summer_project/douban/spider/douban/b站番剧汇总.xls'

    fLink_list = spiderSecondPage(datalist)
    datalist = spiderThirdPage(fLink_list,datalist)
    saveData(datalist, savepath)

#一个功能对应一个函数
#爬取网页
def getData():
    datalist = []   #将爬取出来的信息临时存放在列表中
    # baseurl=
    for i in range(1,166):       #调用获取页面信息的函数，10次——网页一共有10页，一页25条
        url = "https://api.bilibili.com/pgc/season/index/result?season_version=-1&spoken_language_type=-1&area=-1&is_finish=-1&copyright=-1&season_status=-1&season_month=-1&year=-1&style_id=-1&order=3&st=1&sort=0&page=%d&season_type=1&pagesize=20&type=1"% i     #每一页真正的url
        # print(url)
        html = askURL(url)      #保存获取到的网页源码
        json_html=json.loads(html)
        animelist = json_html['data']['list']
        for item in animelist:
            data=[]
            title = item['title']  # 片名可能只有一个中文名，没有外国名
            data.append(title)

            subTitle = item['subTitle']  # 副标题
            data.append(subTitle)

            link = item['link']  # re库用来通过正则表达式查找指定的字符串
            data.append(link)                       #添加链接

            imgSrc = item['cover']
            data.append(imgSrc)                     #添加图片

            people_num = item['order']    #添加追番人数
            count=re.findall(r"\d+", people_num)
            # print(count)
            data.append(count[0])

            chapters = item['index_show']   #提加章节数
            data.append(chapters)

            score = item['score']  #添加评分
            data.append(score)

            datalist.append(data)       #把处理好的一部电影信息放入datalist

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


#保存数据
def saveData(datalist,savepath):
    print("save....")
    print(datalist)
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('b站番剧汇总',cell_overwrite_ok=True)    #创建工作表
    col = ("剧名","副标题","番剧链接","番剧图片","追番人数/万","全话","评分","标签","上映时间","总播放量")
    for i in range(0,10):
        sheet.write(0,i,col[i]) #列名
    print(len(datalist))
    for i in range(0,len(datalist)):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,10):
            sheet.write(i+1,j,data[j])      #数据

    book.save(savepath)       #保存

#影片详情链接的规则
findLink = re.compile(r'<a class="media-title" href="//(.*)" target.*>')     #创建正则表达式对象，表示规则（字符串的模式）r:忽视所有的特殊符号


def spiderSecondPage(datalist):
    print("spider second page")
    flink_list=[]
    flg=0
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
        flink_list.append(final_link)
    return flink_list

#影片标签
findTags = re.compile(r'<span class="media-tag">(.*)</span>')
findTime = re.compile(r'<span>(.*?)日.*</span>')
findCount=re.compile(r'<em>(.*?)</em>')
findText = re.compile(r'<span class="media-info-intro-text">(.*?)</span>')

def spiderThirdPage(flist,datalist):
    print("spider third page")
    flg=0
    for lk in flist:
        url="https://"+lk+"?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2"
        print(url)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        #标签
        souptmp = soup.find('div', attrs={'class': 'media-info-title'})
        tags_html = souptmp.find_all('span', class_="media-tag")
        tags = ""
        for item in tags_html:
            tag = re.findall(findTags, str(item))
            tags = tags + tag[0] + " "

        datalist[flg].append(tags)

        #开播时间
        souptmp2 = soup.find('div', attrs={'class': 'media-info-time'})
        time_ll = re.findall(findTime,str(souptmp2))

        # print(time)
        if(time_ll==[]):
            time="未开播"
        else:
            time = time_ll[0]+'日'

        datalist[flg].append(time)
        #总播放量
        souptmp3 = soup.find('div', attrs={'class': 'media-info-count'})

        count = re.findall(findCount, str(souptmp3))[0]
        # print(count)
        datalist[flg].append(count)

        # #简介
        # souptmp4 = soup.find('div', attrs={'class': 'media-info-intro'})
        # print(souptmp4)
        # text = re.findall(findText, str(souptmp4))
        # print(text)

        # datalist[flg].append(count)

        print(datalist[flg])
        flg=flg+1

    return datalist
if __name__ == "__main__":          #当程序执行时
#调用函数
    main()
    print("爬取完毕！")



