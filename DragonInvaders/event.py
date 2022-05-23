import pygame
import sys

class Event:
    def __init__(self, game):
        self.game = game

    def check_event(self, event):
        # Exit game
        if event.type == pygame.QUIT:
            sys.exit()
        # KEYDOWN Event
        elif event.type == pygame.KEYDOWN:
            self._check_keydown(event)
        # KEYUP Event
        elif event.type == pygame.KEYUP:
            self._check_keyup(event)
        # Dragon animation
        elif event.type == self.game.dragons.DRAGON_MOVEMENT and self.game.scene.scene['game']:
            self.game.dragons.animation()
        # Dragon spawn
        elif event.type == self.game.dragons.SPAWN_DRAGON and self.game.scene.scene['game']:
            self.game.dragons.spawn_dragon()
        # Gold animation
        elif event.type == self.game.golds.GOLD_ROTATE_ANIMATION:
            self.game.golds.animate()
        # Show and hide the level after leveling up
        elif event.type == self.game.scoreboard.HIDE_LEVELUP:
            self.game.scoreboard.hide_levelup()
            self.game.dragons.start_auto_spawn() # Turn ON the spawn of dragons
        # Show and hide 'game over' after losing
        elif event.type == self.game.gameover.HIDE_GAMEOVER:
            self.game.scene.activate_scene('menu')
            self.game.gameover.reset_game()
        # Drop item
        elif event.type == self.game.drop.DROP_ITEM and self.game.scene.scene['game']:
            self.game.drop.try_drop()
        # Active shooting
        # space keydown - activate
        # space keyup - deactivate
        elif event.type == self.game.ship.FIRE:
            self.game.ship.fire_bullet()

    def _check_keydown(self, event):
        # Activate ship movement to the right
        if event.key == pygame.K_RIGHT and self.game.scene.scene['game']:
            self.game.ship.moving_right = True
        # Activate ship movement to the left
        elif event.key == pygame.K_LEFT and self.game.scene.scene['game']:
            self.game.ship.moving_left = True
        # Fire the bullet and activate automatic fire
        elif event.key == pygame.K_SPACE and self.game.scene.scene['game']:
            self.game.ship.fire_bullet()
            self.game.ship.fire_on()
        # Next menu option
        elif event.key == pygame.K_DOWN and self.game.scene.scene['menu']:
            self.game.menu.next_option()
        # Previous menu option
        elif event.key == pygame.K_UP and self.game.scene.scene['menu']:
            self.game.menu.previous_option()
        # Run active option in menu
        elif event.key == pygame.K_RETURN and self.game.scene.scene['menu']:
            self.game.menu.run_active_option()
        # Switch scene [menu / game]. It also serves as a pause
        elif event.key == pygame.K_ESCAPE:
            if self.game.scene.scene['game']:
                self.game.scene.activate_scene('menu')
            elif self.game.scene.scene['menu']:
                self.game.scene.activate_scene('game')

    def _check_keyup(self, event):
        # Deactivate ship movement to the right
        if event.key == pygame.K_RIGHT and self.game.scene.scene['game']:
            self.game.ship.moving_right = False
        # Deactivate ship movement to the left
        elif event.key == pygame.K_LEFT and self.game.scene.scene['game']:
            self.game.ship.moving_left = False
        # Deactivate automatic fire
        elif event.key == pygame.K_SPACE and self.game.scene.scene['game']:
            self.game.ship.fire_off()

