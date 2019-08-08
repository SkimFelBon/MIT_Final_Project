# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime
##import logging
##logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
##logging.warning('is when this event was logged.')
app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
from models import Wind_date, Wind_speed

@app.route("/")
def index():
    # TODO: index page should provide last 5 min of wind speed
    # range query from mm:ss to mm:sec
    # how to specify date??
    DateStart = datetime.datetime(2019, 8, 6, 14, 48, 1, 7732)
    DateEnd = datetime.datetime(2019, 8, 6, 14, 56, 12, 726856)
    # someDate = (50, '2019-08-06 14:56:12.726856')
    # Probably I need to convert string to DateTimeObject
    # datetime.datetime(2019, 8, 8, 14, 25, 58, 376145)
    # (1, '2019-08-06 14:48:01.007732')
    # ...
    # (50, '2019-08-06 14:56:12.726856')

    ## qry = DBSession.query(User).filter(User.birthday.between('1985-01-17', '1988-01-17'))
    qry = Wind_date.query.filter_by(Record_dt >= DateStart).all()
    # return range of speeds/dates
    app.logger.warning(f"Dates in Range: {qry}")
    ImageLocation = "static/images/Figure_1.png"
    return render_template("index.html", ImageLocation=ImageLocation)

@app.route("/alldata")
def alldata():
    # TODO: simple case query db for all data
    ## myQuery = Wind_speed.query.all()
    ## app.logger.warning(f'Wind speed from db: {myQuery}')

    ImageLocation = "static/images/Figure_1.png"
    return render_template("alldata.html", ImageLocation=ImageLocation)

if __name__ == "__main__":
    app.run()
