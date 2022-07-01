import json
import requests
import xlwt
import xlrd

"""up主分析模块"""
"""3.百大up主粉丝趋势展示"""
"""选取名单前20"""


bloggerList = [1313, 1746, 2892468, 17992, 79, 98, 38285, 103, 85, 1212, 972, 937, 510683, 732, 1201290, 105, 3528031,
             1957, 22067, 1336821]
finaldate = []
incrall = []
totalall = []


def main():
    bloggerId = ""
    baseurl = "https://bz.feigua.cn//v1/BloggerInfo/OverViewChart?bloggerId=" + bloggerId + "&period=30"
    xls_file = xlrd.open_workbook('2021百大up主.xls')
    xls_sheet = xls_file.sheets()[0]
    col_value = xls_sheet.col_values(0)
    f = open("bloggerId.txt")
    flag = 0
    for i in range(0, 20):
        uid = str(col_value[i+1])
        bloggerId = str(bloggerList[i])
        datelist, incrlist, totallist = getData(baseurl, i)
        if flag == 0:
            finaldate.append(datelist)
            flag += 1
        incrall.append(incrlist)
        totalall.append(totallist)
    savepath = "2021百大up主粉丝量分析-抽选20个.xls"
    saveData(savepath)

# 获取数据
def getData(baseurl, i):
    filename = str(i+1)
    f = open("FansTimeTrend/"+filename+".json")
    data = json.load(f)
    res = data["Data"]["FansTrend"]
    incrlist = []
    totallist = []
    datelist = []
    for j in range(0, len(res)):
        tmp = res[j]
        date = tmp["Name"]
        datelist.append(date)
        incr = tmp["IncrCount"]
        incrlist.append(incr)
        total = tmp["Count"]
        totallist.append(total)
    return datelist, incrlist, totallist


# 保存数据
def saveData(savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('2021百大up主粉丝增量分析-抽选20个', cell_overwrite_ok=True)
    sheet.write(0, 0, "uid")
    for i in range(0, len(finaldate[0])):
        sheet.write(0, i+1, finaldate[0][i])
    sheet.write(0, 31, "粉丝起始总量")
    sheet.write(0, 32, "粉丝结束总量")
    xls_file = xlrd.open_workbook('2021百大up主.xls')
    xls_sheet = xls_file.sheets()[0]
    col_value = xls_sheet.col_values(0)
    for i in range(0, 20):
        uid = str(col_value[i+1])
        sheet.write(i+1, 0, uid)
        for j in range(0, 30):
            sheet.write(i+1, j+1, incrall[i][j])
        sheet.write(i+1, 31, totalall[i][0])
        sheet.write(i+1, 32, totalall[i][29])
    book.save(savepath)

if __name__ == "__main__":  # 当程序执行时
    main()

