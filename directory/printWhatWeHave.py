# printWhatWeHave.py
import sqlite3

conn = sqlite3.connect('newDataBase.db')
c = conn.cursor()
c.execute("SELECT * FROM wind_speed")
allspeed = c.fetchall()
c.execute("SELECT * FROM wind_date")
alltime = c.fetchall()
conn.close()

# for i in alltime:
#     print(i)
# for j in allspeed:
#     print(j)
