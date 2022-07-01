from config import db


class GuichuLength(db.Model):
    __tablename__ = "guichu_length_interval_count"
    id = db.Column(db.INTEGER, primary_key=True)
    interval = db.Column(db.String(10))
    count=db.Column(db.INTEGER)

class GuichuSubmitHour(db.Model):
    __tablename__ = "guichu_submithour_count"
    hour = db.Column(db.INTEGER, primary_key=True)
    count = db.Column(db.INTEGER)

class GuichuTags(db.Model):
    __tablename__ = "guichu_tags"
    tag = db.Column(db.String(20), primary_key=True)
    sqrt_count = db.Column(db.Float)
