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

class spider_vedioInfo():
    vedio_Linklist = []  # 视频链接列表
    # vedio_Timelist = []  # 对应发布时间列表
    video_Info = []    #视频列表

    savepath = ''
    findVedioTime = re.compile(r'(.*?)</span>')  # 视频时间的正则表达式
    findVedioCollectTime = re.compile(r'<a href="(.*?)"')

    findVideoName = re.compile(r'<h1.*title="(.*?)"',re.S)  #名字
    findVideoUp = re.compile(r'target="_blank">(.*?)<span class="mask"></span>',re.S)  # up主
    findVideoName2=re.compile(r'<h1.*>(.*?)</h1>',re.S)  #名字
    findVideoIntrod = re.compile(r'<span class="desc-info-text">(.*?)</span>',re.S)  # 简介
    findVideoTag2 = re.compile(r'</svg>(.*?)</a>',re.S)  #标签
    findVideoTag1 = re.compile(r'<span>(.*?)</span>',re.S)  # 标签
    findVideoTag3 = re.compile(r'<a class="tag-link" href=.* target="_blank">(.*?)</a>',re.S)  # 标签
    findVideoLike = re.compile(r'<span class="like" title="点赞数(.*?)">')   #点赞
    findVideoCone = re.compile(r'<span class="info-text">(.*?)</span>',re.S)   #投币
    findVideoTransmit = re.compile(r'</svg><span class="info-text">(.*?)</span></span>',re.S)   #转发
    findVideoCollect = re.compile(r'<span class="info-text">(.*?)</span>',re.S)  #收藏
    findVideoImg = re.compile(r'content="(.*?)".*>',re.S)  #图片

    def __init__(self, linklist, savepath):
        self.vedio_Linklist = linklist
        self.savepath = savepath
        # self.vedio_Timelist=[]
        self.video_Info=[]

    def GET_Vedio_Info(self):
        flg=1
        for lk in self.vedio_Linklist:
            # print(self.vedio_Linklist.index(i))
            self.Get_Vedio_Info_S(flg,lk)
            flg = flg + 1
        self.saveData()
        return self.video_Info

    def Get_Vedio_Info_S(self, flg,baseurl):
        self.getData(flg,baseurl)

    def getData(self,flg, baseurl):
        data = []
        data.append(flg)   #标号
        data.append("https:" + baseurl)  #链接
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

        img_s = soup.find_all(name="meta", attrs={"itemprop": "image"})
        print(img_s)
        img = "null"
        if img_s!=[]:
            img = re.findall(self.findVideoImg, str(img_s[0]))[0]
        print("img: ",img)
        data.append(img)
        s =  soup.find_all(name="span", attrs={"class": "pudate item"})

        title_s = soup.find_all(name="h1",attrs={"class": "video-title tit"})
        # print('title_s: ',title_s)
        name = "null"
        if len(title_s)!=0:
            print(title_s)
            name = re.findall(self.findVideoName2, str(title_s))[0]
        # print('name:',name)
        data.append(name)

        tags = soup.find_all(name="li",attrs={"class":"tag"})

        tag_list="null"
        if(len(tags)!=0):
            for item in tags:
                # print('tags: ', item)
                tag1 = re.findall(self.findVideoTag1, str(item))
                tag2 = re.findall(self.findVideoTag2, str(item))
                tag3 = re.findall(self.findVideoTag3, str(item))
                if tag1!=[]:
                    tag_list = tag_list + tag1[0].strip() + " "
                    # print(tag1[0])
                elif tag2!=[]:
                    tag_list = tag_list + tag2[0].strip() + " "
                    # print(tag2[0])
                elif tag3!=[]:
                    tag_list = tag_list + tag3[0].strip() + " "
                    # print(tag3[0])
                else:
                    continue
        data.append(tag_list)
        # print('tag_list: ',tag_list)
        time = "null"
        if (len(s) != 0):
            for item in s:
                # 【测试】查看item全部信息
                # print("ITEM",str(item))
                item = str(item)
                time = re.findall(self.findVedioTime, item)[0].strip()  # re库用来通过正则表达式查找指定的字符串
        data.append(time)
        # print('time: ',time)

        up_s = soup.find_all(name="div",attrs={"class": "name"})
        up_name = "null"
        # print(up_s)
        if len(up_s)!=0:
            up_name = re.findall(self.findVideoUp,str(up_s))[0].strip()
        # print('up_name',up_name)
        data.append(up_name)

        intro_s = soup.find_all(name="div",attrs={"class": "desc-info desc-v2"})
        introduction = "null"
        if len(intro_s)!=0:
            introduction = re.findall(self.findVideoIntrod,str(intro_s))[0].strip()
        data.append(introduction)
        # print('introduction: ',introduction)

        like_s = soup.find_all(name="span",attrs={"class": "like"})
        # print('like_s',like_s[0])
        coin_s = soup.find_all(name="span",attrs={"class": "coin"})
        # print('coin_s', coin_s)
        collect_s = soup.find_all(name="span", attrs={"class": "collect"})
        # print('collect_s', collect_s)
        transmit_s = soup.find_all(name="span", attrs={"class": "share"})
        # print('transmit_s', transmit_s)
        like = "null"
        coin = "null"
        collect = "null"
        transmit = "null"
        if len(like_s)!=0:
            like = re.findall(self.findVideoLike, str(like_s[0]))[0]
        if len(coin_s)!=0:
            coin = re.findall(self.findVideoCone, str(coin_s[0]))[0]
        if len(collect_s) != 0:
            collect = re.findall(self.findVideoCollect, str(collect_s[0]))[0]
        if len(transmit_s) != 0:
            transmit = re.findall(self.findVideoTransmit, str(transmit_s[0]))[0]
        data.append(like)
        data.append(coin)
        data.append(collect)
        data.append(transmit)
        # 【测试】爬取是否正确
        # print(time,"time-----------------------------------------")
        # data.append(link)                       #添加链接

        print(data)
        self.video_Info.append(data)  # 把处理好的一部电影信息放入datalist

    def saveData(self):
        print("save....")
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
        sheet = book.add_sheet('热门视频top100投放时间', cell_overwrite_ok=True)  # 创建工作表
        col = ("视频id", "链接", "图片","视频名", "标签", "投放时间", "up主", "简介", "点赞数", "投币数", "收藏数", "转发数")

        for i in range(0, 12):
            sheet.write(0, i, col[i])  # 列名
        for i in range(0, 100):
            # 【测试】查看data
            print("第%d条" % (i + 1))
            data = self.video_Info[i]
            for j in range(0, 12):
                sheet.write(i+1, j, data[j])  # 数据

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
