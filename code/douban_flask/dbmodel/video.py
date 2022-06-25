from config import db


def make_vedio(partition):
    class Video(db.Model):
        __tablename__ = "video_" + partition + "_info"
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
        __tablename__ = "video_" + partition + "_info"
        id = db.Column(db.INTEGER)
        keyword = db.Column(db.String(20), primary_key=True)
        sqrt_count = db.Column(db.Float)
    return VideoKeyword


def make_vediotime(partition):
    class VideoTime(db.Model):
        __tablename__ = "video_" + partition + "_info"
        id = db.Column(db.INTEGER, primary_key=True)
        time = db.Column(db.String(20), primary_key=True)
        count = db.Column(db.Float)
    return VideoTime