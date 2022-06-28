import json
from flask import Blueprint, render_template,request
from LinkAnalysis import linkAnalys
from compute.anime_tags import getTagsDict, get100TagsDict
import math
"""
本视图专门用于处理ajax数据
"""
search = Blueprint('search', __name__)

@search.route('/main')
def commentmain():
    link = request.args.get('link')

    global la
    la = linkAnalys.LinkAnls(link)
    la.getData()
    DanmakuText = la.video_DanmakuText
    Danmaku = DanmakuText.split('\n')
    keyword = [la.danmaku_keywords[0][0], la.danmaku_keywords[1][0], la.danmaku_keywords[2][0]]
    view_data = []

    def build_view_data(item):
        a = {}
        for i in keyword:
            if i in item:
                a['text'] = item
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
    datalist["comment"] = la.video_comment[0:11]
    # datalist["show"] =
    # print('comment',comment)
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
            if item[1]>5:
                data = {}
                data['name'] = item[0]
                data['value'] = item[1]
                datalst["comment_keyword"].append(data)

    [build_view_data3(item) for item in video_DanmakuDTC]
    [build_view_data(item) for item in danmaku_keywords]
    build_view_data2(comment_keyword)
    print("data: ",datalst["comment_keyword"])
    return json.dumps(datalst, ensure_ascii=False)  # 将python对象转化为json对象

'''
@search.route("/")
def guichuAnalysis():
    link = request.args.get('link')
    print(link)
    #anls = linkAnalys.LinkAnls(link)
    #anls.getData()
    data = la.video_DanmakuText
    data = data.split('\n')
    keyword = [la.danmaku_keywords[0][0], la.danmaku_keywords[1][0], la.danmaku_keywords[2][0]]
    view_data = []

    def build_view_data(item):
        a = {}
        for i in keyword:
            if i in item:
                a['text'] = item
                view_data.append(a)
                return 1
        return 0

    a = 0
    for item in data:
        if build_view_data(item):
            a += 1
        if a == 20:
            break
    #print("view_data",view_data)
    #return json.dumps(view_data, ensure_ascii=False)

    print("view",view_data)
    return render_template("searchVideo_main.html",data = view_data)

@search.route('/dmkeyword',methods=['GET'])
def DanmakuAnls():
    link = request.args.get('link')
    #anls = linkAnalys.LinkAnls(link)
    #anls.getData()
    data = la.danmaku_keywords

    view_data = []

    def build_view_data(item):
        dic = {}
        dic['name'] = item[0]  # 这里可以修改中英文
        dic['value'] = item[1]
        view_data.append(dic)

    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)



@search.route('/dmdt',methods=['GET'])
def DanmakuDTAnls():
    link = request.args.get('link')
    #anls = linkAnalys.LinkAnls(link)
    #anls.getData()
    data = la.video_DanmakuDTC

    view_data = {}
    view_data['x'] = ['<1','(1,3]','(3,6]','(6,12]','(12,15]','(15,18]','(18,24]','(24,36]','(36,48]','(48,60]','(60,72]','>72']
    view_data['y'] = []

    def build_view_data(item):


        view_data['y'].append(item[1])

    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)
'''
