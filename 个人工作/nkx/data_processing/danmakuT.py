# -*- codeing = utf-8 -*-
# @Time :2022/6/30 17:22
# @Author:nkx
# @File : danmakuT.py
# @Software: PyCharm
# -*- codeing = utf-8 -*-
# @Time :2022/6/23 8:49
# @Author:nkx
# @File : Kichiku_Tab.py
# @Software: PyCharm

import xlrd
import collections
import xlsxwriter

class cnt():
    excel = xlrd.open_workbook("C:/Users/Anning/Desktop/5-2/对应弹幕发布时间鬼畜top100.xls")
    book2 = xlsxwriter.Workbook("C:/Users/Anning/Desktop/meta-data/yinyue.xls")  # 创建workbook对象
    def __init__(self,sourcepath,savepath):
        self.excel = xlrd.open_workbook(sourcepath)
        self.book2 = xlsxwriter.Workbook(savepath)


    def CNT(self):
        sheet = self.excel.sheet_by_index(0)  # 获取工作薄
        rows: list = sheet.row_values(0)  # 获取第一行的表头内容
        index = sheet.col_values(rows.index('视频'))  # 获取age列所在的列数: 1，也可以换成"password"
        listindexs = sheet.col_values(rows.index('弹幕发送时间'))  # 获取age列的所有内容


        print(index)
        print("----------------")
        print(listindexs)
        print("----------------")

sourcepath = ["C:/Users/Anning/Desktop/5-2/[对应弹幕发布时间]音乐top100.xls","C:/Users/Anning/Desktop/【信息统计】音乐top100.xls",
          "C:/Users/Anning/Desktop/【信息统计】鬼畜top100.xls","C:/Users/Anning/Desktop/【信息统计】游戏top100.xls",
          "C:/Users/Anning/Desktop/【信息统计】影视top100.xls"]

savepath = ["C:/Users/Anning/Desktop/meta-data/yinyue.xls","C:/Users/Anning/Desktop/video_music_TagCnt.xlsx",
          "C:/Users/Anning/Desktop/video_guichu_TagCnt.xlsx","C:/Users/Anning/Desktop/video_game_TagCnt.xlsx",
          "C:/Users/Anning/Desktop/video_movie_TagCnt.xlsx"]

for i in range(1):
    cnt(sourcepath[i],savepath[i]).CNT()