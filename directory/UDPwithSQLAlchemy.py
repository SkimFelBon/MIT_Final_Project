# UDPwithSQLAlchemy.py
import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///wind_of_change.db')

Base = declarative_base()

class Wind_date(Base):
    __tablename__ = "winddate"

    Id = Column(Integer, primary_key=True)
    Record_dt = Column(DateTime, default=datetime.datetime.utcnow)
    Windspeed_ref = relationship('Wind_speed', backref='windspeed')

class Wind_speed(Base):
    __tablename__ = "wind_speed"

    SpeedId = Column(Integer, primary_key=True)
    Speed = Column(Float, nullable=False)
    DatetimeId = Column(Integer, ForeignKey("winddate.Id"))

    Wind_date = relationship("Wind_date")

# Base.metadata.bind = engine
# Base.metadata.create_all()

Session = sessionmaker(bind=engine)
ses = Session()
w1 = Wind_date()
s1 = Wind_speed(Speed=5)
ses.add(w1)
ses.add(s1)
ses.commit()
