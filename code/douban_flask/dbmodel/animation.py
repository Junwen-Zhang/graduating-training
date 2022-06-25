from config import db

# 番剧基本信息
class Animation(db.Model):
    __tablename__ = "fanju"
    # id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name=db.Column(db.String(50))
    subtitle=db.Column(db.String(50))
    url=db.Column(db.String(100),primary_key=True)    # 直接开始开始看的网址
    picture_url=db.Column(db.String(100))
    followers_number=db.Column(db.INTEGER)
    episodes=db.Column(db.String(50))
    score=db.Column(db.DECIMAL(3,1))
    label=db.Column(db.String(100))
    release_time=db.Column(db.String(100))
    views=db.Column(db.String(100))
    area=db.Column(db.String(20))
    url2=db.Column(db.String(100))     # 需要跳转的网址
    introduction=db.Column(db.String(255))

# 统计番剧的地区分布
class AnimationArea(db.Model):
    __tablename__ = "fanju_area_count"
    area =db.Column(db.String(50),primary_key=True)
    count=db.Column(db.INTEGER)

# 统计番剧的分数分布
class AnimationScore(db.Model):
    __tablename__ = "fanju_score_count"
    score = db.Column(db.DECIMAL(3, 1), primary_key=True)
    count=db.Column(db.INTEGER)
