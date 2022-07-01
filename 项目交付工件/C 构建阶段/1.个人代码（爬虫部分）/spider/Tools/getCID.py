# -*- codeing = utf-8 -*-
# @Time :2022/6/21 16:09
# @Author:Trump
# @File : getCID.py
# @Software: PyCharm
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import ast
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
from spider_vedioLink import spider_vedioLink
from io import BytesIO
import gzip

class getCID():
    vedio_CID = []
    #savepath = 'C:/Users/Anning/Desktop/美食视频CID.txt'
    baseurl = ""
    findVedioCid = re.compile(r'"cid":(.*?),')
    findVedioOther=re.compile(r'"others":(.*?),"open"')
    findVedioOtherCid=re.compile(r'"cid":(.*?),')

    def __init__(self,baseurl):
        self.baseurl=baseurl
        self.vedio_CID=[]
        #self.getData()

    def getData(self):

        html = self.askURL()
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
        for item in soup.find_all(name="script"):
            # 【测试】查看item全部信息
            #print("ITEM",str(item))

            item = str(item)
            allcid = re.findall(self.findVedioCid, item) # 所有cid
            other = re.findall(self.findVedioOther,item) #other字段
            othercid=[] #other字段中的cid

            if(len(allcid)):

                #【测试】查看所有cid
                #print(allcid)
                #print(len(allcid))

                for i in other:
                    cid = re.findall(self.findVedioOtherCid,i) #在other字段中寻找cid
                    othercid.extend(cid)

                topcid = list(set(allcid)-set(othercid)) #在所有cid中去掉other中的cid,保证cid是top100的cid
                topcid.sort(key=allcid.index)  #与排行榜页排序一致
                self.vedio_CID=topcid #添加自身属性
        return self.vedio_CID


    def askURL(self):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome "
                          "/ 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67 "
        }
        request = urllib.request.Request(self.baseurl, headers=head)
        html = ""
        # 异常处理
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf-8')
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        return html

