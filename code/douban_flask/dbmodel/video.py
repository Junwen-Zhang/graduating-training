from config import db


def make_vedio(partition):
    class Video(db.Model):
        __tablename__ = "video_" + partition + "_info"
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.INTEGER, primary_key=True)
        link = db.Column(db.String(100))
        img = db.Column(db.String(100))
        name = db.Column(db.String(50))
        tag = db.Column(db.String(100))
        time = db.Column(db.DateTime)
        up = db.Column(db.String(30))
        intro = db.Column(db.String(100))
        like = db.Column(db.INTEGER)
        coin = db.Column(db.INTEGER)
        collection = db.Column(db.INTEGER)
        trans = db.Column(db.INTEGER)
    return Video
    
def make_vediokeyword(partition):
    class VideoKeyword(db.Model):
        __tablename__ = "video_" + partition + "_keyword"
        __table_args__ = {'extend_existing': True}
        videoid = db.Column(db.INTEGER, primary_key=True)
        keyword = db.Column(db.String(10), primary_key=True)
        count = db.Column(db.Float)
    return VideoKeyword


def make_vediotime(partition):
    class VideoTime(db.Model):
        __tablename__ = "video_" + partition + "_dm_dt"
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.INTEGER, primary_key=True)
        grade = db.Column(db.DateTime, primary_key=True)
        cnt = db.Column(db.INTEGER)
    return VideoTime