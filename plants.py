import arcade
from constantu import *


class Plants(arcade.Sprite):
    def __init__(self, image, HP, cost):
        super().__init__(image)
        self.HP = HP
        self.cost = cost
        self.row = 0
        self.column = 0

    def update(self):
        if self.HP <= 0:
            self.kill()

    def planting(self, center_x, center_y, row, column):
        self.set_position(center_x, center_y)
        self.row = row
        self.column = column


class SunFlower(Plants):
    def __init__(self):
        super().__init__("graphics/Plants/SunFlower/SunFlower_0.png", 10, 50)
