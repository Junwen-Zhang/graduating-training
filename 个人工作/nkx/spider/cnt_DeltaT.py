# -*- codeing = utf-8 -*-
# @Time :2022/6/23 10:17
# @Author:nkx
# @File : cnt_DeltaT.py
# @Software: PyCharm
# 1h-3h-6h-12h-15h-18h-24h-36h-48h-60h-72h

from collections import Counter


class cnt_DeltaT():
    vedio_deltaTlist = []
    cntlist = []
    timesnap = [1, 3, 6, 12, 15, 18, 24, 36, 48, 60, 72,100]

    def __init__(self, deltaTlist):
        self.vedio_deltaTlist = deltaTlist
        self.cntlist = []

    def DeltaT_Processing(self):
        templist = []
        flag = 1
        rcd = []
        for j in range(len(self.vedio_deltaTlist)):
            i=self.vedio_deltaTlist[j]
            #print(i)
            #print(flag,i[0])
            if int(i[0]) == flag:
                rcd.append(i[1])
                if(j==len(self.vedio_deltaTlist)-1):
                    templist.append(rcd)

            else:
                if int(i[0]) - flag > 1:
                    print("rcd----------[]")
                    templist.append([])
                else:
                    flag = int(i[0])
                    templist.append(rcd)
                    print("rcd----------",rcd)
                    rcd = []
        print(len(templist))
        return templist

    def cnt(self):
        templist = self.DeltaT_Processing()
        for i in range(len(templist)):
            cntt = Counter(templist[i])
            for j in self.timesnap:
                if j in cntt:
                    self.cntlist.append([i+1, j, cntt[j]])
                else:
                    self.cntlist.append([i+1, j, 0])

    def get_cntDeltaT(self):
        self.cnt()
        return self.cntlist

