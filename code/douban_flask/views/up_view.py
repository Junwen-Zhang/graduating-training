# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.up import Up
from dbmodel.up_trend_total import UpTrendTotal
from dbmodel.up_fans_trend import UpFansTrend

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

# 展示20个up主粉丝变化趋势
@up.route('/fans')
def showFans():
    return render_template("fans.html")

# 得到二十个up主的近一个月的粉丝变化
@up.route('/getUpFans')
def getUpFans():
    # 需要修改数据结构，暂定为现有的数据
    data = db.session.query(UpFansTrend).all()
    view_data = []

    def build_view_data(item):
        dic = []
        sum=item.f0523
        dic.append(item.uid)
        dic.append(item.name)
        dic.append(item.f0523)
        dic.append(item.f0524+sum)
        sum+=item.f0524
        dic.append(item.f0525+sum)
        sum+=item.f0525
        dic.append(item.f0526+sum)
        sum+=item.f0526
        dic.append(item.f0527+sum)
        sum+=item.f0527
        dic.append(item.f0528+sum)
        sum+=item.f0528
        dic.append(item.f0529+sum)
        sum+=item.f0529
        dic.append(item.f0530+sum)
        sum+=item.f0530
        dic.append(item.f0531+sum)
        sum+=item.f0531
        dic.append(item.f0601+sum)
        sum+=item.f0601
        dic.append(item.f0602+sum)
        sum+=item.f0602
        dic.append(item.f0603+sum)
        sum+=item.f0603
        dic.append(item.f0604+sum)
        sum+=item.f0604
        dic.append(item.f0605+sum)
        sum+=item.f0605
        dic.append(item.f0606+sum)
        sum+=item.f0606
        dic.append(item.f0607+sum)
        sum+=item.f0607
        dic.append(item.f0608+sum)
        sum+=item.f0608
        dic.append(item.f0609+sum)
        sum+=item.f0609
        dic.append(item.f0610+sum)
        sum+=item.f0610
        dic.append(item.f0611+sum)
        sum+=item.f0611
        dic.append(item.f0612+sum)
        sum+=item.f0612
        dic.append(item.f0613+sum)
        sum+=item.f0613
        dic.append(item.f0614+sum)
        sum+=item.f0614
        dic.append(item.f0615+sum)
        sum+=item.f0615
        dic.append(item.f0616+sum)
        sum+=item.f0616
        dic.append(item.f0617+sum)
        sum+=item.f0617
        dic.append(item.f0618+sum)
        sum+=item.f0618
        dic.append(item.f0619+sum)
        sum+=item.f0619
        dic.append(item.f0620+sum)
        sum+=item.f0620
        dic.append(item.f0621+sum)
        dic.append(item.origin+sum)
        dic.append(item.result+sum)
        # dic.append(item.uid)
        # dic.append(item.name)
        # dic.append(item.f0523)
        # dic.append(item.f0524)
        # dic.append(item.f0525)
        # dic.append(item.f0526)
        # dic.append(item.f0527)
        # dic.append(item.f0528)
        # dic.append(item.f0529)
        # dic.append(item.f0530)
        # dic.append(item.f0531)
        # dic.append(item.f0601)
        # dic.append(item.f0602)
        # dic.append(item.f0603)
        # dic.append(item.f0604)
        # dic.append(item.f0605)
        # dic.append(item.f0606)
        # dic.append(item.f0607)
        # dic.append(item.f0608)
        # dic.append(item.f0609)
        # dic.append(item.f0610)
        # dic.append(item.f0611)
        # dic.append(item.f0612)
        # dic.append(item.f0613)
        # dic.append(item.f0614)
        # dic.append(item.f0615)
        # dic.append(item.f0616)
        # dic.append(item.f0617)
        # dic.append(item.f0618)
        # dic.append(item.f0619)
        # dic.append(item.f0620)
        # dic.append(item.f0621)
        # dic.append(item.origin)
        # dic.append(item.result)

        view_data.append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)



















