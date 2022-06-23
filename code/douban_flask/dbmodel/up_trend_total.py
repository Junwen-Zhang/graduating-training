from config import db


class UpTrendTotal(db.Model):
    __tablename__ = "up_trend_total"
    label=db.Column(db.String(50),primary_key=True)
    number=db.Column(db.INTEGER)

