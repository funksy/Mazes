from colorama import Fore
import random


#initialize maze with u's
def init_maze(height, width):
    maze = []
    for i in range(height):
        line = []
        for j in range(width):
            line.append('u')
        maze.append(line)
    return maze


#print maze
def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'u':
                print(Fore.WHITE, f'{maze[i][j]}', end='')
            elif maze[i][j] == 'c':
                print(Fore.GREEN, f'{maze[i][j]}', end='')
            else:
                print(Fore.RED, f'{maze[i][j]}', end='')
        print('\n')


#define starting point for algo
def starting_cell(maze):
    #random starting position
    starting_height = int(random.random() * len(maze))
    starting_width = int(random.random() * len(maze[0]))

    #ensure it's not on a border
    if starting_height == 0:
        starting_height += 1
    if starting_height == len(maze) - 1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == len(maze[0]) - 1:
        starting_width -= 1

    #convert starting position to cell
    maze[starting_height][starting_width] = 'c'

    return maze


#initialize list of walls
def init_walls(maze):
    cell = []
    walls = []

    #find initial cell
    for i in range(len(maze)):
        for j in (range(len(maze[0]))):
            if maze[i][j] == 'c':
                cell += [i, j]

    #assign walls
    walls.append([cell[0] - 1, cell[1]])
    walls.append([cell[0] + 1, cell[1]])
    walls.append([cell[0], cell[1] - 1])
    walls.append([cell[0], cell[1] + 1])

    return walls


#take list of walls and instert them into the maze
def add_walls(maze, walls):
    for wall in walls:
        maze[wall[0]][wall[1]] = 'w'

    return maze


#choose a random wall
def choose_rand_wall(walls):
    return walls[int(random.random() * len(walls)) - 1]


#check how many of the surrounding elemets are cells
def check_surrounding_cells(maze, rand_wall):
    s_cells = 0
    if (maze[rand_wall[0] - 1][rand_wall[1]]) == 'c':
        s_cells += 1
    if (maze[rand_wall[0] + 1][rand_wall[1]]) == 'c':
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] - 1]) == 'c':
        s_cells += 1
    if (maze[rand_wall[0]][rand_wall[1] + 1]) == 'c':
        s_cells += 1
    return s_cells


#define if the wall should convert to a cell
def is_rand_wall_valid(maze, rand_wall):
    #make sure the wall is not on the border
    if rand_wall[0] != 0 and rand_wall[0] != len(maze) - 1 and rand_wall[1] != 0 and rand_wall[1] != len(maze[0]) - 1:

        #check number of surrounding cells
        if check_surrounding_cells(maze, rand_wall) < 2:

            #check if rand_wall is valid and below a cell
            if maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and maze[rand_wall[0] + 1][rand_wall[1]] == 'c':
                return True

            #check if rand_wall is valid and above a cell
            if maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and maze[rand_wall[0] -1][rand_wall[1]] == 'c':
                return True

            #check if rand_wall is valid and left of a cell
            if maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and maze[rand_wall[0]][rand_wall[1] + 1] == 'c':
                return True

            #check if rand wall is valid and right of a cell
            if maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and maze[rand_wall[0]][rand_wall[1] - 1] == 'c':
                return True

    return False


#takes the new cell and creates the surrounding walls
def create_new_walls(maze, walls, cell):
    #element below
    if cell[0] - 1 != 0 and maze[cell[0] - 1][cell[1]] != 'c':
        maze[cell[0] - 1][cell[1]] = 'w'
    if [cell[0] - 1, cell[1]] not in walls:
        walls.append([cell[0] - 1, cell[1]])

    #element above
    if cell[0] + 1 != len(maze) - 1 and maze[cell[0] + 1][cell[1]] != 'c':
        maze[cell[0] + 1][cell[1]] = 'w'
    if [cell[0] + 1, cell[1]] not in walls:
        walls.append([cell[0] + 1, cell[1]])

    #element left
    if cell[1] - 1 != 0 and maze[cell[0]][cell[1] - 1] != 'c':
        maze[cell[0]][cell[1] - 1] = 'w'
    if [cell[0], cell[1] - 1] not in walls:
        walls.append([cell[0], cell[1] - 1])

    #element right
    if cell[1] + 1 != len(maze[0]) - 1 and maze[cell[0]][cell[1] + 1] != 'c':
        maze[cell[0]][cell[1] + 1] = 'w'
    if [cell[0], cell[1] + 1] not in walls:
        walls.append([cell[0], cell[1] + 1])

    walls.remove(cell)

    return maze, walls

#create a maze
def create_maze(height, width):
    #initialize
    maze = init_maze(height, width)
    maze = starting_cell(maze)
    walls = init_walls(maze)
    maze = add_walls(maze, walls)

    #loop to create maze
    while walls:
        rand_wall = choose_rand_wall(walls)
        if is_rand_wall_valid(maze, rand_wall):
            maze[rand_wall[0]][rand_wall[1]] = 'c'
            maze, walls = create_new_walls(maze, walls, rand_wall)
        else:
            walls.remove(rand_wall)

    #clean up
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'u':
                maze[i][j] = 'w'

    #define start and finish
    for i in range(len(maze[0])):
        if maze[1][i] == 'c':
            maze[0][i] = 'c'
            break

    for i in range(len(maze[0]) - 1, 0, -1):
        if maze[len(maze) - 2][i] == 'c':
            maze[len(maze) - 1][i] = 'c'
            break

    return maze

maze = create_maze(20, 100)
print_maze(maze)
