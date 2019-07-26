## DataTocsv.py
import csv
import re
##def WinterToTuple(sample):
##    # Desired result
##    ListofTuples = [('14:15:05','33'),
##                    ('14:15:07','31'),
##                    ('14:15:09','30'),
##                    ('14:15:11','28'),
##                    ('14:15:13','29'),
##                    ('14:15:15','27')]
##    return ListofTuples
##WinterToTuple()
"""
TODO
regex through row
find what date/time separated
and find list of tuples for speed-values
for every speed-value in a row
    increase time by 1.67
    round time
    write time to csv file
"""

sample1 = """2019:02:26->> 14:18:26:    0:03:40   12   13   15   22   19   17
             2019:02:26->> 14:18:36:    0:03:50   16   18   25   30   35   45
             2019:02:26->> 14:18:46:    0:04:00   46   43   40   44   51   49
             2019:02:26->> 14:18:56:    0:04:10   40   37   34   32   34   30
             2019:02:26->> 14:19:06:    0:04:20   26   26   23   19   23   27
             2019:02:26->> 14:19:16:    0:04:30   25   28   27   26   23   22
             2019:02:26->> 14:19:26:    0:04:40   21   21   21   20   16   14
          """
#
DateTimeRegex = re.compile('''(\d{4})\:(\d\d)\:(\d\d)\D*        # date
                        (\d\d)\:(\d\d)\:(\d\d)                  # time
                        ''',re.VERBOSE)
#
SpeedRegex = re.compile('''\s+(\d\d)\s+(\d\d)\s+(\d\d)\s+(\d\d)\s+(\d\d)\s+(\d\d)
                        ''',re.VERBOSE)
sample = "2019:02:26->> 14:18:26:    0:03:40   12   13   15   22   19   17"
#sample = "2019:02:26->> 14:15:05:    0:00:19   33   31   30   28   29   27"
SpeedList = []
DateTimeResult = DateTimeRegex.findall(sample)

hours = int(DateTimeResult[0][3])
mins = int(DateTimeResult[0][4])
sec = int(DateTimeResult[0][5])

print(DateTimeResult)
#print(SpeedResult)
for groups in SpeedRegex.findall(sample):
    for i in range(len(groups)):
        SpeedList.append(groups[i])
print(SpeedList)

for sens in range(len(SpeedList)):
    sec += 1.67
    SpeedList[sens]
    print(str(round(sec)) +","+ str(SpeedList[sens]))
    file = open("mycsv.csv","a")
    writer = csv.writer(file)
    writer.writerow((dt,speed))
    file.close()










