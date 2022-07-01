#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: if_name_main.py
import gzip
from io import BytesIO
from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作


def main():
    baseurl = "https://www.bilibili.com/v/popular/rank/cinephile"
    #爬取网页
    datalist = getData(baseurl)
    #savepath = "豆瓣电影Top250.xls"
    dbpath = "movie.db"
    #保存数据
    savepath='E:\semester3\\ref_code\\cinephile_url.xls'
    saveData(datalist,savepath)
    '''path='E:\semester3\\ref_code\music_date.xls'
    book1 = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet1 = book1.add_sheet('B站视频投放时间', cell_overwrite_ok=True)  # 创建工作表
    for lianjie in datalist:
        d = getData1(lianjie)
        saveData1(d, path, sheet1, book1)'''
    #saveData2DB(datalist,dbpath)

    #askURL("https://movie.douban.com/top250?start=")


#"详情链接","图片链接","视频名称","Up主","浏览量","评论数"
#详情链接的规则
#findLink1 = re.compile(r'<span class="pudate item">.*"(.*?)"</span>')     #创建正则表达式对象，表示规则（字符串的模式）r:忽视所有的特殊符号
findLink = re.compile(r'<a href="(.*?)" target.*>')
'''def getData1(burl):
    datalist = []
    print(111)
        #url = baseurl + str(i*25)
    html = askURL(burl)      #保存获取到的网页源码
    #print(html)
    # 2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    #for item in soup.find_all('div', class_="img"):  # 查找符合要求的字符串，形成列表
    item = soup.find_all('div', class_="video-data")
    # print(item)   #测试：查看电影item全部信息
    data = []  # 保存一部电影的所有信息
    item = str(item)
    print(item)
    # 影片详情的链接
    link = re.findall(findLink1, item)[0]  # re库用来通过正则表达式查找指定的字符串
    data.append(link)
    # 添加链接

    datalist.append(data)  # 把处理好的一部电影信息放入datalist
    return datalist

#保存数据
def saveData1(datalist,savepath,sheet,book):
    print("save....")
    col = ("投放时间")
    for i in range(0,1):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,1):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,1):
            sheet.write(i+1,j,data[j])      #数据

    book.save(savepath)       #保存'''
#图片链接
#findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)   #re.S 让换行符包含在字符中
#视频名称
#findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片评分（Up主）
#findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#浏览量
#findbrowse = re.compile(r'<span >')
#找到评价人数（评论数）
#findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
#findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
#findBd = re.compile(r'<p class="">(.*?)</p>',re.S)



#一个功能对应一个函数
#爬取网页
def getData(baseurl):
    datalist = []
    print(111)
        #url = baseurl + str(i*25)
    html = askURL(baseurl)      #保存获取到的网页源码
    #print(html)
    # 2.逐一解析数据
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.find_all('div', class_="img"):  # 查找符合要求的字符串，形成列表
        # print(item)   #测试：查看电影item全部信息
        data = []  # 保存一部电影的所有信息
        item = str(item)

        # 影片详情的链接
        link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
        #link1 = link.rstrip("\"target=\"_blank")
        data.append('https:'+ link.strip('\\"'))
      #添加链接

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
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('B站视频投放时间',cell_overwrite_ok=True)    #创建工作表
    col = ("详情链接")
    for i in range(0,1):
        sheet.write(0,i,col[i]) #列名
    for i in range(0,100):
        print("第%d条" %(i+1))
        data = datalist[i]
        for j in range(0,1):
            sheet.write(i+1,j,data[j])      #数据

    book.save(savepath)       #保存


# def saveData2DB(datalist,dbpath):
#     init_db(dbpath)
#     conn = sqlite3.connect(dbpath)
#     cur = conn.cursor()
#
#     for data in datalist:
#         for index in range(len(data)):
#             if index == 4 or index == 5:
#                 continue
#             data[index] = '"'+data[index]+'"'
#         sql = '''
#                 insert into movie250 (
#                 info_link,pic_link,cname,ename,score,rated,instroduction,info)
#                 values(%s)'''%",".join(data)
#         print(sql)
#         cur.execute(sql)
#         conn.commit()
#     cur.close()
#     conn.close()
#
#
#
# def init_db(dbpath):
#     sql = '''
#         create table movie250
#         (
#         id integer primary key autoincrement,
#         info_link text,
#         pic_link text,
#         cname varchar,
#         ename varchar,
#         score numeric ,
#         rated numeric ,
#         instroduction text,
#         info text
#         )
#
#     '''  #创建数据表
#     conn = sqlite3.connect(dbpath)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()


if __name__ == "__main__":          #当程序执行时
#调用函数
    main()
    #init_db("movietest.db")
    print("爬取完毕！")