import random
from maze import Maze, Cell


#identify starting cell and walls
def starting_cell(maze):
    #choose random starting position
    start_y = int(random.random() * len(maze.grid))
    start_x = int(random.random() * len(maze.grid[0]))

    #ensure it's not on a border
    if start_y == 0:
        start_y += 1
    if start_y == len(maze.grid) - 1:
        start_y -= 1
    if start_x == 0:
        start_x += 1
    if start_x == len(maze.grid[0]) - 1:
        start_x -= 1

    #convert starting position to a path
    maze.grid[start_y][start_x].state = 'path'

    #add surrounding cells to list of walls
    cell = [start_y, start_x]
    maze.walls.append([cell[0] - 1, cell[1]])
    maze.walls.append([cell[0] + 1, cell[1]])
    maze.walls.append([cell[0], cell[1] - 1])
    maze.walls.append([cell[0], cell[1] + 1])

    #convert cells in maze grid to walls
    for wall in maze.walls:
        maze.grid[wall[0]][wall[1]].state = 'wall'

    return maze


#choose a wall from the walls list randomly
def choose_rand_wall(maze):
    return maze.walls[int(random.random() * len(maze.walls)) - 1]


#check how many of the surrounding cells are paths
def check_surrounding_cells(maze, rand_wall):
    s_cells = 0
    if maze.grid[rand_wall[0] - 1][rand_wall[1]].state == 'path':
        s_cells += 1
    if maze.grid[rand_wall[0] + 1][rand_wall[1]].state == 'path':
        s_cells += 1
    if maze.grid[rand_wall[0]][rand_wall[1] - 1].state == 'path':
        s_cells += 1
    if maze.grid[rand_wall[0]][rand_wall[1] + 1].state == 'path':
        s_cells += 1
    return s_cells


#define if the wall should convert to a path
def is_rand_wall_valid(maze, rand_wall):
    u = 'unvisited'
    p = 'path'
    #make sure the wall is not on the border
    if rand_wall[0] != 0 and rand_wall[0] != len(maze.grid) - 1 and rand_wall[1] != 0 and rand_wall[1] != len(maze.grid[0]) - 1:

        #check number of surrounding cells
        if check_surrounding_cells(maze, rand_wall) < 2:

            #check if rand_wall is valid and below a cell
            if maze.grid[rand_wall[0] - 1][rand_wall[1]].state == u and maze.grid[rand_wall[0] + 1][rand_wall[1]].state == p:
                return True

            #check if rand_wall is valid and above a cell
            elif maze.grid[rand_wall[0] + 1][rand_wall[1]].state == u and maze.grid[rand_wall[0] -1][rand_wall[1]].state == p:
                return True

            #check if rand_wall is valid and left of a cell
            elif maze.grid[rand_wall[0]][rand_wall[1] - 1].state == u and maze.grid[rand_wall[0]][rand_wall[1] + 1].state == p:
                return True

            #check if rand wall is valid and right of a cell
            elif maze.grid[rand_wall[0]][rand_wall[1] + 1].state == u and maze.grid[rand_wall[0]][rand_wall[1] - 1].state == p:
                return True

    return False


#creates walls surrounding the given cell and appends them to the list of walls
def create_new_walls(maze, cell):
    #element below
    if cell[0] - 1 != 0 and maze.grid[cell[0] - 1][cell[1]].state != 'path':
        maze.grid[cell[0] - 1][cell[1]].state = 'wall'
    if [cell[0] - 1, cell[1]] not in maze.walls:
        maze.walls.append([cell[0] - 1, cell[1]])

    #element above
    elif cell[0] + 1 != len(maze.grid) - 1 and maze.grid[cell[0] + 1][cell[1]].state != 'path':
        maze.grid[cell[0] + 1][cell[1]].state = 'wall'
    if [cell[0] + 1, cell[1]] not in maze.walls:
        maze.walls.append([cell[0] + 1, cell[1]])

    #element left
    elif cell[1] - 1 != 0 and maze.grid[cell[0]][cell[1] - 1].state != 'path':
        maze.grid[cell[0]][cell[1] - 1].state = 'wall'
    if [cell[0], cell[1] - 1] not in maze.walls:
        maze.walls.append([cell[0], cell[1] - 1])

    #element right
    elif cell[1] + 1 != len(maze.grid[0]) - 1 and maze.grid[cell[0]][cell[1] + 1].state != 'path':
        maze.grid[cell[0]][cell[1] + 1].state = 'wall'
    if [cell[0], cell[1] + 1] not in maze.walls:
        maze.walls.append([cell[0], cell[1] + 1])

    maze.walls.remove(cell)

    return maze


#main loop to create a maze
def create_maze(maze):
    #run first time to select starting cell
    if maze.started == False:
        maze = starting_cell(maze)
        maze.started = True

    #loop to create path and walls
    if maze.walls:
        rand_wall = choose_rand_wall(maze)
        if is_rand_wall_valid(maze, rand_wall):
            maze.grid[rand_wall[0]][rand_wall[1]].state = 'path'
            maze = create_new_walls(maze, rand_wall)
        else:
            maze.walls.remove(rand_wall)

    #convert remaining unvisited cells to walls and add start and finish
    else:
        for i in range(len(maze.grid)):
            for j in range(len(maze.grid[0])):
                if maze.grid[i][j].state == 'unvisited':
                    maze.grid[i][j].state = 'wall'

        for i in range(len(maze.grid[0])):
            if maze.grid[1][i].state == 'path':
                maze.grid[0][i].state = 'start'
                break

        for i in range(len(maze.grid[0]) - 1, 0, -1):
            if maze.grid[len(maze.grid) -2][i].state == 'path':
                maze.grid[len(maze.grid) -1][i].state = 'finish'
                break

        maze.created = True

    return maze
