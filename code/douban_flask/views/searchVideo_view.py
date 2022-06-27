
# -*- coding:utf-8 -*-
import json

import requests
from flask import Blueprint, jsonify, request, render_template
from spider.linkAnalys import LinkAnls
from compute.anime_tags import getTagsDict, get100TagsDict

"""
本视图专门用于处理ajax数据
"""
search = Blueprint('search', __name__)

@search.route('/main')
def commentmain():
    link = request.args.get('link')

    global la
    la = LinkAnls(link)
    la.getData()
    datalist = {}
    datalist["allinfo"] = la.allinfo
    print(datalist["allinfo"])
    datalist["comment"] = la.video_comment[0:11]
    # datalist["show"] =
    # print('comment',comment)
    return render_template("searchVideo_main.html",data=datalist)

@search.route('/show',methods=['GET'])
def CommentAnaly():
    comment_keyword = la.comment_keywords
    # print(comment_keyword)
    datalst={}
    datalst["comment_keyword"] = []

    def build_view_data2(keyword):
        for item in keyword:
            if item[1]>5:
                data = {}
                data['name'] = item[0]
                data['value'] = item[1]
                datalst["comment_keyword"].append(data)

    build_view_data2(comment_keyword)
    print("data: ",datalst["comment_keyword"])
    return json.dumps(datalst, ensure_ascii=False)  # 将python对象转化为json对象

