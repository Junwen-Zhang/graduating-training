import xlwt  # 进行excel操作
import json
import requests
import xlrd
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import ssl
from io import BytesIO
import gzip

ssl._create_default_https_context = ssl._create_unverified_context

# 最受欢迎up主标签
def main():
    bvlist = getBv()
    print(bvlist)
    print(len(bvlist))
    hotwordlist = getData(bvlist)
    worddict = prcswords(hotwordlist)
    savepath = "最受欢迎up主视频标签统计.xls"
    saveData(savepath, worddict)



# 处理热词
def prcswords(hotwordlist):
    worddict = {}
    for i in range(0, len(hotwordlist)):
        for j in range(0, len(hotwordlist[i])):
            tmp = hotwordlist[i][j]
            if tmp not in worddict:
                worddict[tmp] = 1
            else:
                worddict[tmp] += 1
    del worddict['']
    print(worddict)
    return worddict


# 获取数据
def getBv():
    # 保存数据
    page = ""
    bvlist = []
    for i in range(1, 7):
        page = str(i)
        baseurl = "https://api.bilibili.com/x/space/arc/search?mid=517327498&ps=50&tid=0&pn=" + page + "&keyword=&order=click&jsonp=jsonp"
        typestr = requests.get(baseurl)
        result = open('video-info.json', 'w')
        result.write(typestr.text)
        result.close()
        typedict = json.loads(typestr.text)
        res = typedict["data"]["list"]["vlist"]
        for i in range(0, len(res)):
            bvid = res[i]["bvid"]
            bvlist.append(bvid)
    return bvlist


def askURL(url):
    head = {  # 模拟浏览器头部信息，向bilibili服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉bilibili服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）
    request = urllib.request.Request(url, headers=head)  # 使用request封装url和头部信息
    htmls = ""
    try:
        response = urllib.request.urlopen(request)
        r = response
        htmls = r.read()
        if ('Content-Encoding', 'gzip') in response.headers._headers:
            buff = BytesIO(htmls)
            f = gzip.GzipFile(fileobj=buff)
            htmls = f.read().decode('utf-8')
        else:
            htmls = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return htmls


# 标签
findType = re.compile(r'target="_blank">(.*)</a>')


def getData(bvlist):
    word50 = []
    for i in range(0, len(bvlist)):
        bvurl = "https://www.bilibili.com/video/"+bvlist[i]
        html = askURL(bvurl)  # 保存获取到的网页源码
        soup = BeautifulSoup(html, "html.parser")
        word = ""
        for item in soup.find_all('a', class_="tag-link"):
            # print(item)  # 测试：查看视频标签全部信息
            item = str(item)
            a_list = re.findall(r'[\u4e00-\u9fa5]', item)
            str1 = ""
            for j in a_list:
                str1+=j
            word += str1 +" "
        print(word.rstrip())
        word50.append(word.rstrip())
        print("处理了第"+str(i)+"个视频")
    print(word50)
    return word50


def saveData(savepath, worddict):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ("标签", "频次")
    sheet.write(0, 0, col[0])
    sheet.write(0, 1, col[1])
    cnt = 1
    for key, value in worddict.items():
        sheet.write(cnt, 0, key)
        sheet.write(cnt, 1, value)
        cnt+=1
    book.save(savepath)  # 保存


if __name__ == "__main__":  # 当程序执行时
    main()