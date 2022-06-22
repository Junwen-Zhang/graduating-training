from app import db


class AnimationScore(db.Model):
    __tablename__ = "fanju_score_count"
    score = db.Column(db.DECIMAL(3, 1), primary_key=True)
    count=db.Column(db.INTEGER)



