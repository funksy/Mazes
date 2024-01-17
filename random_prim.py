import random
from maze import Maze, Cell


#identify starting cell and walls
def starting_cell(maze):
    #choose random starting position
    start_x = int(random.random() * len(maze.grid))
    start_y = int(random.random() * len(maze.grid[0]))

    #convert starting position to a path and add frontier cells
    maze = mark_as_path(maze, start_x, start_y)

    return maze


#mark given cell as a path and add appropriate frontier cells
def mark_as_path(maze, cell_x, cell_y):
    maze.grid[cell_x][cell_y].state = 'path'
    if cell_x > 0:
        if maze.grid[cell_x - 1][cell_y].state == 'unvisited':
            add_to_frontier(maze, [cell_x - 1, cell_y])
    if cell_x < len(maze.grid) - 1:
        if maze.grid[cell_x + 1][cell_y].state == 'unvisited':
            add_to_frontier(maze, [cell_x + 1, cell_y])
    if cell_y > 0:
        if maze.grid[cell_x][cell_y - 1].state == 'unvisited':
            add_to_frontier(maze, [cell_x, cell_y - 1])
    if cell_y < len(maze.grid[0]) - 1:
        if maze.grid[cell_x][cell_y + 1].state == 'unvisited':
            add_to_frontier(maze, [cell_x, cell_y + 1])
    return maze


#checks if cell is already in frontier, then adds
def add_to_frontier(maze, frontier_cell):
    if frontier_cell not in maze.frontier:
        maze.frontier.append(frontier_cell)


#choose a random element from the frontier list and return it
def choose_rand_frontier(maze):
    return maze.frontier[int(random.random() * len(maze.frontier)) - 1]


#choose a random adjacent cell, given the random frontier cell
def choose_rand_neighbor(maze, rand_frontier):
    directions = ['u', 'd', 'l', 'r']
    x, y = rand_frontier[0], rand_frontier[1]
    random.shuffle(directions)
    for direction in directions:
        if direction == 'u' and y > 0:
            if maze.grid[x][y - 1].state == 'path':
                return [x, y - 1], direction
        if direction == 'd' and y < len(maze.grid[0]) - 1:
            if maze.grid[x][y + 1].state == 'path':
                return [x, y + 1], direction
        if direction == 'l' and x > 0:
            if maze.grid[x - 1][y].state == 'path':
                return [x - 1, y], direction
        if direction == 'r' and x < len(maze.grid ) - 1:
            if maze.grid[x + 1][y].state == 'path':
                return [x + 1, y], direction


#remove walls between given cells
def remove_walls(maze, rand_frontier, rand_neighbor, direction):
    if direction == 'u':
        maze.grid[rand_frontier[0]][rand_frontier[1]].walls['top'] = False
        maze.grid[rand_neighbor[0]][rand_neighbor[1]].walls['bottom'] = False
    elif direction == 'd':
        maze.grid[rand_frontier[0]][rand_frontier[1]].walls['bottom'] = False
        maze.grid[rand_neighbor[0]][rand_neighbor[1]].walls['top'] = False
    elif direction == 'l':
        maze.grid[rand_frontier[0]][rand_frontier[1]].walls['left'] = False
        maze.grid[rand_neighbor[0]][rand_neighbor[1]].walls['right'] = False
    elif direction == 'r':
        maze.grid[rand_frontier[0]][rand_frontier[1]].walls['right'] = False
        maze.grid[rand_neighbor[0]][rand_neighbor[1]].walls['left'] = False
    return maze



#main loop to create the maze
def create_maze(maze):
    #runs once to select starting cell
    if maze.started == False:
        maze = starting_cell(maze)
        maze.started = True

    #loop to create path and walls
    #if there are frontier cells
    if maze.frontier:
        rand_frontier = choose_rand_frontier(maze)
        rand_neighbor, direction = choose_rand_neighbor(maze, rand_frontier)
        maze = remove_walls(maze, rand_frontier, rand_neighbor, direction)
        maze = mark_as_path(maze, rand_frontier[0], rand_frontier[1])
        maze.frontier.remove(rand_frontier)

    #create start and finish and flag is finished
    else:
        maze.grid[int(random.random() * len(maze.grid) / 2)][int(random.random() * len(maze.grid[0]) / 2)].state = 'start'
        maze.grid[int(random.random() * len(maze.grid) / 2 + len(maze.grid) / 2)][int(random.random() * len(maze.grid[0]) / 2 + len(maze.grid[0]) / 2)].state = 'finish'
        maze.finished = True
