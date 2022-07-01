import json
from flask import Blueprint, render_template,request
from LinkAnalysis import linkAnalys
from compute.anime_tags import getTagsDict, get100TagsDict
import math
"""
本视图专门用于处理ajax数据
"""
search = Blueprint('search', __name__)


@search.route('/box')
def searchVideo():
    return render_template("searchVideo.html")

@search.route('/main')
def commentmain():
    link = request.args.get('link')

    global la
    la = linkAnalys.LinkAnls(link)
    la.getData()
    DanmakuText = la.video_DanmakuText
    Danmaku = DanmakuText.split('\n')
    print(la.danmaku_keywords)
    keyword = [la.danmaku_keywords[0][0], la.danmaku_keywords[1][0], la.danmaku_keywords[2][0],la.danmaku_keywords[3][0]
               ,la.danmaku_keywords[4][0],la.danmaku_keywords[5][0],la.danmaku_keywords[6][0],la.danmaku_keywords[7][0],
               la.danmaku_keywords[8][0],la.danmaku_keywords[9][0],la.danmaku_keywords[10][0],la.danmaku_keywords[11][0]]
    view_data = []

    def build_view_data(item):
        a = {}
        for i in keyword:
            if i in item:
                a['text'] = item
                if a not in view_data:
                    view_data.append(a)
                    return 1
        return 0

    a = 0
    for item in Danmaku:
        if build_view_data(item):
            a += 1
        if a == 20:
            break

    datalist = {}
    datalist["allinfo"] = la.allinfo
    print(datalist["allinfo"])
    datalist["comment"] = la.video_comment[0:12]
    # datalist["show"] =
    # print('comment',comment)
    print(view_data)
    return render_template("searchVideo_main.html",data=datalist,datad=view_data)

@search.route('/show',methods=['GET'])
def CommentAnaly():
    comment_keyword = la.comment_keywords
    danmaku_keywords = la.danmaku_keywords
    video_DanmakuDTC = la.video_DanmakuDTC
    # print(comment_keyword)
    datalst={}
    datalst["comment_keyword"] = []
    datalst["danmaku_keywords"] = []
    datalst["video_DanmakuDTC"] = {}
    datalst["video_DanmakuDTC"]['x'] = ['<1', '(1,3]', '(3,6]', '(6,12]', '(12,15]', '(15,18]', '(18,24]', '(24,36]', '(36,48]',
                      '(48,60]', '(60,72]', '>72']
    datalst["video_DanmakuDTC"]['y'] = []

    def build_view_data3(item):
        datalst["video_DanmakuDTC"]['y'].append(item[1])

    def build_view_data(item):
        dic = {}
        dic['name'] = item[0]  # 这里可以修改中英文
        dic['value'] = item[1]
        datalst["danmaku_keywords"].append(dic)

    def build_view_data2(keyword):
        for item in keyword:
            if item[1]>2:
                data = {}
                data['name'] = item[0]
                data['value'] = item[1]
                datalst["comment_keyword"].append(data)

    [build_view_data3(item) for item in video_DanmakuDTC]
    [build_view_data(item) for item in danmaku_keywords]
    build_view_data2(comment_keyword)
    print("data: ",datalst["comment_keyword"])
    return json.dumps(datalst, ensure_ascii=False)  # 将python对象转化为json对象
