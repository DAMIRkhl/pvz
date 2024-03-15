import arcade
from constantu import *


class Plants(arcade.Sprite):
    def __init__(self, image, HP, cost):
        super().__init__(image)
        self.HP = HP
        self.cost = cost
