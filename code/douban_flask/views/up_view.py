# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.up import Up
from dbmodel.up_trend_total import UpTrendTotal

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

@up.route('/getUpFans')
def getUpFans():
    # 需要修改数据结构，暂定为现有的数据
    data = db.session.query(UpTrendTotal).all()
    view_data = []

    def build_view_data(item):
        dic = {}
        dic['name'] = item.label
        dic['value'] = item.number
        view_data.append(dic)

    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)



















