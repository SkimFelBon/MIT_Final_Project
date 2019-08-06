# UDPwithSQLAlchemy.py
import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import sessionmaker, relationship

import socket, json
import binascii
from helpers import skipN, average

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

## To clear db use drop_all and to recreate empty db use create_all
# Base.metadata.bind = engine
# Base.metadata.drop_all()
# Base.metadata.create_all()



with open('config.json') as json_data_file:
        data = json.load(json_data_file)
localIP = data['myServer']['PPPoeIP']
localPort = int(data['myServer']['localPort'])
bufferSize = 1024

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

# Listen for incoming datagrams
i = 0
speedArray = []
try:
    while i < 50:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        #readableTime = time.localtime()
        #OpTime = time.asctime()
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        print("Message from Client:{}".format(message))
        print("Client IP Address:{}".format(address))
        # DONE: parse response
        listByte = list(message[-12:-1])
        speedArray = skipN(listByte, 1)
        # DONE: calc everage speed per 10 sec
        print(average(speedArray))
        # TODO: Write to db data
        Session = sessionmaker(bind=engine)
        ses = Session()
        w1 = Wind_date()
        ses.add(w1)
        s1 = Wind_speed(Speed=average(speedArray))
        ses.add(s1)
        ses.commit()
        # REWORK LATER increment here, just for simplicity during tests
        i+=1
finally:
    UDPServerSocket.close()
