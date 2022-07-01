# -*- codeing = utf-8 -*-
# @Time :2022/6/25 10:13
# @Author:nkx
# @File : linkAnalys.py
# @Software: PyCharm
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作
from io import BytesIO
import gzip
import requests
import json
import time
import LinkAnalysis.Tools.cacu_DeltaT as cacu_DeltaT
import LinkAnalysis.Tools.cnt_DeltaT as cnt_DT
import jieba
from LinkAnalysis.Tools.spider_videoComment import scrape_url
import collections
stop_path="./LinkAnalysis/stopwords.txt"
class LinkAnls():

    video_Link = ""         #视频
    video_Time = ""         #视频投放时间
    video_BV = ""           #视频BV号
    video_P = 0             #视频分p号
    video_DanmakuText = ""  #视频弹幕内容(用于弹幕关键词统计)
    video_DanmakuDTC = []  #视频弹幕时间(用于量化弹幕发送时间)
    danmaku_keywords = []
    comment_keywords = []
    video_img =""
    video_name = ""
    video_Tags = ""
    video_upname = ""
    like = ""
    coin = ""
    collect = ""
    trans = ""
    Intro = ""
    video_comment = []
    allinfo = {}
    #video_html = ""         #该视频对应页面的html源文件爬取

    def __init__(self,link):
        self.comment_keywords=[]
        self.video_Link = link+'?'
        self.get_BVP()

    #获取视频的BV号和分P号
    def get_BVP(self):
        findVedio_BV = re.compile(r'video/(.*?)\?')
        #findVedio_BV2 = re.compile(r'video/(.*?)')
        find_P = re.compile(r'p=(.*)')
        self.video_BV = re.findall(findVedio_BV,self.video_Link)[0]
        p = re.findall(find_P,self.video_Link)
        if len(p):
            self.video_P = int(p[0])-1
        #【测试】验证bv号和频数正确
        #print(self.video_BV,self.video_P)



    def askURL(self,Baseurl):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome "
                          "/ 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67 "
        }
        #Baseurl = self.video_Link
        # print(Baseurl)
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

    def getData(self):

        html = self.askURL(self.video_Link)
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
        #self.Find_keywords()
        #print("keywords", self.danmaku_keywords)

        self.getTime(soup)
        # self.getDanmaku()
        # self.Find_keywords()
        self.getImg(soup)
        self.getName(soup)
        self.getTags(soup)
        self.getUp(soup)
        self.getLike(soup)
        self.getCoin(soup)
        self.getCollect(soup)
        self.getTrans(soup)
        self.getIntro(soup)
        self.getComment()
        self.allinfo = {'up': self.video_upname, 'like': self.like, 'name': self.video_name, 'img': self.video_img,
                        'tag': self.video_Tags, 'time': self.video_Time, 'coin': self.coin, 'trans': self.trans,
                        'intro': self.Intro, 'collect': self.collect}
        #print(self.video_DanmakuText)
        #print("video_DanmakuDTC",self.video_DanmakuDTC)
        #print("keywords", self.danmaku_keywords)

        print("video_Time",self.video_Time)
        print("video_DanmakuDTC",self.video_DanmakuDTC)
        print("keywords",self.danmaku_keywords)
        print("comment",self.comment_keywords)
        print("img",self.video_img)
        print("name",self.video_name)
        print("tag",self.video_Tags)
        print("up",self.video_upname)
        print("like",self.like)
        print("coin",self.coin)
        print("collect",self.collect)
        print("trans",self.trans)
        print("Intro",self.Intro)
        print("Comment",self.video_comment)




        #return soup
    def getUp(self,soup):
        findVideoUp = re.compile(r'target="_blank">(.*?)<span class="mask"></span>', re.S)  # up主
        up_s = soup.find_all(name="div", attrs={"class": "name"})
        # print(up_s)
        if len(up_s) != 0:
            self.video_upname = re.findall(findVideoUp, str(up_s))[0].strip()
        return self.video_upname

    def getImg(self,soup):
        findVideoImg = re.compile(r'content="(.*?)".*>', re.S)  # 图片
        img_s = soup.find_all(name="meta", attrs={"itemprop": "image"})
        img = ""
        if img_s != []:
            img = re.findall(findVideoImg, str(img_s[0]))[0]
        self.video_img = img
        return self.video_img

    def getName(self,soup):
        findVideoName = re.compile(r'<h1.*title="(.*?)"', re.S)  # 名字
        title_s = soup.find_all(name="h1", attrs={"class": "video-title tit"})
        # print('title_s: ',title_s)
        if len(title_s) != 0:
            self.video_name = re.findall(findVideoName, str(title_s))[0]
        return self.video_name

    def getTags(self,soup):
        findVideoTag2 = re.compile(r'</svg>(.*?)</a>', re.S)  # 标签
        findVideoTag1 = re.compile(r'<span>(.*?)</span>', re.S)  # 标签
        findVideoTag3 = re.compile(r'<a class="tag-link" href=.* target="_blank">(.*?)</a>', re.S)  # 标签
        tags = soup.find_all(name="li", attrs={"class": "tag"})

        if len(tags) != 0:
            for item in tags:
                # print('tags: ', item)
                tag1 = re.findall(findVideoTag1, str(item))
                tag2 = re.findall(findVideoTag2, str(item))
                tag3 = re.findall(findVideoTag3, str(item))
                if tag1 != []:
                    self.video_Tags += tag1[0].strip() + " "
                    # print(tag1[0])
                elif tag2 != []:
                    self.video_Tags += tag2[0].strip() + " "
                    # print(tag2[0])
                elif tag3 != []:
                    self.video_Tags += tag3[0].strip() + " "
                    # print(tag3[0])
                else:
                    continue
        self.video_Tags=self.video_Tags.strip()
        return self.video_Tags

    def getTime(self,soup):

        findVedioTime = re.compile(r'(.*?)</span>')  # 视频时间的正则表达式
        s = soup.find_all(name="span", attrs={"class": "pudate item"})
        if len(s)==0 :
            self.video_Time = "null"

        for item in s:
            # 【测试】查看item全部信息
            # print("ITEM",str(item))

            item = str(item)
            time = re.findall(findVedioTime, item)[0].strip()  # re库用来通过正则表达式查找指定的字符串
            # 【测试】爬取是否正确
            #print(time,"time-----------------------------------------")
            # data.append(link)                       #添加链接
            self.video_Time = time  # 把处理好的一部电影信息放入datalist
        return self.video_Time

    def getDanmaku(self):

        cid = self.getCID()
        baseurl = "https://comment.bilibili.com/" + str(cid) + ".xml"

        #print(cid,baseurl)
        finddanmakuTime = re.compile(r'<d p="(.*?)">')  # 弹幕时间的正则表达式
        finddanmakuText = re.compile(r'">(.*?)</d>')  # 弹幕内容爬取正则

        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome "
                          "/ 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67 "
        }
        html = requests.get(baseurl,headers=head).text.encode('iso-8859-1').decode('utf-8')
        soup = BeautifulSoup(html, "html.parser")

        for item in soup.find_all(name="i"):
            # 【测试】查看item全部信息
            #print("ITEM",str(item))

            item = str(item)
            attr = re.findall(finddanmakuTime, item) # re库用来通过正则表达式查找指定的字符串
            attr2 = re.findall(finddanmakuText, item)
            #【测试】爬取是否正确
            #print(len(attr))
            video_DanmakuDT = []
            for at in attr:
                ilist = at.split(',')
                #【测试】
                #print(ilist[4],file=testf)
                #【工具】 将unix格式的时间转化成本地时间
                time_local = time.localtime(int(ilist[4]))
                #【工具】转换成新的时间格式
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

                #print(self.vedio_TimeList[i],Time)

                deltaT = cacu_DeltaT.cacu_DeltaT(self.video_Time,Time)
                video_DanmakuDT.append([1,deltaT])
                video_DanmakuDT.sort()

            self.video_DanmakuDTC = cnt_DT.cnt_DeltaT(video_DanmakuDT).get_cntDeltaT()
            for i in self.video_DanmakuDTC:
                del i[0]

            for i in attr2:
                self.video_DanmakuText += '\n' + i
        return self.video_DanmakuDTC

    def getCID(self):
        url_video = "https://api.bilibili.com/x/player/pagelist?bvid="+self.video_BV+"&jsonp=jsonp"
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome "
                          "/ 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67 "
        }
        video = requests.get(url=url_video, headers=head)
        video_info = json.loads(video.text)
        cid = video_info["data"][self.video_P]["cid"]
        #print(cid)
        return cid

    def getLike(self,soup):
        findVideoLike = re.compile(r'<span class="like" title="点赞数(.*?)">')  # 点赞
        like_s = soup.find_all(name="span", attrs={"class": "like"})
        if len(like_s) != 0:
            self.like = re.findall(findVideoLike, str(like_s[0]))[0]

    def getCoin(self,soup):
        findVideoCoin = re.compile(r'<span class="info-text">(.*?)</span>',re.S)   #投币
        coin_s = soup.find_all(name="span",attrs={"class": "coin"})
        if len(coin_s) != 0:
            self.coin = re.findall(findVideoCoin, str(coin_s[0]))[0]

    def getCollect(self,soup):

        findVideoCollect = re.compile(r'<span class="info-text">(.*?)</span>',re.S)  #收藏  #投币
        collect_s = soup.find_all(name="span", attrs={"class": "collect"})
        if len(collect_s) != 0:
            self.collect = re.findall(findVideoCollect, str(collect_s[0]))[0]

    def getTrans(self,soup):

        findVideoTransmit = re.compile(r'</svg><span class="info-text">(.*?)</span></span>',re.S)   #转发
        transmit_s = soup.find_all(name="span", attrs={"class": "share"})
        if len(transmit_s) != 0:
            self.trans = re.findall(findVideoTransmit, str(transmit_s[0]))[0]

    def getIntro(self,soup):
        findVideoIntrod = re.compile(r'<span class="desc-info-text">(.*?)</span>', re.S)  # 简介
        intro_s = soup.find_all(name="div", attrs={"class": "desc-info desc-v2"})
        if len(intro_s) != 0:
             self.Intro = re.findall(findVideoIntrod, str(intro_s))[0].strip()

    def Find_keywords(self):

        # 文本预处理  去除一些无用的字符   只提取出中文出来
        new_data = re.findall('[\u4e00-\u9fa5]+', self.video_DanmakuText, re.S)
        new_data = ",".join(new_data)
        #【测试】查看文本预处理结果
        #print(new_data)
        # 文本分词
        seg_list_exact = jieba.cut(new_data, cut_all=True)
        #print(list(seg_list_exact))
        result_list = []

        stop_words = set()
        with open(stop_path, encoding='utf-8') as f:
            con = f.readlines()
            for i in con:
                i = i.replace("\n", "")  # 去掉读取每一行数据的\n
                stop_words.add(i)

        for word in list(seg_list_exact):
            #print(word,word in stop_words)
            # 设置停用词并去除单个词
            if word not in stop_words and len(word)>1:
                result_list.append(word)

        #【测试】查看分词结果
        #print(result_list)

        # 筛选后统计
        word_counts = collections.Counter(result_list)
        # 获取前30高频的词
        word_counts_top30 = word_counts.most_common(50)
        #【测试】查看筛词结果
        #print(word_counts_top30)
        self.danmaku_keywords = word_counts_top30


    def getComment(self):
        comment=""
        coms = scrape_url(self.video_Link)
        self.video_comment = coms
        for data in coms:
            #self.video_comment.append(data['massage'])
            comment = comment + data['massage'] + " "

        word_list = jieba.cut(comment.strip('\n'), cut_all=False)
        keyword_lst=[]
        #去除停用词
        stop_words = set()
        with open(stop_path, encoding='utf-8') as f:
            con = f.readlines()
            for i in con:
                i = i.replace("\n", "")  # 去掉读取每一行数据的\n
                stop_words.add(i)
        for word in list(word_list):
            if word not in stop_words and len(word) > 1:
                keyword_lst.append(word)
        #print(comment)
        c = collections.Counter()
        for word in keyword_lst:
            if len(word) > 1 and word != '\r\n':
                c[word] += 1
        k = list(c.keys())

        v = list(c.values())

        for i in range(len(k)):
            self.comment_keywords.append((k[i],v[i]))
#l = LinkAnls('https://www.bilibili.com/video/BV1rY4y1J7Mt')
#l.getData()
