from config import db


class GuichuLength(db.Model):
    __tablename__ = "guichu_length_interval_count"
    id = db.Column(db.INTEGER, primary_key=True)
    interval = db.Column(db.String(10))
    count=db.Column(db.INTEGER)
