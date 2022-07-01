# -*- codeing = utf-8 -*-
# @Time :2022/6/21 9:50
# @Author:nkx
# @File : spider_vedioLink.py
# @Software: PyCharm

from bs4 import BeautifulSoup     #网页解析，获取数据
import re       #正则表达式，进行文字匹配
import urllib.request,urllib.error      #制定URL，获取网页数据
import xlwt     #进行excel操作
import sqlite3  #进行SQLite数据库操作

class spider_vedioLink:

    #视频链接的正则表达式
    findLink = re.compile(r'href="(.*?)"')
    baseurl = ""
    datalist=[]
    savepath = ''


    def __init__(self,baseurl,savepath):
        self.baseurl=baseurl
        self.savepath=savepath
        self.datalist=[]

    #【实现】获取+爬取+存储
    def GET_vedio_Link(self):

        #爬取网页
        self.getData()

        #【测试】查看爬取结果
        #print("DATALIST")
        #print(datalist)
        #保存数据

        self.saveData()
        return self.datalist


    #【功能】爬取网页，获取视频链接列表
    def getData(self):
        for i in range(0,1):       #调用获取页面信息的函数，10次
            html = self.askURL()      #保存获取到的网页源码

            #【测试】打印网页源码
            #f=open('C:/Users/Anning/Desktop/html.txt','w',encoding='utf-8')
            #print(html,file=f);
            #f.close()

            #解析数据
            soup = BeautifulSoup(html,"html.parser")

            #【测试】打印soup
            #ff = open('C:/Users/Anning/Desktop/soup.txt', 'w', encoding='utf-8')
            #print(soup, file=ff);
            #ff.close()

            #for item in soup.find_all('div',class_="item"):     #查找符合要求的字符串，形成列表

            for item in soup.find_all(attrs = {"class": "info"}):

                # 【测试】查看视频item全部信息
                # print("ITEM",str(item))

                #data = []    #保存一部视频的链接

                item = str(item)

                #影片详情的链接
                link = re.findall(self.findLink,item)[0]     #re库用来通过正则表达式查找指定的字符串
                #data.append(link)                       #添加链接

                self.datalist.append(link)       #把处理好的一部电影信息放入datalist
            #print(self.datalist)

    #【功能】得到网页内容
    def askURL(self):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67"
        }

        request = urllib.request.Request(self.baseurl,headers=head)
        html = ""
        #异常处理
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode("utf-8")
            #print(html)
        except urllib.error.URLError as e:
            if hasattr(e,"code"):
                print(e.code)
            if hasattr(e,"reason"):
                print(e.reason)
        return html

    #【功能】保存数据到表中
    def saveData(self):
        #print("save....")
        #print(self.datalist)
        book = xlwt.Workbook(encoding="utf-8",style_compression=0)  #创建workbook对象
        sheet = book.add_sheet('热门美食视频top100链接',cell_overwrite_ok=True)    #创建工作表
        col = ["视频链接"]
        for i in range(0,1):
            sheet.write(0,i,col[i]) #列名
        for i in range(0,100):

            #【测试】查看data
            #print("第%d条" %(i+1))
            data = self.datalist[i]
            #print(data)

            #存储数据
            for j in range(0,1):
                sheet.write(i+1,j,data)      #数据

        book.save(self.savepath)       #保存


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
#sp=spider_vedioLink("https://www.bilibili.com/v/popular/rank/food","C:/Users/Anning/Desktop/美食top100视频链接.xls")
#sp.GET_vedio_Link()