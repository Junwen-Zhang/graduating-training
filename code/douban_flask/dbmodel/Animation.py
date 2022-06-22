from app import db


class Animation(db.Model):
    __tablename__ = "fanju"
    # id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    name=db.Column(db.String(50))
    subtitle=db.Column(db.String(50))
    url=db.Column(db.String(100),primary_key=True)
    picture_url=db.Column(db.String(100))
    followers_number=db.Column(db.INTEGER)
    episodes=db.Column(db.String(50))
    score=db.Column(db.DECIMAL(3,1))

