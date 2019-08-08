# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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
    ImageLocation = "static/images/Figure_1.png"
    return render_template("index.html", ImageLocation=ImageLocation)

@app.route("/alldata")
def deadEnd():
    # TODO: simple case query db for all data
    myQuery = Wind_speed.query.all()
    app.logger.warning(f'Wind speed from db: {myQuery}')
    # TODO: query db
    # range query from mm:ss to mm:sec
    # return range of speeds
    ImageLocation = "static/images/Figure_1.png"
    return render_template("alldata.html", ImageLocation=ImageLocation)

if __name__ == "__main__":
    app.run()
