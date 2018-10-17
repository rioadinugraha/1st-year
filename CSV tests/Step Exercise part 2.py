import csv
import matplotlib.pyplot as plt
filename = "activity.csv"
import statistics as stat
with open(filename) as f:
    reader = csv.reader(f)

    header_row = next(reader)
    interval = []
    steps_Interval = []
    step_total = 0
    i = 0
    mean =[]

    dictInterval = {}
    for row in reader:
        if(row[0] != "NA"):
            dictInterval.setdefault(int(row[2]), [])
            dictInterval[int(row[2])].append(int(row[0]))
    for i in dictInterval.keys():
        mean.append(stat.mean(dictInterval.get(i)))
interval =list(dictInterval.keys())
maximum = max(mean)
for i in range (0,len(mean)+1):
    if maximum == mean[i-1]:
        index = i
intervalOfMax = index*5
print(intervalOfMax)
plt.scatter(interval,mean,cmap = plt.cm.Blues,edgecolors='none',s =100)
plt.show()



    # print(steps_Interval)
    # print(interval)
    # for row in reader:
    #     if current_date == datetime.strptime(row[1],"%Y-%m-%d"):
    #         try:
    #             stepNo= int(row[0])
    #         except ValueError:
    #             continue
    #         else:
    #             step_total += stepNo
    #     else:
    #         steps_Day.append(step_total)
    #         day.append(current_date)
    #         step_total= 0
    #         current_date = datetime.strptime(row[1],"%Y-%m-%d")
    #         try:
    #             stepNo = int(row[0])
    #         except ValueError:
    #             continue
    #         else:
    #             step_total += stepNo
