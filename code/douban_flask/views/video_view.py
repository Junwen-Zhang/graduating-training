# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.video import make_vedio,make_vediokeyword,make_vediotime

transform={"movie":"电影","game":"游戏","music":"音乐","guichu":"鬼畜","food":"美食"}

"""
本视图专门用于处理ajax数据
"""
video = Blueprint('video', __name__)

@video.route('/main')
def videoAnalysis():
    return render_template("video_main.html")


@video.route('/showhot')
def show100video():
    partition=request.args.get('partition')
    data = db.session.query(make_vedio(partition)).all()
    videos = []
    def build_view_data(item):
        dic = {}
        dic["name"] = item.name
        dic["url"] = item.link
        dic["picture_url"] = item.img
        dic["time"] = item.time
        dic["label"]=item.tag
        dic["like"] = item.like
        dic["coin"] = item.coin
        dic["collection"] = item.collection
        dic["trans"] = item.trans

        if len(item.intro)<=5:
            dic["intro"]=""
        else:
            dic["intro"]=item.intro
        tagslist=item.tag.split(" ")
        if len(tagslist)>4:
            tagslist=tagslist[0:4]
        dic["label"]="/".join(tagslist)
        videos.append(dic)

    [build_view_data(item) for item in data]
    data={}
    data["videos"]=videos
    data["partition"]=transform[partition]+"分区"
    return render_template("video_hot.html",data=data)


@video.route('/time',)
def videotime():
    partition=request.args.get('partition')
    videoid=request.args.get('videoid')
    return render_template("show_video_time.html",partition=partition,videoid=videoid)

@video.route('/timeAnalyse',methods=['GET'])
def videotimeAnalyse():
    partition=request.args.get('partition')
    videoid=request.args.get('videoid')
    data = db.session.query(make_vediotime(partition)).all()
    view_data = {}
    view_data["x"] = []
    view_data["y"] = []
    def build_view_data(item):
        view_data["y"].append(item.count)
        view_data["x"].append(item.time)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象


@video.route('/keyword')
def videokeyword():
    partition=request.args.get('partition')
    videoid=request.args.get('videoid')
    return render_template("show_video_time.html",partition=partition,videoid=videoid)

@video.route('/keywordAnalyse',methods=['GET'])
def videokeywordAnalyse(partition,videoid):
    partition=request.args.get(partition)
    videoid=request.args.get(videoid)
    data = db.session.query(make_vediokeyword(partition)).all()
    view_data = {}
    view_data['series']=[]
    def build_view_data(item):
        dic={}
        dic['name']=item.keyword   # 这里可以修改中英文
        dic['value']=item.count
        view_data['series'].append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象

