# -*- coding:utf-8 -*-
import json

from flask import Blueprint,render_template

from config import db
from dbmodel.up import Up,UpTrendTotal,UpFansTrend,MostPopularUp,MostPopularUpVideo,MostPopularUpVideosTagsCount,UpTags

up = Blueprint('up', __name__)

@up.route('/main')
def upAnalysis():
    # return render_template("up_main.html")
    return render_template("up-main-2.html")

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
    return render_template("show100up-2.html", ups=view_data)

@up.route('/trend')
def showUpTrend():
    return render_template("show-up-trend-2.html")
    # return render_template("show_up_trend.html")

@up.route('/getUpTrend',methods=["GET"])
def getUpTrend():
    data=db.session.query(UpTrendTotal).all()
    view_data=[]
    def build_view_data(item):
        dic={}
        dic['name']=item.label
        dic['value']=item.number
        if(dic['name']!='总视频数'):   # 去除总视频数
            view_data.append(dic)
    [build_view_data(item) for item in data]
    return json.dumps(view_data, ensure_ascii=False)

# 展示20个up主粉丝变化趋势页面
@up.route('/fans')
def showFans():
    # return render_template("show_up_fans.html")
    return render_template("show-up-fans-2.html")

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

# 得到百大up的视频的tags
@up.route('/getUpTags')
def getUpTags():
    data = db.session.query(UpTags).all()
    view_data = []
    def build_view_data(item):
        dic={}
        dic['uid']=item.uid
        dic['data']=[]
        dic2={}
        dic2['name']='生活'
        dic2['value']=item.live
        if(dic2['value']==None):
            dic2['value']=0
        if(dic2['value']>=3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '影视'
        dic2['value'] = item.movie
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '科技'
        dic2['value'] = item.technology
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '动物圈'
        dic2['value'] = item.animal
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '动画'
        dic2['value'] = item.animation
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '电视剧'
        dic2['value'] = item.teleplay
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '音乐'
        dic2['value'] = item.music
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '知识'
        dic2['value'] = item.knowledge
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '游戏'
        dic2['value'] = item.game
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '时尚'
        dic2['value'] = item.fashion
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '纪录片'
        dic2['value'] = item.documentary
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '美食'
        dic2['value'] = item.food
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '汽车'
        dic2['value'] = item.car
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '运动'
        dic2['value'] = item.sport
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '娱乐'
        dic2['value'] = item.entertainment
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '舞蹈'
        dic2['value'] = item.dance
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '国创'
        dic2['value'] = item.guochuang
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '资讯'
        dic2['value'] = item.information
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

        dic2 = {}
        dic2['name'] = '鬼畜'
        dic2['value'] = item.guichu
        if (dic2['value'] == None):
            dic2['value'] = 0
        if (dic2['value'] >= 3):
            dic['data'].append(dic2)

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
    for i in range(21):
        if i==9:
            continue
        dic={}
        dic['picture_url']=data2[i].picture_url
        dic['title']=data2[i].title
        dic['introduction']=data2[i].introduction
        dic['url']=data2[i].url
        dic['views']=data2[i].views
        dic['danmus']=data2[i].danmus
        dic['likes']=data2[i].likes
        dic['coins']=data2[i].coins
        dic['collections']=data2[i].collections
        # dic['tags']=data2[i].tags.split(' ')
        tag_list = data2[i].tags.split(' ')
        tag_2 = []
        for j in range(4):
            tag_2.append(tag_list[j])
        dic['tags'] = tag_2
        view_data2.append(dic)
    # return render_template("show_most_popular_up.html", ups=view_data,videos=view_data2)
    return render_template("show-most-popular-up-2.html", ups=view_data, videos=view_data2)


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




















