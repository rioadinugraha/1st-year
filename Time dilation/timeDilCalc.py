import numpy
class timeDilation():

    def __init__(self,speed):
        SPEEDOFLIGHT = 299792458
        self.speedRelativeToLight = speed/SPEEDOFLIGHT
        self.TimeRatio = numpy.sqrt(1-self.speedRelativeToLight)
    def gettimeratio(self):
        return self.TimeRatio
