# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.video import VideoLength,VideoSubmitHour,VideoTags


"""
本视图专门用于处理ajax数据
"""
video = Blueprint('video', __name__)

@video.route('/main')
def videoAnalysis():
    return render_template("video_main.html")

@video.route('/show100video')
def show100video():
    data = db.session.query(video).all()
    view_data = {}
    view_data["series"] = []
    def build_view_data(item):
        dic = {}
        dic["name"] = item.name
        dic["url"] = "https://"+item.url2+"?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2"
        dic["picture_url"] = item.picture_url
        dic["followers_number"] = item.followers_number
        dic["episodes"] = item.episodes
        dic["time"] = item.time
        dic["label"]=item.label
        dic["introduction"]=item.introduction
        view_data["series"].append([dic])
    for i in range(100):
        item=data[i]
        build_view_data(item)
    return render_template("show100video.html",fanjus=view_data)

@video.route('/time')
def videotime():
    return render_template("show_video_time.html")

@video.route('/timeAnalyse',methods=['GET'])
def videotimeAnalyse():
    data = db.session.query(videotime).all()
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

@video.route('/keywordAnalyse',methods=['GET'])
def videokeywordAnalyse():
    data = db.session.query(videokeyword).all()
    view_data = {}
    view_data['series']=[]
    def build_view_data(item):
        dic={}
        dic['name']=item.keyword   # 这里可以修改中英文
        dic['value']=item.count
        view_data['series'].append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象


@video.route('/tagsAnalyse',methods=['GET'])
def videoTagsAnalyse():
    Tags_dict = getTagsDict()
    view_data={}
    view_data["series1"] = []
    def build_view_data(Tags_dict):
        for key,value in Tags_dict.items():
            data = {}
            data['name'] = key
            data['value'] = value
            view_data['series1'].append(data)
    build_view_data(Tags_dict)

    Tags_dict2 = get100TagsDict()
    view_data["series2"] = []
    def build_view_data2(Tags_dict):
        for key, value in Tags_dict.items():
            data = {}

            data['name'] = key
            data['value'] = value
            view_data['series2'].append(data)
    build_view_data2(Tags_dict2)
    view_data['maskImage']='./img/tree.jpg'
    # print(view_data)
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象


@video.route('/animeTags')
def videoTags():
    return render_template("video_tags.html")