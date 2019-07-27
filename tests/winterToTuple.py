# winterToTuple.py
import csv

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

def DataToCsv(row):
    date = str(row[0:10]) # date
    time = str(row[14:22]) # time
    dt = date + " " + time
    #speed = int(row[37:39])/10 # speed
    speed = str(row[38]) +','+ str(row[37])
    #print(time)
    #print(speed)
    file = open("mycsv.csv","a")
    writer = csv.writer(file,delimiter=';')
    writer.writerow((dt,speed))
    file.close()
    return True

#fileObj = open('winter.log','r')
#myFile = fileObj.read()
#fileObj.close()

#sample = "2019:02:26->> 14:15:05:    0:00:19   33   31   30   28   29   27"
sample1 = """2019:02:26->> 14:18:26:    0:03:40   12   13   15   22   19   17
             2019:02:26->> 14:18:36:    0:03:50   16   18   25   30   35   45
             2019:02:26->> 14:18:46:    0:04:00   46   43   40   44   51   49
             2019:02:26->> 14:18:56:    0:04:10   40   37   34   32   34   30
             2019:02:26->> 14:19:06:    0:04:20   26   26   23   19   23   27
             2019:02:26->> 14:19:16:    0:04:30   25   28   27   26   23   22
             2019:02:26->> 14:19:26:    0:04:40   21   21   21   20   16   14
          """

with open('winter.log','r') as f:
    for line in f:
        DataToCsv(line)
        

