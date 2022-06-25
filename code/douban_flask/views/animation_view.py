# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.animation import Animation
from dbmodel.animation import AnimationArea
from dbmodel.animation import AnimationScore
from compute.anime_tags import getTagsDict, get100TagsDict

"""
本视图专门用于处理ajax数据
"""
animation = Blueprint('animation', __name__)

@animation.route('/main')
def animationAnalysis():
    return render_template("animation_main.html")

@animation.route('/show100animation')
def show100animation():
    data = db.session.query(Animation).all()
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
    return render_template("show100animation.html",fanjus=view_data)

@animation.route('/score')
def animationScore():
    return render_template("show_animation_score.html")

@animation.route('/scoreAnalyse',methods=['GET'])
def animationScoreAnalyse():
    data = db.session.query(AnimationScore).all()
    view_data = {}
    view_data["x"] = []
    view_data["y"] = []
    def build_view_data(item):
        view_data["y"].append(item.count)
        view_data["x"].append(item.score)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象

@animation.route('/area')
def animationArea():
    return render_template("show_animation_area.html")

@animation.route('/areaAnalyse',methods=['GET'])
def animationAreaAnalyse():
    data = db.session.query(AnimationArea).all()
    view_data = {}
    view_data['series']=[]
    def build_view_data(item):
        dic={}
        dic['name']=item.area   # 这里可以修改中英文
        dic['value']=item.count
        view_data['series'].append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象


@animation.route('/tagsAnalyse',methods=['GET'])
def animationTagsAnalyse():
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


@animation.route('/animeTags')
def animationTags():
    return render_template("animation_tags.html")