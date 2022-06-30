# -*- coding:utf-8 -*-
from flask import Blueprint, render_template

"""
本视图专门用于处理页面
"""
index = Blueprint('index', __name__)


@index.route('/', endpoint="index")
def login():
    return render_template("searchVideo.html")
