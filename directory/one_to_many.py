# UDPwithSQLAlchemy.py
import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship

import socket, json
import binascii
from helpers import skipN, average

import pickle
engine = create_engine('sqlite:///fix_database.db')

Base = declarative_base()

class Wind_date(Base):
    __tablename__ = "wind_date"
    id = Column(Integer, primary_key=True)
    record_dt = Column(DateTime, default=datetime.datetime.utcnow)
    windspeed_ref = relationship('Wind_speed', backref='parent')

class Wind_speed(Base):
    __tablename__ = "wind_speed"
    speed_id = Column(Integer, primary_key=True)
    speed = Column(Float)
    parent_id = Column(Integer, ForeignKey("wind_date.id"))


Base.metadata.bind = engine
Base.metadata.drop_all()
Base.metadata.create_all()
Session = sessionmaker(bind=engine)
ses = Session()
# TODO: read pickle obj's
LogDate = "./alldate.pickle"
pickleObj = open(LogDate,'rb')
allDates = pickle.load(pickleObj)
pickleObj.close()
LogSpeed = "./allspeed.pickle"
pickleObj = open(LogSpeed,'rb')
allSpeeds = pickle.load(pickleObj)
pickleObj.close()

# TODO: loop here
for i in range(len(allDates)):
    dateObj = datetime.datetime.fromisoformat(allDates[i][1])
    w1 = Wind_date(record_dt = dateObj)
    ses.add(w1)
    ses.commit()
    s1 = Wind_speed(speed=allSpeeds[i][1], parent=w1)
    ses.add(s1)
    ses.commit()


# >>> ses.query(Wind_date).filter_by(record_dt='2019-08-11 10:51:47.597707').all()
# [<__main__.Wind_date object at 0x04474830>]
# >>> sometime.id
# 1
# >>> sometime.record_dt
# datetime.datetime(2019, 8, 11, 10, 51, 47, 597707)
# >>> sometime.windspeed_ref
# [<__main__.Wind_speed object at 0x04474C70>]
# >>> sometime.windspeed_ref.speed
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'InstrumentedList' object has no attribute 'speed'
# >>> sometime.windspeed_ref[0].speed
# 0.5
#==============================================
# >>> DateStart = datetime.datetime(2019, 8, 6, 14, 48, 1, 7732)
# >>> ses.query(Wind_date).filter_by(record_dt=DateStart).all()
# [<__main__.Wind_date object at 0x03AB35B0>]
# >>> someData = ses.query(Wind_date).filter_by(record_dt=DateStart).all()
# >>> someData
# [<__main__.Wind_date object at 0x03AB35B0>]
# >>> someDate[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'someDate' is not defined
# >>> someData[0]
# <__main__.Wind_date object at 0x03AB35B0>
# >>> someData[0].id
# 1
# >>> someData[0].record_dt
# datetime.datetime(2019, 8, 6, 14, 48, 1, 7732)
# >>> someData[0].windspeed_ref
# [<__main__.Wind_speed object at 0x03AB36B0>]
# >>> someData[0].windspeed_ref[0]
# <__main__.Wind_speed object at 0x03AB36B0>
# >>> someData[0].windspeed_ref[0].speed
# 0.85
# >>>
