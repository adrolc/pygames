from collections import deque
import itertools
from .algorithm import AbstractAlgorithm, Node


class DFS(AbstractAlgorithm):
    def __init__(self, maze, maze_objects):
        super().__init__()
        # Maze environment
        self.maze = maze.maze
        self.fields_in_row = maze.fields_in_row
        self.fields_in_col = maze.fields_in_col
        self.maze_objects = maze_objects

        self.start = Node(
            (maze.INIT_PLAYER_POSITION[1], maze.INIT_PLAYER_POSITION[0]), None
        )
        self.stack = [self.start]
        self.visited = {self.start.coord}

    def _process_neighbor(self, current, neighbor_coord):
        field = self.maze[neighbor_coord[0]][neighbor_coord[1]]
        if field == self.maze_objects.TARGET:
            self.found = True
        elif field == self.maze_objects.PATH and neighbor_coord not in self.visited:
            self.stack.append(Node(neighbor_coord, current))
            self.visited.add(neighbor_coord)

    def search(self, speed=10):
        for i in itertools.count() if speed < 1 else range(speed):
            if self.found or not self.stack:
                break
            current = self.stack.pop()
            self.visited_fields.append(current)
            y, x = current.coord

            # up
            if y > 0:
                self._process_neighbor(current, (y - 1, x))

            # down
            if y < self.fields_in_col - 1:
                self._process_neighbor(current, (y + 1, x))

            # right
            if x < self.fields_in_row - 1:
                self._process_neighbor(current, (y, x + 1))

            # left
            if x > 0:
                self._process_neighbor(current, (y, x - 1))

    def build_found_path(self, speed=10):
        if self.found:
            for i in itertools.count() if speed < 1 else range(speed):
                if not self.found_path:
                    self.c = self.visited_fields[-1]
                    self.found_path.append(self.c)
                elif self.c.parent:
                    self.c = self.c.parent
                    self.found_path.append(self.c)
                else:
                    break
