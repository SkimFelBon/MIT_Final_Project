from app import db

class Wind_date(db.Base):
    __tablename__ = "winddate"

    Id = db.Column(db.Integer, primary_key=True)
    Record_dt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    Windspeed_ref = db.relationship('Wind_speed', backref='windspeed')


class Wind_speed(db.Base):
    __tablename__ = "wind_speed"

    SpeedId = db.Column(db.Integer, primary_key=True)
    Speed = db.Column(db.Float, nullable=False)
    DatetimeId = db.Column(db.Integer, ForeignKey("winddate.Id"))

    Wind_date = db.relationship("Wind_date")
