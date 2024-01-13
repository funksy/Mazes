import pygame

#represent each cell within the maze
class Cell:
    def __init__(self, x, y, cell_type):
        self.x, self.y = x, y
        self.visited = False
        if cell_type == 0:
            self.state = 'unvisited'
        if cell_type == 1:
            self.walls = {
                'top': True,
                'bottom': True,
                'left': True,
                'right': True,
            }


#the collection of cells that a maze is composed of
class Maze:
    def __init__(self, height, width, maze_type):
        self.started = False
        self.created = False
        self.height = height
        self.width = width
        self.maze_type = maze_type
        self.grid = []
        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(Cell(i, j, self.maze_type))
            self.grid.append(line)
        self.walls = []


    #draw the current contents of the maze
    def draw(self, surface):
        cell_x, cell_y = (surface.get_width() / len(self.grid[0])), (surface.get_height() / len(self.grid))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                x, y = j * cell_x, i * cell_y
                current_cell = self.grid[i][j]

                if current_cell.state == 'unvisited':
                    pygame.draw.rect(surface, pygame.Color('gray25'), (x, y, cell_x, cell_y))

                if current_cell.state == 'wall':
                    pygame.draw.rect(surface, pygame.Color('gray25'), (x, y, cell_x, cell_y))

                if current_cell.state == 'path':
                    pygame.draw.rect(surface, pygame.Color('gray55'), (x, y, cell_x, cell_y))

                if current_cell.state == 'start' or current_cell.state == 'finish':
                    pygame.draw.rect(surface, pygame.Color('indigo'), (x, y, cell_x, cell_y))

                if self.maze_type == 0:
                    pygame.draw.line(surface, pygame.Color('black'), (x, y), (x + cell_x, y), 1)
                    pygame.draw.line(surface, pygame.Color('black'), (x, y), (x, y + cell_y), 1)
                    pygame.draw.line(surface, pygame.Color('black'), (x, y + cell_y), (x + cell_x, y + cell_y), 1)
                    pygame.draw.line(surface, pygame.Color('black'), (x + cell_x, y), (x + cell_x, y + cell_y), 1)
