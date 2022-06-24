from config import db


class Video(db.Model):
    __tablename__ = "video"
    id = db.Column(db.INTEGER, primary_key=True)
    interval = db.Column(db.String(10))
    count=db.Column(db.INTEGER)
    

class VideoKeyword(db.Model):
    __tablename__ = "video_keyword"
    id = db.Column(db.INTEGER)
    keyword = db.Column(db.String(20), primary_key=True)
    sqrt_count = db.Column(db.Float)

class VideoTime(db.Model):
    __tablename__ = "video_time"
    id = db.Column(db.INTEGER, primary_key=True)
    time = db.Column(db.String(20), primary_key=True)
    count = db.Column(db.Float)