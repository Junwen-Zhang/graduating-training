import json
import requests
import xlwt

"""up主分析模块"""
"""1.百大up主展示"""


# 共99人，一人被取消资格
def main():
    # 百大up主api
    baseurl = "https://api.bilibili.com/x/activity/up/list?ps=100&sid=239549&type=ctime"
    datalist = getData(baseurl)
    savepath = "2021百大up主.xls"
    saveData(datalist, savepath)


# 获取数据
def getData(baseurl):
    # up主信息列表
    datalist = []
    upstr = requests.get(baseurl)  # 这里返回json数据
    result = open('up-info.json', 'w')
    result.write(upstr.text)
    result.close()
    updict = json.loads(upstr.text)
    res = updict["data"]["list"]
    for i in range(0, 99):
        data = []
        item = res[i]
        uid = str(item["wid"])
        data.append(uid)
        name = item["object"]["act"]["name"]
        data.append(name)
        imgSrc = item["object"]["cont"]["image"]
        data.append(imgSrc)
        followNum = item["object"]["act"]["follower_num"]
        data.append(followNum)
        desc = item["object"]["cont"]["message"]
        data.append(desc)
        link = "https://space.bilibili.com/" + uid
        data.append(link)
        datalist.append(data)
    print(datalist)
    return datalist


# 保存数据
def saveData(datalist, savepath):
    print("save....")
    # 创建workbook对象
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    # 创建工作表
    sheet = book.add_sheet('2021百大up主', cell_overwrite_ok=True)
    col = ("uid", "up名", "图片链接", "粉丝数", "评价", "空间链接")
    for i in range(0, 6):
        sheet.write(0, i, col[i])
    for i in range(0, 99):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 6):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


if __name__ == "__main__":
    main()
    print("爬取完毕！")
