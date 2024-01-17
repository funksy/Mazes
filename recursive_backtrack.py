import random

#define starting point
def starting_cell(maze):
    #choose random starting position
    start_y = int(random.random() * len(maze.grid))
    start_x = int(random.random() * len(maze.grid[0]))

    #convert starting position to a path
    maze.grid[start_y][start_x].state = 'path'
    maze.grid[start_y][start_x].visited = True

    return maze


def choose_rand_cell(maze):
    #choose random starting position
    start_y = int(random.random() * len(maze.grid))
    start_x = int(random.random() * len(maze.grid[0]))
    maze.grid[start_y][start_x] = 'path'


def choose_rand_direction(maze, current_position):
    #take maze and current position as inputs
    #choose a random direction and verify the cell in that direction is valid
    #return that random cell
