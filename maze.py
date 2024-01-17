import pygame

#represent each cell within the maze
class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.state = 'unvisited'
        self.walls = {
            'top': True,
            'bottom': True,
            'left': True,
            'right': True,
        }


#the collection of cells that a maze is composed of
class Maze:
    def __init__(self, size):
        self.started = False
        self.finished = False
        self.height = size
        self.width = size
        self.grid = []
        for i in range(self.width):
            line = []
            for j in range(self.height):
                line.append(Cell(i, j))
            self.grid.append(line)
        self.frontier = []


    #draw the current contents of the maze
    def draw(self, surface):
        cell_x, cell_y = (surface.get_width() / len(self.grid[0])), (surface.get_height() / len(self.grid))
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                x, y = i * cell_x, j * cell_y
                current_cell = self.grid[i][j]

                if current_cell.state == 'unvisited':
                    pygame.draw.rect(surface, pygame.Color('gray25'), (x, y, cell_x, cell_y))

                if current_cell.state == 'wall':
                    pygame.draw.rect(surface, pygame.Color('gray25'), (x, y, cell_x, cell_y))

                if current_cell.state == 'path':
                    pygame.draw.rect(surface, pygame.Color('gray55'), (x, y, cell_x, cell_y))

                if current_cell.state == 'start':
                    pygame.draw.rect(surface, pygame.Color('forestgreen'), (x, y, cell_x, cell_y))
                if current_cell.state == 'finish':
                    pygame.draw.rect(surface, pygame.Color('red2'), (x, y, cell_x, cell_y))

                if current_cell.walls["top"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x, y), (x + cell_x, y), 2)
                if current_cell.walls["left"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x, y), (x, y + cell_y), 2)
                if current_cell.walls["bottom"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x, y + cell_y), (x + cell_x, y + cell_y), 2)
                if current_cell.walls["right"]:
                    pygame.draw.line(surface, pygame.Color('black'), (x + cell_x, y), (x + cell_x, y + cell_y), 2)
