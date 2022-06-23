from config import db

class GuichuTags(db.Model):
    __tablename__ = "guichu_tags"
    tag = db.Column(db.String(20), primary_key=True)
    sqrt_count = db.Column(db.Float)