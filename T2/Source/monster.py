class Monster:
    energypoints = 100
    damage = 0
    id = -1
    coordinate_x = -1
    coordinate_y = -1

    def __init__(self, id, damage, x, y):
        self.damage = damage
        self.id = id
        self.x = x
        self.y = y