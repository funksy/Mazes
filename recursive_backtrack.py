import random
from maze import Maze, Cell

#define starting point
def starting_cell(maze):
    #choose random starting position
    start_y = int(random.random() * len(maze.grid))
    start_x = int(random.random() * len(maze.grid[0]))

    #convert starting position to a path
    maze.grid[start_y][start_x].state = 'path'
    maze.grid[start_y][start_x].visited = True

    return maze


def cell_is_valid(maze, direction):
    if direction == 'u':
        pass
    if direction == 'd':
        pass
    if direction == 'l':
        pass
    if direction == 'r':
        pass
    return False


def carve_passage_from(maze, cell):
    directions = random.shuffle(['u','r', 'd', 'l'])
    for direction in directions:
        if cell_is_valid(maze, direction):


def create_maze(maze):
    pass
