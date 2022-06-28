from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# url的格式为：数据库的协议：//用户名：密码@ip地址：端口号（默认可以不写）/数据库名
# 兰庆秋
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@192.168.66.121:3306/bilibili"

# 章俊文
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@127.0.0.1:3306/bilibili"

# 杨雅馨
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@192.168.80.150:3306/guichu"

#张倩
#app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:12345678@192.168.80.155:3306/bilibili"
# 动态追踪数据库的修改. 性能不好. 且未来版本中会移除. 目前只是为了解决控制台的提示才写的
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# 创建数据库的操作对象
db = SQLAlchemy(app)