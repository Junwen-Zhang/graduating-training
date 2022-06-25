from config import db

# up基本信息
class Up(db.Model):
    __tablename__ = "sorted_up"    # 按照粉丝数进行了排序
    uid=db.Column(db.String(50))
    name=db.Column(db.String(50))
    picture_url=db.Column(db.String(100))
    fans=db.Column(db.INTEGER)
    evaluation=db.Column(db.String(255))
    url=db.Column(db.String(100),primary_key=True)

# 近一个月up粉丝变化趋势
class UpFansTrend(db.Model):
    __tablename__ = "up_fans_trend"
    uid=db.Column(db.String(50),primary_key=True)
    name=db.Column(db.String(50))
    f0523 = db.Column(db.INTEGER)
    f0524 = db.Column(db.INTEGER)
    f0525 = db.Column(db.INTEGER)
    f0526 = db.Column(db.INTEGER)
    f0527 = db.Column(db.INTEGER)
    f0528 = db.Column(db.INTEGER)
    f0529 = db.Column(db.INTEGER)
    f0530 = db.Column(db.INTEGER)
    f0531 = db.Column(db.INTEGER)
    f0601 = db.Column(db.INTEGER)
    f0602 = db.Column(db.INTEGER)
    f0603 = db.Column(db.INTEGER)
    f0604 = db.Column(db.INTEGER)
    f0605 = db.Column(db.INTEGER)
    f0606 = db.Column(db.INTEGER)
    f0607 = db.Column(db.INTEGER)
    f0608 = db.Column(db.INTEGER)
    f0609 = db.Column(db.INTEGER)
    f0610 = db.Column(db.INTEGER)
    f0611 = db.Column(db.INTEGER)
    f0612 = db.Column(db.INTEGER)
    f0613 = db.Column(db.INTEGER)
    f0614 = db.Column(db.INTEGER)
    f0615 = db.Column(db.INTEGER)
    f0616 = db.Column(db.INTEGER)
    f0617 = db.Column(db.INTEGER)
    f0618 = db.Column(db.INTEGER)
    f0619 = db.Column(db.INTEGER)
    f0620 = db.Column(db.INTEGER)
    f0621 = db.Column(db.INTEGER)
    origin = db.Column(db.INTEGER)
    result = db.Column(db.INTEGER)

# up创作标签分布（创作流行趋势）
class UpTrendTotal(db.Model):
    __tablename__ = "up_trend_total"
    label=db.Column(db.String(50),primary_key=True)
    number=db.Column(db.INTEGER)

# 最受欢迎up主的基本信息
class MostPopularUp(db.Model):
    __tablename__="most_popular_up"
    uid=db.Column(db.String(50))
    name=db.Column(db.String(50))
    section=db.Column(db.String(100))
    fans=db.column(db.INTEGER)
    likes=db.Column(db.String(50))
    views=db.Column(db.String(50))


