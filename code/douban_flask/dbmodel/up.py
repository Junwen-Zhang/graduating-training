from config import db


class Up(db.Model):
    __tablename__ = "sorted_up"    # 按照粉丝数进行了排序
    uid=db.Column(db.String(50))
    name=db.Column(db.String(50))
    picture_url=db.Column(db.String(100))
    fans=db.Column(db.INTEGER)
    evaluation=db.Column(db.String(255))
    url=db.Column(db.String(100),primary_key=True)



