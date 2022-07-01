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
from xlutils.copy import copy


"""最受欢迎up主分析模块"""


ssl._create_default_https_context = ssl._create_unverified_context


folist = []
viewlist = []
likelist = []


def main():
    # 百大up主api
    baseurl1 = "https://space.bilibili.com/"
    xls_file = xlrd.open_workbook('最受欢迎up主候选.xls')
    xls_sheet = xls_file.sheets()[0]
    col_value = xls_sheet.col_values(0)
    for i in range(0, 20):
        uid = str(int(col_value[i+1]))
        follower, view, like = getData(baseurl1+uid, uid, i)
        folist.append(follower)
        viewlist.append(view)
        likelist.append(like)
    savepath = "最受欢迎up主候选.xls"
    print(viewlist)
    saveData(savepath)


def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)  # 使用request封装url和头部信息
    html = ""
    # 异常处理
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 获取数据
def getData(baseurl, uid, i):
    followerurl = "https://api.bilibili.com/x/relation/stat?vmid="+uid+"&jsonp=jsonp"
    follower = requests.get(followerurl)
    result = open('follower-info.json', 'w')
    result.write(follower.text)
    result.close()
    followerdict = json.loads(follower.text)
    resfollower = followerdict["data"]["follower"]
    f = open("viewlike-info.json")
    viewlikedict = json.load(f)
    resview = viewlikedict["data"][i]["archive"]["view"]
    reslike = viewlikedict["data"][i]["likes"]
    # print(resfollower)
    print(resview)
    # print(reslike)
    print("processing:"+ str(i) + "...")
    return resfollower, resview, reslike



# 保存数据
def saveData(savepath):
    print("save....")

    data = xlrd.open_workbook(savepath, formatting_info=True)
    excel = copy(wb=data)  # 完成xlrd对象向xlwt对象转换
    sheet = excel.get_sheet(0)  # 获得要操作的页
    table = data.sheets()[0]
    # book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # sheet = book.add_sheet('sheet1', cell_overwrite_ok=True)
    sheet.write(0, 3, "粉丝数")
    sheet.write(0, 4, "获赞数")
    sheet.write(0, 5, "播放数")
    print(folist)
    print(likelist)
    print(viewlist)
    for i in range(0, 20):
        sheet.write(i+1, 3, folist[i])
        sheet.write(i+1, 4, likelist[i])
        sheet.write(i+1, 5, viewlist[i])
    excel.save(savepath)

if __name__ == "__main__":
    main()
    print("爬取完毕！")

