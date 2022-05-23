import pygame

from settings import Settings
from event import Event
from player.ship import Ship
from enemy.dragon import Dragons

from background import Background
from menu import Menu

from scene import Scene
from game.gold import Golds
from game.game_stats import GameStats
from game.scoreboard import Scoreboard
from game.level import Level
from game.drop import Drop
from game.game_over import GameOver


class DragonInvaders:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Dragon Invaders")

        self.event = Event(self)
        self.background = Background(self)
        self.scene = Scene()
        self.menu = Menu(self)
        self.level = Level(self)
        self.ship = Ship(self)
        self.dragons = Dragons(self)
        self.golds = Golds(self)
        self.drop = Drop(self)
        self.game_stats = GameStats(self)
        self.scoreboard = Scoreboard(self)
        self.gameover = GameOver(self)

        # self.clock = pygame.time.Clock()

    def run_game(self):
        while True:
            self._check_events()
            self._update()
            self._draw()
            pygame.display.flip()
            # self.clock.tick(200)

    def _check_events(self):
        for event in pygame.event.get():
            self.event.check_event(event)

    def _update(self):
        if self.scene.scene['game']:
            self.ship.update()
            self.dragons.update()
            self.golds.update()
            self.drop.update()
            self._check_collisions()

    def _draw(self):
        self.background.draw()

        if self.scene.scene['menu']:
            self.menu.draw()

        elif self.scene.scene['game']:
            self.ship.draw()
            self.dragons.draw()
            self.golds.draw()
            self.drop.draw()
            self.scoreboard.draw()
            self.scoreboard.draw_levelup()
            self.gameover.draw()

    def _check_collisions(self):
        self._check_ship_dragon_collision()
        self._check_dragons_bullets_collision()
        self._check_dragons_bottom_collision()
        self._check_ship_gold_collision()
        self._check_ship_item_collision()

    def _check_ship_dragon_collision(self):
        if pygame.sprite.spritecollideany(self.ship, self.dragons.dragons):
            self._ship_hit()

    def _ship_hit(self):
        self.ship.lifes.decrease()
        self.dragons.dragons.empty()
        if self.ship.lifes.dead():
            self.gameover.show_gameover()
            self.drop.dropped_items.empty()


    def _check_dragons_bullets_collision(self):
        collisions = pygame.sprite.groupcollide(self.dragons.dragons, self.ship.bullets, True, True)
        for dragon in collisions.keys():
            self.dragons.dragons_left -= 1 # Reduce the number of dragons
            self.dragons.explode_animation.explode(dragon.rect) # dragon explode animation
            self.golds.drop_gold(dragon.rect) # Drop gold
        if self.dragons.dragons_left <= 0: # level up
            self.level.levelup()
            self.dragons.dragons_left = self.level.dragons_number
            self.game_stats.level += 1
            self.scoreboard.render_level()
            self.dragons.dragons.empty() # Remove all dragons from the group
            # show_levelup method will run an event after 3 sec
            # that will re-enable dragon spawn at increased speed
            self.dragons.stop_auto_spawn()
            self.scoreboard.show_levelup()
        self.scoreboard.render_dragons_left() # render the new value on the scoreboard


    def _check_dragons_bottom_collision(self):
        screen_rect = self.screen.get_rect()
        for dragon in self.dragons.dragons.sprites():
            if dragon.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_ship_gold_collision(self):
        gold = pygame.sprite.spritecollideany(self.ship, self.golds.golds)
        if gold:
            self._pickup_gold()
            self.golds.golds.remove(gold)

    def _check_ship_item_collision(self):
        item = pygame.sprite.spritecollideany(self.ship, self.drop.dropped_items)
        if item:
            item.pickup()
            self.drop.dropped_items.remove(item)


    def _pickup_gold(self):
        self.game_stats.gold += 1
        self.scoreboard.render_gold()


if __name__ == '__main__':
    game = DragonInvaders()
    game.run_game()
