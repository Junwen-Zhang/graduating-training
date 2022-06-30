# -*- codeing = utf-8 -*-
# @Time :2022/6/22 14:42
# @Author:Trump
# @File : cacu_DeltaT.py
# @Software: PyCharm
import datetime
import sys
timesnap = [0,1,3,6,12,15,18,24,36,48,60,72,sys.maxsize]
def cacu_DeltaT(VedioTime,danmakuTime):

    #视频发布时间
    VT = datetime.datetime.strptime(VedioTime, '%Y-%m-%d %H:%M:%S')
    #视频弹幕发布时间
    DT = datetime.datetime.strptime(danmakuTime, '%Y-%m-%d %H:%M:%S')
    #时间差
    delta = DT - VT
    #换算分钟
    seconds = delta.total_seconds()
    hours = int(seconds/60/60)
    for i in range(0,len(timesnap)-1):
        if(hours>=timesnap[i] and hours<timesnap[i+1]):
            if hours == 0:
                return 1
            if hours==timesnap[i]:
                return timesnap[i]
            return timesnap[i+1]

