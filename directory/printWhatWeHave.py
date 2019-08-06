# printWhatWeHave.py
import sqlite3

conn = sqlite3.connect('wind_of_Change.db')
c = conn.cursor()
c.execute("SELECT * FROM wind_speed")
alltime = c.fetchall()
c.execute("SELECT * FROM winddate")
allspeed = c.fetchall()
conn.close()

for i in alltime:
    print(i)
for j in allspeed:
    print(j)
