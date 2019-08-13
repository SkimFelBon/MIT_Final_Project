# helpers.py
import datetime
def read_calendar(dateRange, timeFrom, timeTo):
    """
    This function parse string from POST request,
    and return DatetimeObject"""
    StartEndlist = dateRange.split(' to ')
    ## ['2019-08-06', '2019-08-14']
    StartListString = StartEndlist[0].split('-')
    EndListString = StartEndlist[1].split('-')
    ## ['2019', '08', '06']
    # TODO: make objects
    # datetime.datetime(2019,8,6), datetime.datetime(2019,8,6)
    Start = list(map(lambda i: int(i), StartListString))
    End = list(map(lambda j: int(j), EndListString))
    intTimeFrom = list(map(lambda k: int(k), timeFrom.split(':')))
    intTimeTo = list(map(lambda h: int(h), timeTo.split(':')))
    startDate = datetime.datetime(Start[0], Start[1], Start[2], intTimeFrom[0], intTimeFrom[1])
    endDate = datetime.datetime(End[0], End[1], End[2], intTimeTo[0], intTimeTo[1])
    return startDate, endDate


def makePlot(myTime,mySpeed):
    """ This function saves plot and return's file name"""
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.dates as mdates
    from dateutil import parser

    def my_plotter(ax, data1, data2, param_dict):
        """
        A helper function to make a graph

        Parameters
        ----------
        ax : Axes
            The axes to draw to

        data1 : array
           The x data

        data2 : array
           The y data

        param_dict : dict
           Dictionary of kwargs to pass to ax.plot

        Returns
        -------
        out : list
            list of artists added
        """
        out = ax.plot_date(data1, data2, **param_dict)
        return out
    years = mdates.YearLocator()   # every year
    # minutes = mdates.MinuteLocator() # every minute
    months = mdates.MonthLocator()  # every month
    # seconds = mdates.SecondLocator() # every second
    years_fmt = mdates.DateFormatter('%Y')
    # minutes_fmt = mdates.DateFormatter('%M:%S')


    # which you would then use as:
    # data1, data2, data3, data4 = np.random.randn(4, 100)
    fig, ax = plt.subplots(1, 1)

    # format the ticks
    # ax.xaxis.set_major_locator(minutes)
    # ax.xaxis.set_major_formatter(minutes_fmt)
    # ax.xaxis.set_minor_locator(seconds)

    my_plotter(ax, myTime, mySpeed, {'marker': 'o'})
    plt.title('Wind Speed vs Time')
    plt.ylabel('Wind Speed, m/s')
    plt.xlabel('time')
    filelocation = "static/images/myfile2.png"
    # plt.savefig(filelocation)
    return fig, filelocation


"""
@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    return fig
"""
