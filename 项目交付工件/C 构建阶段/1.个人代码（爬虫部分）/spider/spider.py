# -*- codeing = utf-8 -*-
# @Time :2022/6/22 9:13
# @Author:Trump
# @File : spider.py
# @Software: PyCharm
from spider_vedioLink import spider_vedioLink
from spider_vedioInfo import spider_vedioInfo
from spider_vedioTime import spider_vedioTime
from spider_danmakuTime import spider_danmakuTime
from Tools import getCID
#【监测】保存输出
console = f=open('C:/Users/Anning/Desktop/console.txt','w',encoding='utf-8')

vedioLink_savepath = ["C:/Users/Anning/Desktop/[视频链接]美食top100.xls", "C:/Users/Anning/Desktop/[视频链接]音乐top100.xls",
                      "C:/Users/Anning/Desktop/[视频链接]鬼畜top100.xls", "C:/Users/Anning/Desktop/[视频链接]游戏top100.xls",
                      "C:/Users/Anning/Desktop/[视频链接]影视top100.xls"]

spider_baseurl = ["https://www.bilibili.com/v/popular/rank/food", "https://www.bilibili.com/v/popular/rank/music",
                  "https://www.bilibili.com/v/popular/rank/kichiku", "https://www.bilibili.com/v/popular/rank/game"
    , "https://www.bilibili.com/v/popular/rank/cinephile"]

vedioTime_savepath = ["C:/Users/Anning/Desktop/[视频发布时间]美食top100.xls", "C:/Users/Anning/Desktop/[视频发布时间]音乐top100.xls",
                      "C:/Users/Anning/Desktop/[视频发布时间]鬼畜top100.xls", "C:/Users/Anning/Desktop/[视频发布时间]游戏top100.xls",
                      "C:/Users/Anning/Desktop/[视频发布时间]影视top100.xls"]

danmakuTime_savepath = ["C:/Users/Anning/Desktop/[对应弹幕发布时间]美食top100.xls",
                        "C:/Users/Anning/Desktop/[对应弹幕发布时间]音乐top100.xls",
                        "C:/Users/Anning/Desktop/[对应弹幕发布时间]鬼畜top100.xls",
                        "C:/Users/Anning/Desktop/[对应弹幕发布时间]游戏top100.xls",
                        "C:/Users/Anning/Desktop/[对应弹幕发布时间]影视top100.xls"]

danmakuDeltaT_savepath = ["C:/Users/Anning/Desktop/[弹幕时间差]美食top100.xls",
                        "C:/Users/Anning/Desktop/[弹幕时间差]音乐top100.xls",
                        "C:/Users/Anning/Desktop/[弹幕时间差]鬼畜top100.xls",
                        "C:/Users/Anning/Desktop/[弹幕时间差]游戏top100.xls",
                        "C:/Users/Anning/Desktop/[弹幕时间差]影视top100.xls"]
danmakuTsavepath = ["C:/Users/Anning/Desktop/【弹幕关键词】美食top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕关键词】音乐top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕关键词】鬼畜top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕关键词】游戏top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕关键词】影视top100.xls"]

DTcntsavepath = ["C:/Users/Anning/Desktop/【弹幕时间差量化统计】美食top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕时间差量化统计】音乐top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕时间差量化统计】鬼畜top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕时间差量化统计】游戏top100.xls",
                        "C:/Users/Anning/Desktop/【弹幕时间差量化统计】影视top100.xls"]

vedioInfo_savepath = ["C:/Users/Anning/Desktop/【信息统计】美食top100.xls",
                        "C:/Users/Anning/Desktop/【信息统计】音乐top100.xls",
                        "C:/Users/Anning/Desktop/【信息统计】鬼畜top100.xls",
                        "C:/Users/Anning/Desktop/【信息统计】游戏top100.xls",
                        "C:/Users/Anning/Desktop//【信息统计】影视top100.xls"]

label = ["美食","音乐","鬼畜","游戏","影视"]

class spider():
    vedioLink_savepath=""
    spider_baseurl=""
    vedioTime_savepath=""
    danmakuTime_savepath=""
    danmakuTsavepath = ""
    DTcntsavepath=""
    vedioInfo_savepath = ""

    def __init__(self,vedioLink_savepath,spider_baseurl,vedioTime_savepath,danmakuTime_savepath,danmakuDeltaT_savepath,danmakuTsavepath,DTcntsavepath,vedioInfo_savepath):
        self.vedioLink_savepath=vedioLink_savepath
        self.spider_baseurl=spider_baseurl
        self.vedioTime_savepath=vedioTime_savepath
        self.danmakuTime_savepath=danmakuTime_savepath
        self.danmakuDeltaT_savepath = danmakuDeltaT_savepath
        self.danmakuTsavepath = danmakuTsavepath
        self.DTcntsavepath = DTcntsavepath
        self.vedioInfo_savepath = vedioInfo_savepath

    def spiderdata(self):

        print("VedioLink-------------------------------------------------------------------------")
        VedioLink = spider_vedioLink(self.spider_baseurl,self.vedioLink_savepath).GET_vedio_Link()
        #print(VedioLink)
        print(len(VedioLink),file=console)

        print("Vediotime-------------------------------------------------------------------------")
        VedioTime = spider_vedioTime(VedioLink,self.vedioTime_savepath)
        VedioTimeList = VedioTime.GET_Vedio_Time()

        print("VedioInfo-------------------------------------------------------------------------")
        VedioInfo = spider_vedioInfo(VedioLink, self.vedioInfo_savepath)
        VedioInfoList = VedioInfo.GET_Vedio_Info()
        print(VedioInfoList)


        print("CID--------------------------------------------------------------------------------")
        CID = getCID.getCID(self.spider_baseurl).getData()
        print(CID,file=console)

        print("DanmakuTime------------------------------------------------------------------------")
        danmakuTime = spider_danmakuTime(CID,self.danmakuTime_savepath,VedioTimeList,self.danmakuDeltaT_savepath,self.danmakuTsavepath,self.DTcntsavepath)
        danmakuTime.GET_Danmaku_Time()

if __name__ == "__main__":

    for i in range(4,len(spider_baseurl)):
        print(label[i],spider_baseurl[i])
        sp = spider(vedioLink_savepath[i],spider_baseurl[i],vedioTime_savepath[i],danmakuTime_savepath[i],danmakuDeltaT_savepath[i],danmakuTsavepath[i],DTcntsavepath[i],vedioInfo_savepath[i])
        sp.spiderdata()



