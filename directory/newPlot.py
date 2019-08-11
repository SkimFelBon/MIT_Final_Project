# sphinx_gallery_thumbnail_number = 3
import sqlite3
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
    out = ax.plot(data1, data2, **param_dict)
    return out

# contact db
conn = sqlite3.connect('wind_of_change.db')
c = conn.cursor()
c.execute("SELECT * FROM wind_speed")
allspeed = c.fetchall()
c.execute("SELECT * FROM winddate")
alltime = c.fetchall()
conn.close()
myTime = []
mySpeed = []
# parse result from db
for i in allspeed:
    mySpeed.append(i[1])

for j in alltime:
    myTime.append(parser.parse(j[1]))

#years = mdates.YearLocator()   # every year
minutes = mdates.MinuteLocator() # every minute
#months = mdates.MonthLocator()  # every month
seconds = mdates.SecondLocator() # every second
#years_fmt = mdates.DateFormatter('%Y')
minutes_fmt = mdates.DateFormatter('%M:%S')


# which you would then use as:
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)

# format the ticks
ax.xaxis.set_major_locator(minutes)
ax.xaxis.set_major_formatter(minutes_fmt)
ax.xaxis.set_minor_locator(seconds)

my_plotter(ax, myTime, mySpeed, {'marker': 'x'})
plt.title('Wind of Change')
plt.ylabel('Wind Speed, m/s')
plt.xlabel('time, min:sec')
plt.show()
# plt.savefig('myfile1.png')
# plt.savefig('myfile.png',dpi=(500), bbox_inches='tight')
