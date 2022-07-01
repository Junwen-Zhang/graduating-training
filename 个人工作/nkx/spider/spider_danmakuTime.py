# -*- codeing = utf-8 -*-
# @Time :2022/6/21 10:14
# @Author:nkx
# @File : spider_danmakuTime.py
# @Software: PyCharm


# 弹幕文件网址“https://comment.bilibili.com/cid.xml”
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlsxwriter  # 进行excel操作
import time
import requests
import Tools.cacu_DeltaT as cacu_DeltaT
import jieba
import collections
from Tools import cnt_DeltaT
import datetime
stop_path="C:/Users/Anning/Desktop/stopwords.txt"

#【测试】cid和对应弹幕unix时间
testf=open('C:/Users/Anning/Desktop/out.txt','w',encoding='utf-8')
class spider_danmakuTime():

    vedio_TimeList = [] #视频发布时间列表
    vedio_Cidlist = []  # 视频CID列表
    vedio_danmakulist = []  # 对应弹幕时间列表
    vedio_deltaTlist = []  #弹幕时间与发布时间差列表
    savepath = ""
    deltaTsavepath = ""
    danmakuTsavepath = ""
    DTcntsavepath = ""
    finddanmakuTime = re.compile(r'<d p="(.*?)">')  # 弹幕时间的正则表达式
    finddanmakuTest = re.compile(r'">(.*?)</d>')  # 弹幕内容爬取正则
    keywords = []
    vedio_danmakuT = ""
    cnt = []

    def __init__(self, cidlist,savepath,vedio_TimeList,deltasavepath,danmakuTsavepath,DTcntsavepath):
        self.vedio_Cidlist = cidlist
        self.savepath=savepath
        self.vedio_danmakulist=[]
        self.vedio_danmakuT=""
        self.keywords=[]
        self.vedio_TimeList = vedio_TimeList
        self.deltaTsavepath = deltasavepath
        self.danmakuTsavepath = danmakuTsavepath
        self.DTcntsavepath = DTcntsavepath
        self.cnt = []
        self.vedio_deltaTlist = []

    def GET_Danmaku_Time(self):
        for i in range(len(self.vedio_Cidlist)):
            #print(i)
            self.Get_Danmaku_Time_S(i)
        #print(self.vedio_deltaTlist,file=testf)
        self.cnt = cnt_DeltaT.cnt_DeltaT(self.vedio_deltaTlist).get_cntDeltaT()
        #print(self.cnt)
        for i in self.cnt:
            #print(i)
            time0 = self.vedio_TimeList[i[0]-1]
            if(time0!="null"):
                VT = datetime.datetime.strptime(time0, "%Y-%m-%d %H:%M:%S")
                # 视频弹幕发布时间
                DT = datetime.timedelta(hours=i[1])
                i[1] = str(VT+DT)

        self.saveData()

    def Get_Danmaku_Time_S(self,i):
        self.getData(i)


    def getData(self, i):
        cid = self.vedio_Cidlist[i]
        #【测试】
        #print(cid,"-------------------------------------",file=testf)
        baseurl="https://comment.bilibili.com/"+cid+".xml"
        #print(baseurl)
        html = self.askURL(baseurl)
        #【测试】打印网页源码
        #f=open('C:/Users/Anning/Desktop/html.txt','w',encoding='utf-8')
        #print(html,file=f);
        #f.close()

        # 解析数据
        soup = BeautifulSoup(html, "html.parser")

        # 【测试】打印soup
        #ff = open('C:/Users/Anning/Desktop/soup.txt', 'w', encoding='utf-8')
        #print(soup, file=ff);
        #ff.close()
        for item in soup.find_all(name="i"):
            # 【测试】查看item全部信息
            #print("ITEM",str(item))

            item = str(item)
            attr = re.findall(self.finddanmakuTime, item) # re库用来通过正则表达式查找指定的字符串
            attr2 = re.findall(self.finddanmakuTest, item)
            #【测试】爬取是否正确
            #print(len(attr))
            # data.append(link)

            for at in attr:
                ilist = at.split(',')
                #【测试】
                #print(ilist[4],file=testf)
                #【工具】 将unix格式的时间转化成本地时间
                time_local = time.localtime(int(ilist[4]))
                #【工具】转换成新的时间格式
                Time = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                danmaku = []
                danmaku_DeltaT = []
                danmaku.append(str(i+1))
                danmaku.append(Time)
                #print(self.vedio_TimeList[i],Time)
                if(self.vedio_TimeList[i]=="null"):
                    danmaku_DeltaT.append(str(i + 1))
                    danmaku_DeltaT.append("null")
                else:
                    deltaT = cacu_DeltaT.cacu_DeltaT(self.vedio_TimeList[i],Time)
                    danmaku_DeltaT.append(str(i+1))
                    danmaku_DeltaT.append(deltaT)

                self.vedio_danmakulist.append(danmaku)
                self.vedio_deltaTlist.append(danmaku_DeltaT)
            for i in attr2:
                self.vedio_danmakuT += '\n' + i
        self.Find_keywords()


    def saveData(self):
        print("save....")
        #print(self.vedio_deltaTlist)
        print(self.cnt)

        book = xlsxwriter.Workbook(self.savepath)  # 创建workbook对象
        sheet = book.add_worksheet('弹幕投放时间')  # 创建工作表
        col = ["视频","弹幕发送时间"]
        sheet.write_row("A1", col)
        #for i in range(0, 1):
        #    sheet.write(0, i, col[i])  # 列名

        for i in range(len(self.vedio_danmakulist)):
            writeline = 'A' + str(i+1+1)

            sheet.write_row(writeline,self.vedio_danmakulist[i])

            #【测试】数据格式是否正确
            #print(self.vedio_danmakulist[i],writeline,len(self.vedio_danmakulist[i]))
        book.close()

        book1 = xlsxwriter.Workbook(self.deltaTsavepath)
        sheet1 = book1.add_worksheet('弹幕投放时间差')
        col1 = ["原视频排行", "弹幕发送时间-视频投放时间"]
        sheet1.write_row("A1", col1)

        for i in range(len(self.vedio_deltaTlist)):
            writeline = 'A' + str(i+1+1)
            sheet1.write_row(writeline,self.vedio_deltaTlist[i])

            #【测试】数据格式是否正确
            #print(self.vedio_deltaTlist[i],writeline,len(self.vedio_deltaTlist[i]))
        book1.close()

        for i in range(len(self.keywords)):
            for j in range(len(self.keywords[i])):
                self.keywords[i][j] = list(self.keywords[i][j])
                self.keywords[i][j].insert(0,i+1)
        #print(self.keywords)
        book2 = xlsxwriter.Workbook(self.danmakuTsavepath)  # 创建workbook对象
        sheet2 = book2.add_worksheet('弹幕关键词')  # 创建工作表
        col2 = ["视频","关键词","词频"]
        sheet2.write_row("A1",col2)
        for i in range(len(self.keywords)):
            for j in range(len(self.keywords[i])):
                writeline = 'A' + str(i*30 + 2 + j)
                sheet2.write_row(writeline, self.keywords[i][j])
        book2.close()

        book3 = xlsxwriter.Workbook(self.DTcntsavepath)  # 创建workbook对象
        sheet3 = book3.add_worksheet('弹幕时间差统计')  # 创建工作表
        col3 = ["视频", "时间差等级/h", "频数"]
        sheet3.write_row("A1", col3)
        # for i in range(0, 1):
        #    sheet.write(0, i, col[i])  # 列名

        for i in range(len(self.cnt)):
            writeline = 'A' + str(i + 1 + 1)
            sheet3.write_row(writeline, self.cnt[i])

            # 【测试】数据格式是否正确
            # print(self.vedio_danmakulist[i],writeline,len(self.vedio_danmakulist[i]))
        book3.close()

    def askURL(self, baseurl):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome "
                          "/ 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67 "
        }


        #request = urllib.request.Request(baseurl, headers=head)
        res = requests.get(baseurl,headers=head)
        html = ""
        # 异常处理
        try:
            #response = urllib.request.urlopen(request)
            #print(response)
            #print(res.text.encode('UTF-8'))
            #html = str(etree.HTML(res.text))
            #html = response.read().decode('ISO-8859-1')
            #buff = BytesIO(html)
            #f = gzip.GzipFile(fileobj=buff)
            html = res.text.encode('iso-8859-1').decode('utf-8')
            #print(html)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        return html

    def Find_keywords(self):

        # 文本预处理  去除一些无用的字符   只提取出中文出来
        new_data = re.findall('[\u4e00-\u9fa5]+', self.vedio_danmakuT, re.S)
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
        word_counts_top30 = word_counts.most_common(30)
        #【测试】查看筛词结果
        #print(word_counts_top30)
        self.keywords.append(word_counts_top30)
        self.vedio_danmakuT=""


