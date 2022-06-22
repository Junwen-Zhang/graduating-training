# -*- coding:utf-8 -*-
import json

from flask import Blueprint, render_template

from config import db
from dbmodel.guichu_length import GuichuLength


"""
本视图专门用于处理ajax数据
"""
guichu = Blueprint('guichu', __name__)

@guichu.route('/main')
def guichuAnalysis():
    return render_template("guichu_main.html")

@guichu.route('/length')
def guichuLength():
    return render_template("show_guichu_length.html")

@guichu.route('/lengthAnalyse',methods=['GET'])
def guichuLengthAnalyse():
    data = db.session.query(GuichuLength).all()
    view_data = []

    def build_view_data(item):
        dic={}
        dic["name"]=item.interval
        dic["value"]=item.count
        view_data.append(dic)
    [build_view_data(item) for item in data]
    print("view_data")
    print(view_data)
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象
