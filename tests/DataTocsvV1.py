## DataTocsv.py
import csv
import re
#
DateTimeRegex = re.compile('''(\d{4})\:(\d\d)\:(\d\d)\D*        # date
                        (\d\d)\:(\d\d)\:(\d\d)                  # time
                        ''',re.VERBOSE)
#
SpeedRegex = re.compile('''\s+(\d\d)\s+(\d\d)\s+(\d\d)\s+(\d\d)\s+(\d\d)\s+(\d\d)\n?
                        ''',re.VERBOSE)

def DataTocsv(sample):
    SpeedList = []
    DateTimeResult = DateTimeRegex.findall(sample)
    hours = int(DateTimeResult[0][3])
    mins = int(DateTimeResult[0][4])
    sec = int(DateTimeResult[0][5])
    for groups in SpeedRegex.findall(sample):
        for i in range(len(groups)):
            SpeedList.append(groups[i])
    file = open("Results.csv","a")
    for sens in range(len(SpeedList)):
        dt = str(DateTimeResult[0][2])+"."+str(DateTimeResult[0][1])+"."+str(DateTimeResult[0][0])+" "+str(hours)+":"+str(mins)+":"+str(round(sec))
        speed = int(SpeedList[sens])
        writer = csv.writer(file)
        writer.writerow((dt,speed))
        sec += 1.67
        if sec >= 60:
            sec %= 60
            mins += 1
            if mins >= 60:
                mins %= 60
                hours += 1
                if hours >= 24:
                    hours %= 24
    file.close()
    return False

with open('winterTest.log','r') as f:
    for line in f:
        DataTocsv(line)
