# -*- coding:utf-8 -*-
import json, math

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.video import make_vedio, make_vediokeyword, make_vediotime

# transform2cn={"movie":"电影","game":"游戏","music":"音乐","guichu":"鬼畜","food":"美食"}
# transform2en={"电影":"movie","游戏":"game","音乐":"music","鬼畜":"guichu","美食":"food"}

"""
本视图专门用于处理ajax数据
"""
video = Blueprint('video', __name__)


# @video.route('/main')
# def videoAnalysis():
#     return render_template("video_main.html")


@video.route('/showhot')
def show100video():
    partition = request.args.get('partition')
    data = db.session.query(make_vedio(partition)).all()
    videos = []

    def build_view_data(item):
        dic = {}
        dic['id'] = item.id
        dic["name"] = item.name
        dic["up"] = item.up
        dic["url"] = item.link
        dic["picture_url"] = item.img
        dic["time"] = item.time
        dic["label"] = item.tag
        dic["like"] = item.like
        dic["coin"] = item.coin
        dic["collection"] = item.collection
        dic["trans"] = item.trans

        if (not (item.intro)) or (len(item.intro) <= 1):
            dic["intro"] = "暂无简介。"
        else:
            dic["intro"] = item.intro
        tagslist = item.tag.split(" ")
        if len(tagslist) > 4:
            tagslist = tagslist[0:4]
        dic["label"] = tagslist
        videos.append(dic)

    [build_view_data(item) for item in data]
    data = {}
    data["videos"] = videos
    data["partition"] = partition
    data['trans'] = {"guichu":"鬼畜","food":"美食","movie":"影视","music":"音乐","game":"游戏"};
    return render_template("video_hot.html", data=data)


# @video.route('/time',)
# def videotime():
#     partition=request.args.get('partition')
#     videoid=request.args.get('videoid')
#     return render_template("show_video_time.html",partition=partition,videoid=videoid)

@video.route('/timeAnalyse', methods=['GET'])
def videotimeAnalyse():
    partition = request.args.get('partition')
    data = db.session.query(make_vediotime(partition)).all()
    view_data = {}
    for i in range(1, 101):
        view_data[i] = {}
        view_data[i]['x'] = []
        view_data[i]['y'] = []

    def build_view_data(item):
        # print("partition:",partition,"  ",item.id,"  ",item.grade,"  ",type(item.grade))
        view_data[item.id]['x'].append(item.grade.hour)
        view_data[item.id]['y'].append(item.cnt)
    [build_view_data(item) for item in data]


    for id in range(1, 101):
        view_data[id]['x']=view_data[id]['x'][1:]
        view_data[id]['y'] = view_data[id]['y'][1:]
        for i in range(24):
            for j in range(0, 24 - i - 1):
                if view_data[id]['x'][j] > view_data[id]['x'][j + 1]:
                    view_data[id]['x'][j], view_data[id]['x'][j + 1] = view_data[id]['x'][j + 1], view_data[id]['x'][j]
                    view_data[id]['y'][j], view_data[id]['y'][j + 1] = view_data[id]['y'][j + 1], view_data[id]['y'][j]
    return json.dumps(view_data, ensure_ascii=False)


@video.route('/keywordAnalyse', methods=['GET'])
def videokeywordAnalyse():
    partition = request.args.get('partition')
    data = db.session.query(make_vediokeyword(partition)).all()
    view_data = {}
    for i in range(1, 101):
        view_data[i] = []

    def build_view_data(item):
        dic = {}
        if item:
            dic['name'] = item.keyword  # 这里可以修改中英文
            dic['value'] = math.sqrt(item.cnt)
            view_data[item.id].append(dic)

    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象
