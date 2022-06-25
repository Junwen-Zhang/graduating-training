# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.up import Up
from dbmodel.up import UpTrendTotal
from dbmodel.up import UpFansTrend
from dbmodel.up import MostPopularUp,MostPopularUpVideo,MostPopularUpVideosTagsCount

up = Blueprint('up', __name__)

@up.route('/main')
def upAnalysis():
    return render_template("up_main.html")

@up.route('/show100up')
def show100up():
    data=db.session.query(Up).all()
    view_data=[]
    def build_view_data(item):
        dic={}
        dic['uid']=item.uid
        dic['name']=item.name
        dic['picture_url']=item.picture_url
        dic['fans']=item.fans
        dic['evaluation']=item.evaluation
        dic['url']=item.url
        view_data.append(dic)
    [build_view_data(item) for item in data]
    return render_template("show100up.html",ups=view_data)

@up.route('/trend')
def showUpTrend():
    return render_template("show_up_trend.html")

@up.route('/getUpTrend',methods=["GET"])
def getUpTrend():
    data=db.session.query(UpTrendTotal).all()
    view_data=[]
    def build_view_data(item):
        dic={}
        dic['name']=item.label
        dic['value']=item.number
        view_data.append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)

# 展示20个up主粉丝变化趋势页面
@up.route('/fans')
def showFans():
    return render_template("show_up_fans.html")

# 得到二十个up主的近一个月的粉丝变化
@up.route('/getUpFans')
def getUpFans():
    data = db.session.query(UpFansTrend).all()
    view_data = []

    def build_view_data(item):
        dic = []
        dic.append(item.uid)
        dic.append(item.name)
        dic.append(item.f0523)
        dic.append(item.f0524)
        dic.append(item.f0525)
        dic.append(item.f0526)
        dic.append(item.f0527)
        dic.append(item.f0528)
        dic.append(item.f0529)
        dic.append(item.f0530)
        dic.append(item.f0531)
        dic.append(item.f0601)
        dic.append(item.f0602)
        dic.append(item.f0603)
        dic.append(item.f0604)
        dic.append(item.f0605)
        dic.append(item.f0606)
        dic.append(item.f0607)
        dic.append(item.f0608)
        dic.append(item.f0609)
        dic.append(item.f0610)
        dic.append(item.f0611)
        dic.append(item.f0612)
        dic.append(item.f0613)
        dic.append(item.f0614)
        dic.append(item.f0615)
        dic.append(item.f0616)
        dic.append(item.f0617)
        dic.append(item.f0618)
        dic.append(item.f0619)
        dic.append(item.f0620)
        dic.append(item.f0621)
        dic.append(item.origin)
        dic.append(item.result)

        view_data.append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)

# 展示最受欢迎up主的基本信息
@up.route('/showMostPopularUp')
def showMostPolpularUp():
    # 最受欢迎up主的主要信息
    data=db.session.query(MostPopularUp).all()
    view_data=[]
    def selectData(item):
        dic={}
        if(item.uid=="517327498"):
            dic['uid']=item.uid
            dic['name']=item.name
            dic['fans']=item.fans
            dic['likes']=item.likes
            dic['views']=item.views
            dic['section']=item.section.split(' ')
            data2=db.session.query(Up).filter(Up.uid==item.uid).first()
            dic['picture_url']=data2.picture_url
            dic['url']=data2.url
            view_data.append(dic)
    [selectData(item) for item in data]

    # 最受欢迎的up主的热门视频
    data2=db.session.query(MostPopularUpVideo).all()
    view_data2=[]
    for i in range(10):
        dic={}
        dic['picture_url']=data2[i].picture_url
        dic['title']=data2[i].title
        dic['introduction']=data2[i].introduction
        dic['url']=data2[i].url
        dic['views']=data2[i].views
        dic['tags']=data2[i].tags.split(' ')
        view_data2.append(dic)
    return render_template("show_most_popular_up.html", ups=view_data,videos=view_data2)

# 得到画出最受欢迎的up主的视频的标签的统计数据
@up.route('/getMostPopularUpVideosTags')
def getMostPopularUpVideosTags():
    data=db.session.query(MostPopularUpVideosTagsCount)
    view_data=[]
    def build_view_data(item):
        dic={}
        dic['name']=item.tag
        dic['value']=item.count
        if(dic['value']>10):
            view_data.append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)
    



















