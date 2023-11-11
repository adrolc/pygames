import pygame
import sys
from .config import load_config
from .maze_generator import generate_maze


class MazeObject:
    PATH = 0
    WALL = 1
    PLAYER = 2
    TARGET = 3

    class Player(pygame.sprite.Sprite):
        def __init__(self, x: int, y: int, field_size: int):
            super().__init__()
            self.field_size = field_size
            self.image = self.create_image()
            self.rect = self.image.get_rect()
            self.set_position(x, y)

        def create_image(self):
            image = pygame.Surface((self.field_size, self.field_size))
            image.fill((255, 0, 0))
            return image

        def set_position(self, x: int, y: int):
            self.rect.x = x * self.field_size
            self.rect.y = y * self.field_size

    class Target(pygame.sprite.Sprite):
        def __init__(self, x: int, y: int, field_size: int):
            super().__init__()
            self.field_size = field_size
            self.image = self.create_image()
            self.rect = self.image.get_rect()
            self.set_position(x, y)

        def create_image(self):
            image = pygame.Surface((self.field_size, self.field_size))
            image.fill((0, 255, 0))
            return image

        def set_position(self, x: int, y: int):
            self.rect.x = x * self.field_size
            self.rect.y = y * self.field_size

    class Wall(pygame.sprite.Sprite):
        def __init__(self, x: int, y: int, field_size: int):
            super().__init__()
            self.field_size = field_size
            self.image = self.create_image()
            self.rect = self.image.get_rect()
            self.set_position(x, y)

        def create_image(self):
            image = pygame.Surface((self.field_size, self.field_size))
            image.fill((0, 0, 0))
            return image

        def set_position(self, x: int, y: int):
            self.rect.x = x * self.field_size
            self.rect.y = y * self.field_size


class Maze:
    def __init__(self, algorithm):
        pygame.init()
        self.config = load_config()
        self.field_size = self.config["field_size"]
        self.fields_in_row = self.config["fields_in_row"]
        self.fields_in_col = self.config["fields_in_col"]
        self.screen_width = self.field_size * self.fields_in_col
        self.screen_height = self.field_size * self.fields_in_row

        self.INIT_PLAYER_POSITION = (1, 1)
        self.INIT_TARGET_POSITION = (self.fields_in_col - 2, self.fields_in_row - 2)

        self.setup_display()
        self.init_maze()
        self.init_maze_objects()

        self.algorithm = algorithm(self, MazeObject)

    def setup_display(self):
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Maze")
        self.clock = pygame.time.Clock()

    def init_maze(self):
        self.maze = generate_maze(self.fields_in_row, self.fields_in_col)
        x, y = self.INIT_PLAYER_POSITION
        self.maze[x][y] = MazeObject.PLAYER
        x, y = self.INIT_TARGET_POSITION
        self.maze[x][y] = MazeObject.TARGET

    def init_maze_objects(self):
        self.walls = pygame.sprite.Group()
        for row in range(self.fields_in_row):
            for col in range(self.fields_in_col):
                field = self.maze[col][row]
                if field == MazeObject.WALL:
                    self.walls.add(MazeObject.Wall(col, row, self.field_size))
                elif field == MazeObject.PLAYER:
                    self.player = MazeObject.Player(col, row, self.field_size)
                elif field == MazeObject.TARGET:
                    self.target = MazeObject.Target(col, row, self.field_size)

    def update(self):
        self.algorithm.search(self.config["draw_visited_fields_speed"])
        self.algorithm.build_found_path(self.config["draw_found_path_speed"])

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw_screen()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw_grid(self):
        for x in range(0, self.screen_width, self.field_size):
            pygame.draw.line(
                self.screen, (200, 200, 200), (x, 0), (x, self.screen_height)
            )
        for y in range(0, self.screen_height, self.field_size):
            pygame.draw.line(
                self.screen, (200, 200, 200), (0, y), (self.screen_width, y)
            )

    def draw_visited_fields(self):
        for field in self.algorithm.visited_fields:
            x, y = field.coord
            pygame.draw.rect(
                self.screen,
                (255, 159, 67),
                (
                    x * self.field_size,
                    y * self.field_size,
                    self.field_size,
                    self.field_size,
                ),
            )

    def draw_found_path(self):
        for field in self.algorithm.found_path:
            x, y = field.coord
            pygame.draw.rect(
                self.screen,
                (46, 134, 222),
                (
                    x * self.field_size,
                    y * self.field_size,
                    self.field_size,
                    self.field_size,
                ),
            )

    def draw_screen(self):
        self.screen.fill((255, 255, 255))
        self.draw_visited_fields()
        self.draw_found_path()
        # self.draw_grid()
        self.screen.blit(self.player.image, self.player.rect)
        self.walls.draw(self.screen)
        self.screen.blit(self.target.image, self.target.rect)
        pygame.display.flip()
        self.clock.tick(120)
