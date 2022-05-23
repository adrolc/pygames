class GameStats:
    def __init__(self, game):
        self.ship = game.ship

        self.reset()

    def reset(self):
        self.ship.lifes.start()
        self.level = 1
        self.gold = 0
