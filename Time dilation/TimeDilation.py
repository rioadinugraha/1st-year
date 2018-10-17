from timeDilCalc import timeDilation

timeLimit = 20
speed = int(input("input speed in m/s^2 "))

timeDilation = timeDilation(speed)


ratio = timeDilation.gettimeratio()
timedilated =[]
for i in range (0,timeLimit+1):
    timedilated.append(i*ratio)

print(timedilated)
