import pygame
import random

from utilities.asset_path import AssetPath

class Drop():
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.game = game

        # name, icon, icon_size
        # the name must match the name of the function that is called on this item
        self.items = [
            ['bullet_0', AssetPath.boxes[0], (40, 43)],
            ['bullet_1', AssetPath.boxes[0], (40, 43)],
            ['bullet_2', AssetPath.boxes[0], (40, 43)],
            ['bullet_3', AssetPath.boxes[0], (40, 43)],
            ['heart', AssetPath.heart, (35, 35)],
        ]

        self.dropped_items = pygame.sprite.Group()

        self.DROP_ITEM = pygame.USEREVENT + 4
        self.start_auto_drop()

    def start_auto_drop(self):
        pygame.time.set_timer(self.DROP_ITEM, self.settings.item_drop_lottery_speed)

    def stop_auto_drop(self):
        pygame.time.set_timer(self.DROP_ITEM, 0)

    def _drop_item(self):
        item = random.choice(self.items)
        item = Item(self.game, item[0], item[1], item[2])
        self.dropped_items.add(item)

    def try_drop(self):
        num = random.randint(0, 100)
        if num <= self.settings.item_drop_luck:
            self._drop_item()


    def update(self):
        self.dropped_items.update()

        # remove item from group if its position moves beyond the bottom of the screen
        for item in self.dropped_items.copy():
            if item.rect.top >= self.settings.screen_height:
                self.dropped_items.remove(item)

    def draw(self):
        self.dropped_items.draw(self.screen)

class Item(pygame.sprite.Sprite):
    def __init__(self, game, name, image, size):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.name = name
        self.game = game

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, self.settings.screen_width - size[0])
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.item_drop_speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def pickup(self):
        globals()[self.name](self.game)


def bullet_0(game):
    game.settings.bullet_type = 0

def bullet_1(game):
    game.settings.bullet_type = 1

def bullet_2(game):
    game.settings.bullet_type = 2

def bullet_3(game):
    game.settings.bullet_type = 3

def heart(game):
    game.ship.lifes.increase()






