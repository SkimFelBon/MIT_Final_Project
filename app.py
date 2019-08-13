# app.py
from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy
import datetime
from flask import flash, redirect
#================================
from io import BytesIO
from urllib.parse import quote
from base64 import b64encode

import random
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
#================================
from helpers import read_calendar, makePlot

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

    # DONE: Figure out how to use range between without session?
    # DONE: second problem how to query DateTimeObject?
    ## Using metod.query works like a charm!
    # qry = Wind_date.query.filter(Wind_date.Record_dt >= DateStart).all()
        ## Using db.session works too!
        # qry = db.session.query(Wind_date).filter(Wind_date.Record_dt >= DateStart).all()
            ## Using .between
            # qry = db.session.query(Wind_date).filter(Wind_date.Record_dt.between(DateStart, DateEnd))

    # DONE: return range of dates
    # qry = db.session.query(Wind_date).filter(Wind_date.Record_dt.between(datetime.datetime(2019,8,6,14), datetime.datetime(2019,8,6,15)))
    # for i in qry:
    #     app.logger.warning(f"Contents: {i.Record_dt}\n")

    ImageLocation = "static/images/Figure_1.png"
    return render_template("index.html", ImageLocation=ImageLocation)

@app.route("/alldata")
def alldata():
    # TODO: simple case query db for all data
    ImageLocation = "static/images/Figure_1.png"
    return render_template("alldata.html", ImageLocation=ImageLocation)


@app.route("/calendar", methods=["GET", "POST"])
def calendar():
    if request.method == "POST":
        dateRange = request.form.get('DateRange')
        timeFrom = request.form.get('From')
        timeTo = request.form.get('To')
        if not dateRange:
            dateRange = f"Please choose Date Range!"
            flash(dateRange, "alert-warning")
            return redirect("/calendar")
        if not timeFrom:
            timeFrom = '00:00'
        if not timeTo:
            timeTo = '00:00'
        # TODO: use parser.parse from dateutil in read_calendar
        startDate, endDate = read_calendar(dateRange, timeFrom, timeTo)
        # DONE: qry db using data from POST request
        qry = db.session.query(Wind_date).filter(Wind_date.record_dt.between(startDate, endDate)).all()
        if len(qry) is 0:
            msg = f"No records for this date range"
            flash(msg, "alert-warning")
            return redirect("/calendar")
        myTime = []
        mySpeed = []
        for i in qry:
            myTime.append(i.record_dt)
            mySpeed.append(i.windspeed_ref[0].speed)
        # DONE: build plot from queryData
        fig, ImageLocation = makePlot(myTime,mySpeed)
        png_output = BytesIO()
        FigureCanvas(fig).print_png(png_output)
        data = b64encode(png_output.getvalue()).decode('ascii')
        data_url = 'data:image/png;base64,{}'.format(quote(data))
        return render_template("calendar.html", img_data=data_url)

    return render_template("calendar.html")

#===========================
@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig
#===========================

if __name__ == "__main__":
    app.run()
