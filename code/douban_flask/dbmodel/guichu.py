from config import db


class GuichuLength(db.Model):
    def __init__(self,partition):
        super().__init__()
        __tablename__ = partition
    
    id = db.Column(db.INTEGER, primary_key=True)
    interval = db.Column(db.String(10))
    count=db.Column(db.INTEGER)


class GuichuSubmitHour(db.Model):
    def __init__(self,partition):
        super().__init__()
        __tablename__ = partition

    hour = db.Column(db.INTEGER, primary_key=True)
    count = db.Column(db.INTEGER)


class GuichuTags(db.Model):
    def __init__(self,partition):
        super().__init__()
        __tablename__ = partition

    tag = db.Column(db.String(20), primary_key=True)
    sqrt_count = db.Column(db.Float)
