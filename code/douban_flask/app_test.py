#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Filename: app_test.py

from flask import  Flask

app_test = Flask(__name__)

@app_test.route('/')
def hello():
    return "hello worsad545645656ddld"


if __name__ == '__main__':
    #app_test.run()
    app_test.run(debug=True)