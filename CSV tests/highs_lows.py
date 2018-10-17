import csv
from datetime import datetime
import matplotlib.ticker as ticker

import matplotlib.pyplot as plt

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    lows = []
    dates = []
    highs = []
    for row in reader:
        current_date = datetime.strptime(row[0],"%Y-%m-%d")
        # current_date = datetime.strftime(current_date,"%Y-%m-%d")
        try:
            low= int(row[3])
            high = int(row[1])
        except ValueError:
            print(current_date,'no data')
        else:
            dates.append(current_date)
            lows.append(low)
            highs.append(high)
#plot data
fig = plt.figure(dpi=128,figsize =(10,6))
plt.plot(dates,highs,c='red',alpha =0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)


#format plot
title = "daily high and low temperature - 2014\nDeathValley,CA"
plt.title(title,fontsize=20)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)',fontsize =16)
plt.tick_params(axis='both',which ='major',labelsize=16)

plt.show()
