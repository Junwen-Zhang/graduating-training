# -*- codeing = utf-8 -*-
# @Time :2022/6/23 8:49
# @Author:nkx
# @File : Kichiku_Tab.py
# @Software: PyCharm

import xlrd
import collections
import xlsxwriter

class cnt():
    excel = xlrd.open_workbook("C:/Users/Anning/Desktop/【信息统计】音乐top100.xls")
    book2 = xlsxwriter.Workbook("C:/Users/Anning/Desktop/meta-data/video_chu_tagCnt.xls")  # 创建workbook对象
    def __init__(self,sourcepath,savepath):
        self.excel = xlrd.open_workbook(sourcepath)
        self.book2 = xlsxwriter.Workbook(savepath)


    def CNT(self):
        sheet = self.excel.sheet_by_index(0)  # 获取工作薄
        rows: list = sheet.row_values(0)  # 获取第一行的表头内容
        index = rows.index('标签')  # 获取age列所在的列数: 1，也可以换成"password"
        listindexs = sheet.col_values(rows.index('标签'))  # 获取age列的所有内容

        TagText = ""
        print(listindexs)
        print("----------------")
        # 遍历该列所有的内容
        for i in range(1, len(listindexs)):
            TagText += listindexs[i]
        TagText = TagText.strip(" ")
        print(TagText)
        Tags = TagText.split(" ")
        print(Tags)

        word_counts = collections.Counter(Tags)

        tag = list(word_counts.keys())
        cnt = list(word_counts.values())


        sheet2 = self.book2.add_worksheet('tags')  # 创建工作表
        col2 = ["tag","cnt"]
        sheet2.write_row("A1",col2)
        for i in range(len(tag)):
            writeline = 'A' + str(i+2)
            writes = []
            writes.append(tag[i])
            writes.append(cnt[i])
            sheet2.write_row(writeline, writes)
            print(writeline,writes)
        self.book2.close()

sourcepath = ["C:/Users/Anning/Desktop/【信息统计】美食top100.xls","C:/Users/Anning/Desktop/【信息统计】音乐top100.xls",
          "C:/Users/Anning/Desktop/【信息统计】鬼畜top100.xls","C:/Users/Anning/Desktop/【信息统计】游戏top100.xls",
          "C:/Users/Anning/Desktop/【信息统计】影视top100.xls"]

savepath = ["C:/Users/Anning/Desktop/video_food_TagCnt.xlsx","C:/Users/Anning/Desktop/video_music_TagCnt.xlsx",
          "C:/Users/Anning/Desktop/video_guichu_TagCnt.xlsx","C:/Users/Anning/Desktop/video_game_TagCnt.xlsx",
          "C:/Users/Anning/Desktop/video_movie_TagCnt.xlsx"]

for i in range(5):
    cnt(sourcepath[i],savepath[i]).CNT()