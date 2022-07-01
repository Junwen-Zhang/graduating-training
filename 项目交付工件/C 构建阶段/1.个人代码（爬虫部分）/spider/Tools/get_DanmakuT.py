# -*- codeing = utf-8 -*-
# @Time :2022/6/22 16:05
# @Author:Trump
# @File : test_danmakuText.py
# @Software: PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import requests
import jieba
import collections
import xlsxwriter
stop_path="C:/Users/Anning/Desktop/stopwords.txt"
class T_danmakuT():

    #---------------------------------------------------------------------------

    #vedio_Cid = " "  # 视频CID
    vedio_danmakuT = ""  # 对应弹幕列表
    vedio_Cidlist = []  # 视频CID列表
    savepath = "C:/Users/Anning/Desktop/弹幕关键词.xls"
    finddanmakuTest = re.compile(r'">(.*?)</d>') #弹幕内容爬取正则
    keywords = []

    #---------------------------------------------------------------------------

    def __init__(self,cid):
        self.vedio_Cidlist = cid

    def Get_Danmaku_Text(self):
        for i in range(0,len(self.vedio_Cidlist)):
            self.getData(self.vedio_Cidlist[i])
        self.savaData()

    def getData(self,cid):
        baseurl = "https://comment.bilibili.com/" + cid + ".xml"
        html = self.askURL(baseurl)
        # 【测试】打印网页源码
        #f = open('C:/Users/Anning/Desktop/html.txt','w',encoding='utf-8')
        #print(html,file=f);
        #f.close()

        soup = BeautifulSoup(html, "html.parser")
        # 【测试】打印soup
        #ff = open('C:/Users/Anning/Desktop/soup.txt', 'w', encoding='utf-8')
        #print(soup, file=ff);
        #ff.close()
        for item in soup.find_all(name="i"):
            # 【测试】查看item全部信息
            #print("ITEM",str(item))

            item = str(item)
            attr = re.findall(self.finddanmakuTest, item)  # re库用来通过正则表达式查找指定的字符串

            # 【测试】爬取是否正确
            #print(attr)
            #print(len(attr))
            # data.append(link)
            # 【测试】爬取是否正确
            # print(len(attr))
            # data.append(link)
            for i in attr:
                self.vedio_danmakuT += '\n' + i

        print(self.vedio_danmakuT)
        self.Find_keywords()

    def savaData(self):
        #saveF = open(self.savepath,'w',encoding='utf-8')
        #print(self.vedio_danmakuT.strip(),file=saveF)
        for i in range(len(self.keywords)):
            for j in range(len(self.keywords[i])):
                self.keywords[i][j] = list(self.keywords[i][j])
                self.keywords[i][j].insert(0,i+1)
        print(self.keywords)
        book2 = xlsxwriter.Workbook(self.savepath)  # 创建workbook对象
        sheet2 = book2.add_worksheet('弹幕关键词')  # 创建工作表
        col2 = ["视频","关键词","词频"]
        sheet2.write_row("A1",col2)
        for i in range(len(self.keywords)):
            for j in range(len(self.keywords[i])):
                writeline = 'A' + str(i*30 + 2 + j)
                sheet2.write_row(writeline, self.keywords[i][j])
        book2.close()

    def askURL(self,baseurl):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome "
                          "/ 80.0.3987.122  Safari / 537.36 Edg/91.0.864.67 "
        }

        # request = urllib.request.Request(baseurl, headers=head)
        res = requests.get(baseurl, headers=head)
        html = ""
        # 异常处理
        try:
            # response = urllib.request.urlopen(request)
            # print(response)
            # print(res.text.encode('UTF-8'))
            # html = str(etree.HTML(res.text))
            # html = response.read().decode('ISO-8859-1')
            # buff = BytesIO(html)
            # f = gzip.GzipFile(fileobj=buff)
            #html = res.text.encode('UTF-8')
            #print(type(res.text))
            html = res.text.encode('iso-8859-1').decode('utf-8')
            # print(html)
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
        print(new_data)
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
            if word not in stop_words:
                result_list.append(word)

        #【测试】查看分词结果
        print(result_list)

        # 筛选后统计
        word_counts = collections.Counter(result_list)
        # 获取前30高频的词
        word_counts_top30 = word_counts.most_common(30)
        #【测试】查看筛词结果
        print(word_counts_top30)
        self.keywords.append(word_counts_top30)
        self.vedio_danmakuT=""

test = T_danmakuT(["751446137","748276108"])
test.Get_Danmaku_Text()

