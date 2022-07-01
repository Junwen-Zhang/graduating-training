# -*- codeing = utf-8 -*-
# @Time :2022/6/21 10:31
# @Author:nkx
# @File : spider_vedioTime.py
# @Software: PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
from spider_vedioLink import spider_vedioLink
from io import BytesIO
import gzip


# 【调用】调用视频链接爬取函数
# 【获取】视频链接列表

class spider_vedioTime():
    vedio_Linklist = []  # 视频链接列表
    vedio_Timelist = []  # 对应发布时间列表
    savepath = ''
    findVedioTime = re.compile(r'(.*?)</span>')  # 视频时间的正则表达式
    findVedioCollectTime = re.compile(r'<a href="(.*?)"')

    def __init__(self, linklist, savepath):
        self.vedio_Linklist = linklist
        self.savepath = savepath
        self.vedio_Timelist=[]

    def GET_Vedio_Time(self):
        for i in self.vedio_Linklist:
            # print(self.vedio_Linklist.index(i))
            self.Get_Vedio_Time_S(i)
        self.saveData()
        return self.vedio_Timelist

    def Get_Vedio_Time_S(self, baseurl):
        self.getData(baseurl)

    def getData(self, baseurl):

        html = self.askURL(baseurl)
        # 【测试】打印网页源码
        # f=open('C:/Users/Anning/Desktop/html.txt','w',encoding='utf-8')
        # print(html,file=f);
        # f.close()

        # 解析数据
        soup = BeautifulSoup(html, "html.parser")

        # 【测试】打印soup
        # ff = open('C:/Users/Anning/Desktop/soup.txt', 'w', encoding='utf-8')
        # print(soup, file=ff);
        # ff.close()
        s =  soup.find_all(name="span", attrs={"class": "pudate item"})
        if(len(s)==0):
            self.vedio_Timelist.append("null")
        for item in s:
            # 【测试】查看item全部信息
            # print("ITEM",str(item))

            item = str(item)
            time = re.findall(self.findVedioTime, item)[0].strip()  # re库用来通过正则表达式查找指定的字符串
            # 【测试】爬取是否正确
            # print(time,"time-----------------------------------------")
            # data.append(link)                       #添加链接

            self.vedio_Timelist.append(time)  # 把处理好的一部电影信息放入datalist

    def saveData(self):
        print("save....")
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
        sheet = book.add_sheet('热门美食视频top100投放时间', cell_overwrite_ok=True)  # 创建工作表
        col = ["视频投放时间"]
        for i in range(0, 1):
            sheet.write(0, i, col[i])  # 列名
        for i in range(0, 100):

            # 【测试】查看data
            #print("第%d条" % (i + 1))
            data = self.vedio_Timelist[i]
            #print(data)

            # 存储数据
            for j in range(0, 1):
                sheet.write(i + 1, j, data)  # 数据

        book.save(self.savepath)  # 保存

    def askURL(self, baseurl):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome "
                          "/ 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67 "
        }
        Baseurl = "https:" + baseurl
        #print(Baseurl)
        request = urllib.request.Request(Baseurl, headers=head)
        html = ""
        # 异常处理
        try:
            response = urllib.request.urlopen(request)
            html = response.read()
            buff = BytesIO(html)
            f = gzip.GzipFile(fileobj=buff)
            html = f.read().decode('utf-8')
            # print(html)
        except:
            try:
                response = urllib.request.urlopen(request)
                html = response.read().decode("utf-8")

            except urllib.error.URLError as e:

                if hasattr(e, "code"):
                    print(e.code)
                if hasattr(e, "reason"):
                    print(e.reason)
        return html

# p=spider_vedioTime(vedio_Linklist)
# p.GET_Vedio_Time()
# print(p.vedio_Timelist)
