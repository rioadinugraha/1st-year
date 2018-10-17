import csv
from datetime import datetime
import pygal
import math as m
filename = "activity.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    day = []
    steps_Day = []
    step_total = 0
    current_date = datetime.strptime("2012-10-01","%Y-%m-%d")
    for row in reader:
        if current_date == datetime.strptime(row[1],"%Y-%m-%d"):
            try:
                stepNo= int(row[0])
            except ValueError:
                continue
            else:
                step_total += stepNo
        else:
            steps_Day.append(step_total)
            day.append(current_date)
            step_total= 0
            current_date = datetime.strptime(row[1],"%Y-%m-%d")
            try:
                stepNo = int(row[0])
            except ValueError:
                continue
            else:
                step_total += stepNo

steps_Day.append(step_total)
day.append(current_date)


mean = m.fsum(steps_Day)/len(steps_Day)
sorted = sorted(steps_Day)
median = sorted[31]

hist = pygal.Bar()

hist.title = "steps per day"
hist.x_labels = day
hist.x_title ="Date"
hist.y_title ="frequency"
hist.add("day",steps_Day)
hist.render_to_file('steps per day visual.svg')
print(mean)
print(median)
