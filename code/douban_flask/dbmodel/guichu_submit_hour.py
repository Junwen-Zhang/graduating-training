from config import db

class GuichuSubmitHour(db.Model):
    __tablename__ = "guichu_submithour_count"
    hour = db.Column(db.INTEGER, primary_key=True)
    count = db.Column(db.INTEGER)
