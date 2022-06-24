# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.video import Video,VideoKeyword,VideoTime


"""
本视图专门用于处理ajax数据
"""
video = Blueprint('video', __name__)

@video.route('/main')
def videoAnalysis():
    return render_template("video_main.html")


@video.route('/showhot/<partition>')
def show100video(partition):
    data = db.session.query(video(partition)).all()
    view_data = {}
    view_data["series"] = []
    def build_view_data(item):
        dic = {}
        dic["name"] = item.name
        dic["url"] = "https://"+item.url2+"?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2"
        dic["picture_url"] = item.picture_url
        dic["followers_number"] = item.followers_number
        dic["episodes"] = item.episodes
        dic["score"] = item.score
        dic["label"]=item.label
        dic["introduction"]=item.introduction
        view_data["series"].append([dic])
    for i in range(100):
        item=data[i]
        build_view_data(item)
    return render_template("video_hot_guichu.html",fanjus=view_data)


@video.route('/time',)
def videotime():

    return render_template("show_video_time.html",partition=)

@video.route('/timeAnalyse/<partition>/<videoid>',methods=['GET'])
def videotimeAnalyse(partition,videoid):
    data = db.session.query(videotime(partition)).all()
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
    return render_template("show_video_keyword.html")

@video.route('/keywordAnalyse/<partition>/<videoid>',methods=['GET'])
def videokeywordAnalyse(partition,videoid):
    data = db.session.query(videokeyword(partition)).all()
    view_data = {}
    view_data['series']=[]
    def build_view_data(item):
        dic={}
        dic['name']=item.keyword   # 这里可以修改中英文
        dic['value']=item.count
        view_data['series'].append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象

