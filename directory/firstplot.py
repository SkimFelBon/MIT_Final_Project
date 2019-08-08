# firstplot.py
import sqlite3
import pylab as plt
import matplotlib
from dateutil import parser
conn = sqlite3.connect('wind_of_change.db')
c = conn.cursor()
c.execute("SELECT * FROM wind_speed")
allspeed = c.fetchall()
c.execute("SELECT * FROM winddate")
alltime = c.fetchall()
conn.close()
print(f"alltime type is {type(alltime)}")
print(f"allspeed type is {type(allspeed)}")
myTime = []
mySpeed = []

for i in allspeed:
    mySpeed.append(i[1])

for j in alltime:
    myTime.append(parser.parse(j[1]))
print(myTime[:5])
plt.figure('wind')
plt.title('Wind of Change')
plt.xlabel('time, sec')
plt.ylabel('Wind Speed, m/s')
plt.plot(myTime,mySpeed)
# Specify a rotation for the tick labels in degrees or with keywords.
plt.xticks(rotation=45, horizontalalignment="right")
# Pad margins so that markers don't get clipped by the axes
#plt.margins(0.5)
# Tweak spacing to prevent clipping of tick-labels
plt.subplots_adjust(bottom=0.19)
plt.show()
