from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式,进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import json
import requests
import xlrd
import re

"""up主分析模块"""
"""2.百大up主流行趋势展示"""

all_type_dict = []
allinfo = []
numlist = []


xls_file = xlrd.open_workbook('2021百大up主.xls')
xls_sheet = xls_file.sheets()[0]
col_value = xls_sheet.col_values(0)


def main():
    baseurl1 = "https://api.bilibili.com/x/space/arc/search?mid="
    baseurl2 = "&ps=50&tid=0&pn=1&keyword=&order=click&jsonp=jsonp"
    for i in range(1, 100):
        mid = str(col_value[i])
        baseurl = baseurl1 + mid + baseurl2
        datalist, allnum = getData(baseurl, mid)
        allinfo.append(datalist)
        numlist.append(allnum)
    savepath = "2021百大up主流行趋势.xls"
    saveData(savepath)

# 获取数据
def getData(baseurl, mid):
    # up主空间视频分类
    datalist = []
    typestr = requests.get(baseurl)
    result = open('type-info.json', 'w')
    result.write(typestr.text)
    result.close()
    typedict = json.loads(typestr.text)
    res = typedict
    res = typedict["data"]["list"]["tlist"]
    allnum = 0
    for item in res.items():
        strlist = []
        valuelist = []
        for t1 in item[1].items():
            strlist.append(t1[0])
            valuelist.append(t1[1])
        if valuelist[2] not in all_type_dict:
            all_type_dict.append(valuelist[2])
        list1 = [valuelist[2], valuelist[1]]
        allnum += valuelist[1]
        datalist.append(list1)
    return datalist, allnum


# 保存数据
def saveData(savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('2021百大up主流行趋势', cell_overwrite_ok=True)
    col = ("uid", "总视频数", "生活", "影视", "科技", "动物圈", "动画", "电视剧", "音乐", "知识", "游戏", "时尚", "纪录片", "美食", "汽车", "运动",
           "娱乐", "舞蹈", "国创", "咨讯", "鬼畜")
    for i in range(0, 21):
        sheet.write(0, i, col[i])
    for i in range(0, 99):
        print("第%d条" % (i + 1))
        mid = str(col_value[i+1])
        sheet.write(i+1, 0, mid)
        datanum = numlist[i]
        datainfo = allinfo[i]
        sheet.write(i+1, 1, datanum)
        for j in range(0, len(datainfo)):
            for k in range(0, 21):
                if datainfo[j][0] == col[k]:
                    sheet.write(i+1, k, datainfo[j][1])
    book.save(savepath)


if __name__ == "__main__":  # 当程序执行时
    main()

