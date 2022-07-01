from config import db


def make_vedio(partition):
    class Video(db.Model):
        __tablename__ = "video_" + partition + "_info"
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.INTEGER, primary_key=True)
        link = db.Column(db.String(100))
        img = db.Column(db.String(100))
        name = db.Column(db.String(100))
        tag = db.Column(db.String(100))
        time = db.Column(db.DateTime)
        up = db.Column(db.String(30))
        intro = db.Column(db.String(500))
        like = db.Column(db.String(15))
        coin = db.Column(db.String(15))
        collection = db.Column(db.String(15))
        trans = db.Column(db.String(15))
    return Video
    
def make_vediokeyword(partition):
    class VideoKeyword(db.Model):
        __tablename__ = "video_" + partition + "_dm_keyword"
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.INTEGER, primary_key=True)
        keyword = db.Column(db.String(255), primary_key=True)
        cnt = db.Column(db.INTEGER)
    return VideoKeyword


def make_vediotime(partition):
    class VideoTime(db.Model):
        __tablename__ = "video_" + partition + "_dm_dt"
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.INTEGER, primary_key=True)
        grade = db.Column(db.DateTime, primary_key=True)
        cnt = db.Column(db.INTEGER)
    return VideoTime