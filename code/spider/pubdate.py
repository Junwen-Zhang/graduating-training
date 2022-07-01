#coding:utf-8
import gzip
from io import BytesIO

from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作
import pandas as pd
import numpy as np

findLink = re.compile(r'(20\d{2}([\.\-/|年月\s]{1,3}\d{1,2}){2}日?(\s?\d{2}:\d{2}(:\d{2})?)?)|(\d{1,2}\s?(分钟|小时|天)前)')   #d{4}-d{2}-d{2} d{2}:d{2}:d{2}   .*"(.*?)"

def main():
    URL = pd.read_excel(r'E:\semester3\ref_code\cinephile_url.xls', encoding='gdk')
    URL = np.array(URL)
    line = 0
    path='E:\semester3\\ref_code\\cinephile_date.xls'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('B站视频投放时间', cell_overwrite_ok=True)  # 创建工作表
    col = ("时间")
    sheet.write(0, 0, col[0])  # 列名
    for baseurl in URL:
        baseurl = baseurl[0]
        print(str(line+1)+': '+baseurl)
        line = line+1
    #baseurl = "https://www.bilibili.com/video/BV1gY411T7MA"
        music_date = getData(baseurl)
        if music_date != '0':
            print(music_date[0][0])
            saveData(music_date, path, book, sheet, col, line)



def getData(baseurl):
    #datalist = []
    html = askURL(baseurl)
    soup = BeautifulSoup(html, "html.parser")
    item = soup.find_all('span', class_="pudate item")
    item = str(item)
    if item == '[]':
        print('暂无')
        link = '0'
    else:
        print("item: " + item)
        link = re.findall(findLink, item)
    #datalist.append(link)
    return link #datalist

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

def saveData(date,savepath, book, sheet, col, line):
    print("save....")
    '''book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
    sheet = book.add_sheet('B站视频投放时间',cell_overwrite_ok=True)    #创建工作表
    col = ("时间")'''
    '''for i in range(0,1):
        sheet.write(0,i,col[i]) #列名'''
    print("第%d条" % (line))
    d = date[0]
    sheet.write(line, 0, d[0])
    book.save(savepath)       #保存


if __name__ == "__main__":          #当程序执行时
#调用函数
    main()
    #init_db("movietest.db")
    print("爬取完毕！")