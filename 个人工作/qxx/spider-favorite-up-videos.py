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

fobbiden_list = ["BV1Wz4y1y7yM", "BV1Yi4y1f7ou", "BV1aR4y1M7pQ", "BV1CE411A7hE", "BV1zC4y1t7Et", "BV1CZ4y1T7JD",
                 "BV16F411n7MN", "BV1p341137dE", "BV1Uq4y1C7oN"]


def main():
    bvlist, imglist, titlelist, desclist = getBv()
    linklist, viewlist, dmlist, timelist, likelist, coinlist, collectlist, typelist = getData(bvlist)
    savepath = "最受欢迎up主热门视频.xls"
    saveData(savepath, bvlist, imglist, titlelist, desclist, linklist, viewlist, dmlist, timelist, likelist, coinlist,
             collectlist, typelist)


# 获取数据
def getBv():
    # 保存数据
    bvlist = []
    imglist = []
    titlelist = []
    desclist = []
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
            img = res[i]["pic"]
            title = res[i]["title"]
            desc = res[i]["description"]
            if bvid in fobbiden_list:
                continue
            bvlist.append(bvid)
            imglist.append(img)
            titlelist.append(title)
            desclist.append(desc)
    return bvlist, imglist, titlelist, desclist


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
findview = re.compile(r'<span class="view item" title="总播放数(.*)"><svg')
finddm = re.compile(r'<span class="dm item" title="历史累计弹幕数(.*)"><svg')
findtime = re.compile(r'(.*)</span>')
findlike = re.compile(r'<span class="like" title="点赞数(.*)"><!-- -->')
findcoin = re.compile(r'<span class="info-text">(.*)</span></span>')
findcollect = re.compile(r'<span class="info-text">(.*)</span></span>')

find_default = re.compile(r'(.*)')


def getData(bvlist):
    # 视频链接
    linklist = []
    # 播放量
    viewlist = []
    # 弹幕数
    dmlist = []
    # 投放时间
    timelist = []
    # 点赞
    likelist = []
    # 投币
    coinlist = []
    # 收藏
    collectlist = []
    # 标签
    typelist = []
    for i in range(0, len(bvlist)):
        print("processing:" + str(i + 1) + " " + bvlist[i] + "...")
        bvurl = "https://www.bilibili.com/video/" + bvlist[i]
        linklist.append(bvurl)
        html = askURL(bvurl)  # 保存获取到的网页源码
        soup = BeautifulSoup(html, "html.parser")
        word = ""
        for item in soup.find_all('a', class_="tag-link"):
            item = str(item)
            a_list = re.findall(r'[\u4e00-\u9fa5]', item)
            str1 = ""
            for j in a_list:
                str1 += j
            word += str1 + " "
        typelist.append(word.rstrip())

        view = soup.find_all('span', class_="view item")
        viewres = re.findall(findview, str(view))[0]
        viewres = int(viewres)
        viewlist.append(viewres)

        dm = soup.find_all('span', class_="dm item")
        dmres = re.findall(finddm, str(dm))[0]
        dmres = int(dmres)
        dmlist.append(dmres)

        time = soup.find_all('span', class_="pudate item")
        timeres = re.findall(find_default, str(time))
        timeres1 = re.findall(findtime, timeres[3])[0]
        timeres1 = timeres1.lstrip()
        timelist.append(timeres1)

        like = soup.find_all('span', class_="like")
        likeres = re.findall(findlike, str(like))[0]
        likeres = int(likeres)
        likelist.append(likeres)

        coin = soup.find_all('span', class_="coin")
        coinres = re.findall(findcoin, str(coin))[0]
        coinlist.append(coinres)

        collect = soup.find_all('span', class_="collect")
        collectres = re.findall(findcollect, str(collect))[0]
        collectlist.append(collectres)
    print("processing:" + str(i) + "...")
    return linklist, viewlist, dmlist, timelist, likelist, coinlist, collectlist, typelist


def saveData(savepath, bvlist, imglist, titlelist, desclist, linklist, viewlist, dmlist, timelist, likelist, coinlist,
             collectlist, typelist):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建工作表
    col = ["bvid", "图片链接", "标题", "简介", "视频链接", "播放量", "弹幕数", "发布时间", "点赞量", "硬币数", "收藏数", "标签"]
    for i in range(0, len(col)):
        sheet.write(0, i, col[i])
    for i in range(0, len(bvlist)):
        sheet.write(i + 1, 0, bvlist[i])
        sheet.write(i + 1, 1, imglist[i])
        sheet.write(i + 1, 2, titlelist[i])
        sheet.write(i + 1, 3, desclist[i])
        sheet.write(i + 1, 4, linklist[i])
        sheet.write(i + 1, 5, viewlist[i])
        sheet.write(i + 1, 6, dmlist[i])
        sheet.write(i + 1, 7, timelist[i])
        sheet.write(i + 1, 8, likelist[i])
        sheet.write(i + 1, 9, coinlist[i])
        sheet.write(i + 1, 10, collectlist[i])
        sheet.write(i + 1, 11, typelist[i])
    book.save(savepath)  # 保存


if __name__ == "__main__":  # 当程序执行时
    main()
