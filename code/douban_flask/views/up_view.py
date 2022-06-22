# -*- coding:utf-8 -*-
import json

from flask import Blueprint, jsonify, request, render_template

from config import db
from dbmodel.up import Up

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