from random import randint

class Die():

    def __init__(self,num_Sides=6):
        self.num_sides = num_Sides

    def roll(self):
        return randint(1,self.num_sides)

