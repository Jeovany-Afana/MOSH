import random


class Dice:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tuple = (self.x, self.y)

    def roll(self):
        self.x = random.randint(0, 20)
        self.y = random.randint(0, 20)
        self.tuple = self.x, self.y
        return self.tuple


dice1 = Dice()
print(dice1.roll())
