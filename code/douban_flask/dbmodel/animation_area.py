from config import db


class AnimationArea(db.Model):
    __tablename__ = "fanju_area_count"
    area =db.Column(db.String(50),primary_key=True)
    count=db.Column(db.INTEGER)