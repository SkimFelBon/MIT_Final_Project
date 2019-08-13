# read_old_log.py
import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship

from udphelpers import average, findSpeed

engine = create_engine('sqlite:///newDataBase.db')

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

path = "C:/MyPythonScripts/myGitHub/Winter/tests/winter.log"

with open('winter.log','r') as f:
    for line in f:
        # DONE make DateTime object
        rowDate = line[0:10] + ' ' + line[14:22]
        dateObj = datetime.datetime.strptime(rowDate,"%Y:%m:%d %H:%M:%S")
        # TODO calculate average speed
        # this one dosn't work
            # speed = line[37:64]
            # speedArrayStr = speed.split('  ')
            # SpeedArrayInt = list(map(lambda x: int(x), speedArrayStr))
        SpeedArrayInt = findSpeed(line)
        aSpeed = average(SpeedArrayInt)
        # TODO write to db
        w1 = Wind_date(record_dt = dateObj)
        ses.add(w1)
        s1 = Wind_speed(speed=aSpeed, parent=w1)
        ses.add(s1)
        ses.commit()
