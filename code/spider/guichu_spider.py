#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: if_name_main.py

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import json
from jsonpath import jsonpath
import sqlite3  # 进行SQLite数据库操作


def main():
    #鬼畜调教
    baseurl1="https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click" \
             "&copy_right=-1&cate_id=22&page="
    #音MAD
    baseurl2="https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click" \
             "&copy_right=-1&cate_id=26&page="
    #人力VOLCALOID
    baseurl3="https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click" \
             "&copy_right=-1&cate_id=126&page="
    #鬼畜剧场
    baseurl4="https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click" \
             "&copy_right=-1&cate_id=216&page="
    #教程演示
    baseurl5 = "https://s.search.bilibili.com/cate/search?main_ver=v3&search_type=video&view_type=hot_rank&order=click" \
               "&copy_right=-1&cate_id=127&page="
    # 爬取网页
    #鬼畜区没有总榜，共五个分区，分别爬取
    datalist1 = getData(baseurl1,50)
    datalist2 = getData(baseurl2,25)
    datalist3 = getData(baseurl3,14)
    datalist4 = getData(baseurl4,50)
    datalist5 = getData(baseurl5,3)
    #把爬取到的鬼畜区五个分类下的视频信息存入同一个列表
    datalist=[]
    for i in range(0,len(datalist1)):
        datalist.append(datalist1[i])
    for i in range(0,len(datalist2)):
        datalist.append(datalist2[i])
    for i in range(0,len(datalist3)):
        datalist.append(datalist3[i])
    for i in range(0,len(datalist4)):
        datalist.append(datalist4[i])
    for i in range(0,len(datalist5)):
        datalist.append(datalist5[i])

    # 保存数据
    savepath='C:/Users/14413/Desktop/鬼畜.xls'
    saveData(datalist, savepath)


# 一个功能对应一个函数
# 爬取网页
#page是爬取的总页数，由于鬼畜五个分区的热门视频总数各不相同，故根据分区设置不同的页数
def getData(baseurl,page):
    datalist = []
    for k in range(1,page):
        Url=baseurl+str(k)+"&pagesize=20&jsonp=jsonp&time_from=20220614&time_to=20220621"
        html = askURL(Url)
        #soup = BeautifulSoup(html, "html.parser")
        #将返回的str信息转换成字典
        json_str=json.loads(html)
        newjson = json.dumps(json_str, ensure_ascii=False)
        result=json.loads(newjson)
        #转换后的字典中，result键对应的值是一个存储字典的列表，每个字典存储一个视频的所有信息
        html_data=result['result']
        for i in range(0,len(html_data)):
            #一个视频的所有信息
            dict=html_data[i]
            data=[]
            #视频链接
            url = dict['arcurl']
            #print(bvid)
            data.append(url)
            #视频标题
            title = dict['title']
            data.append(title)
            #播放量
            plays=dict['play']
            data.append(plays)
            #评论数
            reviews = dict['review']
            data.append(reviews)
            #弹幕数
            danmu=dict['video_review']
            data.append(danmu)
            #收藏量
            favorites=dict['favorites']
            data.append(favorites)
            #上传时间
            pubdate=dict['pubdate']
            data.append(pubdate)
            #视频时长
            duration=dict['duration']
            data.append(duration)
            #up主
            up=dict['author']
            data.append(up)
            #标签分类
            tag=dict['tag']
            data.append(tag)

            datalist.append(data)

    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/102.0.0.0 Mobile Safari/537.36",
        "referer": "https://www.bilibili.com/",
        "cookie":"buvid3=72AC6337-2A6B-4531-8DDB-BB59F6F9AEBA185005infoc; rpdid=|(umukk)luJm0J'uYuJmu|lJk; LIVE_BUVID=AUTO3616145174618945; fingerprint3=75bdc26c04aa52a4d45ced8b91eb7484; fingerprint_s=c31c150c2e4d477fa622ff7efeb7b833; video_page_version=v_old_home; b_ut=5; buvid4=F6143A48-790F-0EC1-8A5D-7FB3EB29C78105833-022020322-V35mpzdvTWTWr7BtZn/6tA%3D%3D; CURRENT_BLACKGAP=0; fingerprint=8209fd7c8aaf2ba6fcc8218effec0c73; buvid_fp_plain=undefined; buvid_fp=5d6d6357635b452cbfab035e9c3ad46e; DedeUserID=156593773; DedeUserID__ckMd5=5e8fa28031f78f5f; _uuid=5F8C29FD-B141-FC109-11066-9B66DDE66510537668infoc; nostalgia_conf=-1; hit-dyn-v2=1; CURRENT_QUALITY=80; blackside_state=0; SESSDATA=0a183c0d%2C1670931134%2C7235a%2A61; bili_jct=46032eeca74460179dd31ca80efad49a; sid=jbb2ld0h; is-2022-channel=1; PVID=2; b_lsid=FF3322F4_18183C854B7; bsource=search_baidu; i-wanna-go-back=2; bp_video_offset_156593773=674029932591972400; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_72AC6337%22%3A%2218183C85B96%22%2C%22333.1073.fp.risk_72AC6337%22%3A%2218183C86336%22%2C%22333.6.fp.risk_72AC6337%22%3A%2218183C939D0%22%2C%22333.788.fp.risk_72AC6337%22%3A%2218183CA4F56%22%2C%22333.934.fp.risk_72AC6337%22%3A%2218183EFB9F6%22%7D%7D; CURRENT_FNVAL=4048; innersign=0"
    }
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


# 保存数据
def saveData(datalist, savepath):
    print("save....")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet('鬼畜', cell_overwrite_ok=True)  # 创建工作表
    col = ("视频链接", "视频标题", "播放量","评论数","弹幕数","收藏量","上传时间","视频时长","up主","标签分类")
    for i in range(0, 10):
        sheet.write(0, i, col[i])  # 列名
    for i in range(0, len(datalist)):
        print("第%d条" % (i+1))
        data = datalist[i]
        #sheet.write(i , 0, i )
        for j in range(0, 10):
            sheet.write(i+1, j, data[j])  # 数据
        book.save(savepath)  # 保存


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    print("爬取完毕！")
