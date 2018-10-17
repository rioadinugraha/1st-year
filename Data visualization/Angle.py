import math as m

class projectile():

    def __init__(self,angle,velocity):
        self.angle =  m.radians(angle)
        self.initVelocity = velocity
        self.yvelocity = self.initVelocity*m.sin(self.angle)
        self.xvelocity = self.initVelocity*m.cos(self.angle)

