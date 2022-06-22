#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: app_test.py

import json
from flask import render_template
import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@192.168.66.121:3306/bilibili"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)



from dbmodel.Animation_score import AnimationScore
from dbmodel.Animation import Animation


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/index')
def home():
    return render_template("index.html")
    # return index()


@app.route('/movie')
def movie():
    datalist  = []
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    print(datalist)
    return render_template("movie.html",movies = datalist)



@app.route('/score')
def score():
    score = []  #评分
    num = []    #每个评分所统计出的电影数量
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        score.append(str(item[0]))
        num.append(item[1])

    cur.close()
    con.close()
    return render_template("score.html",score= score,num=num)


@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/test')
def hello_world():
    return 'Hello World!'


@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/animationAnalysis')
def animationAnalysis():
    return render_template("animation_main.html")

@app.route('/show100animation')
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

@app.route('/animationScore')
def animationScore():
    # print('animationScore')
    return render_template("showAnimationScore.html")

@app.route('/animationScoreAnalyse',methods=['GET'])
def animationScoreAnalyse():
    print('animationScoreAnalyse')
    data = db.session.query(AnimationScore).all()
    view_data = {}
    view_data["x"] = []
    view_data["y"] = []

    def build_view_data(item):
        view_data["y"].append(item.count)
        view_data["x"].append(item.score)
    [build_view_data(item) for item in data]
    print(view_data)
    return json.dumps(view_data, ensure_ascii=False)  # 将python对象转化为json对象


if __name__ == '__main__':
    app.run()
