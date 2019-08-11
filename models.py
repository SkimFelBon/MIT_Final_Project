from app import db
import datetime

class Wind_date(db.Model):
    __tablename__ = "wind_date"
    id = db.Column(db.Integer, primary_key=True)
    record_dt = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    windspeed_ref = db.relationship('Wind_speed', backref='parent')


class Wind_speed(db.Model):
    __tablename__ = "wind_speed"
    speed_id = db.Column(db.Integer, primary_key=True)
    speed = db.Column(db.Float)
    parent_id = db.Column(db.Integer, db.ForeignKey("wind_date.id"))
