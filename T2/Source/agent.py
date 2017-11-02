import random

class Agent:
    energypoints = 100
    arrows = 5
    position = (0,0)
    facing = (0,1)

    def __init__(self, position, facing):
        self.position = position
        self.facing = facing

    def shoot(self):
        self.arrows = self.arrows - 1
        return random.randint(20, 50)