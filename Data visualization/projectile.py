from Angle import projectile
import math as m
import matplotlib.pyplot as plt
angle = int(input("input angle "))
gravity = 9.81
initialVelocity = int(input("put velocity"))

projectile = projectile(angle,initialVelocity)

time= 2*projectile.yvelocity/gravity
xcoordinate = []
ycoordinate = []
rounded = round(time)
for time in range (0,rounded +1):
    xresult = (time * projectile.xvelocity)
    yresult = (time * projectile.yvelocity - (gravity * (time**2)/2))
    if yresult <0:
        break
    xcoordinate.append(xresult)
    ycoordinate.append(yresult)
print(xcoordinate)
print(ycoordinate)

plt.plot(xcoordinate,ycoordinate,marker = '*')

plt.show()
