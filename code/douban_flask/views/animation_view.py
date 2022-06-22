# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.animation import Animation
from dbmodel.animation_score import AnimationScore


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
        dic["subtitle"] = item.subtitle
        dic["url"] = item.url
        dic["picture_url"] = item.picture_url
        dic["followers_number"] = item.followers_number
        dic["episodes"] = item.episodes
        dic["score"] = item.score
        view_data["series"].append([dic])
    [build_view_data(item) for item in data]

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
