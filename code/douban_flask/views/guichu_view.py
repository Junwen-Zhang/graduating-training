# -*- coding:utf-8 -*-
import json

from flask import Blueprint, render_template

from config import db
from dbmodel.guichu import GuichuLength,GuichuSubmitHour,GuichuTags



"""
本视图专门用于处理ajax数据
"""
guichu = Blueprint('guichu', __name__)

@guichu.route('/main')
def guichuAnalysis():
    return render_template("guichu_main.html")


@guichu.route('/keyword')
def guichuLength():
    return render_template("vedio_keyword.html")

@guichu.route('/keywordAnalyse',methods=['GET'])
def guichuLengthAnalyse():
    data = db.session.query(GuichuLength).all()
    view_data = []

    def build_view_data(item):
        dic={}
        dic["name"]=item.interval
        dic["value"]=item.count
        view_data.append(dic)
    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象


@guichu.route('/submithour')
def guichuSubmitHour():
    return render_template("show_guichu_submithour.html")

@guichu.route('/submitHourAnalyse',methods=['GET'])
def guichuSubmitHourAnalyse():
    data = db.session.query(GuichuSubmitHour).all()
    view_data={}
    view_data['x'] = []
    view_data['y'] = []

    def build_view_data(item):
        view_data['x'].append(item.hour)
        view_data['y'].append(item.count)
    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象

@guichu.route('/wordcloud')
def guichuWordcloud():
    return render_template("show_guichu_wordcloud.html")

@guichu.route('/wordcloudAnalyse',methods=['GET'])
def guichuWordcloudAnalyse():
    data = db.session.query(GuichuTags).all()
    view_data=[]

    def build_view_data(item):
        view_data.append({"name":item.tag,"value":item.sqrt_count})
    [build_view_data(item) for item in data]

    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象