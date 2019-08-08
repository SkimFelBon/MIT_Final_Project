from app import db
import datetime
class Wind_date(db.Model):
    __tablename__ = "winddate"

    Id = db.Column(db.Integer, primary_key=True)
    Record_dt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    Windspeed_ref = db.relationship('Wind_speed', backref='windspeed')


class Wind_speed(db.Model):
    __tablename__ = "wind_speed"

    SpeedId = db.Column(db.Integer, primary_key=True)
    Speed = db.Column(db.Float, nullable=False)
    DatetimeId = db.Column(db.Integer, db.ForeignKey("winddate.Id"))

    Wind_date = db.relationship("Wind_date")
