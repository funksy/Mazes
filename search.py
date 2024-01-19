import pygame
from maze import Maze, Cell

class Search:
    def __init__(self, maze):
        self.start = []
        self.finish = []
        self.frontier = []
        self.explored = {}
        self.current = []
        self.started = False
        self.finished = False
        self.backtrack = {}
        self.solution = []


    def initialize(self, maze):
        self.start = [maze.start[0], maze.start[1]]
        self.current = [maze.start[0], maze.start[1]]
        self.frontier = [[maze.start[0], maze.start[1]]]
        self.finish = [maze.finish[0], maze.finish[1]]
        for i in range(len(maze.grid)):
            for j in range(len(maze.grid[0])):
                self.explored[(maze.grid[i][j].x, maze.grid[i][j].y)] = False


    def draw(self, maze, surface):
        cell_x, cell_y = (surface.get_width() / len(maze.grid[0])), (surface.get_height() / len(maze.grid))
        for i in range(len(maze.grid)):
            for j in range(len(maze.grid[0])):
                x, y = i * cell_x, j * cell_y
                current_cell = maze.grid[i][j]
                if current_cell.state == 'start' or current_cell.state == 'finish':
                    continue
                if self.explored.get((i, j)) == True:
                    pygame.draw.rect(surface, pygame.Color(51, 51, 255), (x, y, cell_x, cell_y))
                if [i, j] in self.solution:
                    pygame.draw.rect(surface, pygame.Color(255, 255, 0), (x, y, cell_x, cell_y))
                if [current_cell.x, current_cell.y] == self.current:
                    pygame.draw.rect(surface, pygame.Color(255, 255, 0), (x, y, cell_x, cell_y))

                if current_cell.walls["top"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x, y), (x + cell_x, y), 2)
                if current_cell.walls["left"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x, y), (x, y + cell_y), 2)
                if current_cell.walls["bottom"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x, y + cell_y), (x + cell_x, y + cell_y), 2)
                if current_cell.walls["right"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x + cell_x, y), (x + cell_x, y + cell_y), 2)
