import arcade


class PlantsCards(arcade.Sprite):
    def __init__(self, x, image):
        super().__init__(image, scale=0.8)
        self.center_x = x
        self.center_y = 555.55


class Shop(arcade.Sprite):
    def __init__(self):
        super().__init__(
            "graphics/Screen/4B51B958-6D47-454C-A3A7-EBB961F31138.jpg", scale=0.5)
        self.center_x = 500
        self.center_y = 555.55


class Shoparrow(arcade.Sprite):
    def __init__(self):
        super().__init__("graphics/Items/1514151.webp", 0.15, angle=-90)
        self.center_x = 500
        self.center_y = 500


class Start(arcade.Sprite):
    def __init__(self):
        super().__init__("graphics/Screen/StartButton.png")
        self.center_x = 600
        self.center_y = 400
