import arcade
from constantu import *
from Elements import *
from plants import *


class FirstGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.BG = arcade.load_texture(
            "graphics/Items/Background/Background_0.jpg")
        self.main_menu = True
        self.ma1n_menu = arcade.load_texture("graphics/Screen/MainMenu.png")
        self.start_button = Start()
        self.shop = True
        self.shoparrow = Shoparrow()
        self.houchodamou = Shop()
        self.plants = arcade.SpriteList()
        self.plantscardspeashooter = PlantsCards(340, "graphics/Cards/card_peashooter.png")

        self.plantscardssunflower = PlantsCards(395, "graphics/Cards/card_sunflower.png")

        self.plantscardwallnut = PlantsCards(450, "graphics/Cards/card_wallnut.png")

        self.plantscardpotatomine = PlantsCards(505, "graphics/Cards/card_potatomine.png")

        self.plantscardsnowpea = PlantsCards(560, "graphics/Cards/card_snowpea.png")

        self.plantscardiceshroom = PlantsCards(615, "graphics/Cards/card_iceshroom.png")

        self.plantscardjalapeno = PlantsCards(670, "graphics/Cards/card_jalapeno.png")

        self.plantscardcherrybomb = PlantsCards(725, "graphics/Cards/card_cherrybomb.png")

        self.showel = PlantsCards(795, "graphics/Cards/Shovel.webp")

        self.hold = None

    def spawn(self):
        pass

    def on_draw(self):
        self.clear()
        if self.main_menu:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.ma1n_menu)
            self.start_button.draw()
        if not self.main_menu:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.BG)
            self.shoparrow.draw()
            self.houchodamou.draw()
            self.plantscardspeashooter.draw()
            self.plantscardssunflower.draw()
            self.plantscardwallnut.draw()
            self.plantscardpotatomine.draw()
            self.plantscardsnowpea.draw()
            self.plantscardiceshroom.draw()
            self.plantscardjalapeno.draw()
            self.plantscardcherrybomb.draw()
            self.showel.draw()
            self.plants.draw()
            if self.hold is not None:
                self.hold.draw()

    def shop_and_not_shop(self):
        if self.shop:
            self.houchodamou.center_y = 555.55
            self.shoparrow.center_y = 500
            self.shoparrow.angle = -90
            self.plantscardspeashooter.center_y = 555.55
            self.plantscardssunflower.center_y = 555.55
            self.plantscardwallnut.center_y = 555.55
            self.plantscardpotatomine.center_y = 555.55
            self.plantscardsnowpea.center_y = 555.55
            self.plantscardiceshroom.center_y = 555.55
            self.plantscardjalapeno.center_y = 555.55
            self.plantscardcherrybomb.center_y = 555.55
            self.showel.center_y = 555.55
        elif not self.shop:
            self.houchodamou.center_y = 1000
            self.shoparrow.center_y = 585
            self.shoparrow.angle = 90
            self.plantscardspeashooter.center_y = 1000000
            self.plantscardssunflower.center_y = 8685749534
            self.plantscardwallnut.center_y = 474743829
            self.plantscardpotatomine.center_y = 86945892
            self.plantscardsnowpea.center_y = 528859
            self.plantscardiceshroom.center_y = 423729
            self.plantscardjalapeno.center_y = 182837
            self.plantscardcherrybomb.center_y = 583478
            self.showel.center_y = 48902375

    def update(self, delta_time: float):
        pass

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if (self.start_button.left <= x <= self.start_button.right) and (
                self.start_button.bottom <= y <= self.start_button.top):
            self.main_menu = False

        if (self.shoparrow.left <= x <= self.shoparrow.right) and (self.shoparrow.bottom <= y <= self.shoparrow.top) \
                and not self.main_menu:
            self.shop = not self.shop
            self.shop_and_not_shop()
        if (self.plantscardspeashooter.left <= x <= self.plantscardspeashooter.right) and (
                self.plantscardspeashooter.bottom <= y <= self.plantscardspeashooter.top):
            print("peashooter")
        if (self.plantscardssunflower.left <= x <= self.plantscardssunflower.right) and (
                self.plantscardssunflower.bottom <= y <= self.plantscardssunflower.top):
            self.hold = SunFlower()
            self.hold.center_x = x
            self.hold.center_y = y

    def cards_size(self, name, x, y, normalscale, pressscale):
        if (name.left <= x <= name.right) and (
                name.bottom <= y <= name.top) \
                and not self.main_menu:
            name.scale = pressscale
        else:
            name.scale = normalscale

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.cards_size(self.plantscardspeashooter, x, y, 0.8, 0.7)
        self.cards_size(self.plantscardcherrybomb, x, y, 0.8, 0.7)
        self.cards_size(self.plantscardjalapeno, x, y, 0.8, 0.7)
        self.cards_size(self.plantscardsnowpea, x, y, 0.8, 0.7)
        self.cards_size(self.plantscardiceshroom, x, y, 0.8, 0.7)
        self.cards_size(self.plantscardpotatomine, x, y, 0.8, 0.7)
        self.cards_size(self.plantscardwallnut, x, y, 0.8, 0.7)
        self.cards_size(self.plantscardssunflower, x, y, 0.8, 0.7)
        self.cards_size(self.showel, x, y, 0.5, 0.4)

        if self.hold is not None:
            self.hold.center_x = x
            self.hold.center_y = y


window = FirstGame(SCREEN_WIDTH, SCREEN_HEIGHT)
window.spawn()

arcade.run()

"""

"""
