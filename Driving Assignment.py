import matplotlib.pyplot as plt



def speed(v0, acc, t): # speed formula
    return acc *t + v0


def dist(v0, acc, t):   # Distance formula
    return v0 * t + t**2 * acc /2


while True:
    try:
        Time = int(input("seconds:"))
        Acc = int(input("Acceleration:"))
        Distance = int(input("Distance:"))
        break
    except ValueError:
        print("non-integer detected please re-input values")


starNumber = 0
limit = 60
v0= 0
ActualTime= 0
maxspeed = speed(v0,Acc,Time) #maximum speed
maxdistance = dist(v0,Acc,Time) #total distance travelled
Data = []
while ActualTime <Time +1:
    starNumber = dist(v0, Acc, ActualTime)/10
    starNumber = int(starNumber)
    Data.append(dist(v0, Acc, ActualTime))
    print("duration:" + str(ActualTime) + "+" + "Distance:" + (starNumber * "*"))
    ActualTime = ActualTime + 1

print(Data)
plt.plot(Data)
plt.show()

if limit < maxspeed:
    print("Person went over speed limit. (max speed was " + str(maxspeed) + "m/s)")
else:
    print("Person did not go over speed limit. (max speed was " + str(maxspeed) + "m/s)")

if Distance < maxdistance:
    print("The person reached the destination " + str(maxdistance) + "m)")
else:
    print("The person did not reach the destination. (reached " + str(maxspeed) + "m)")
