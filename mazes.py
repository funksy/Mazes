import pygame
import random
from maze import Maze
from random_prim import create_maze, starting_cell

res = [1000, 1000]

pygame.init()
display_win = pygame.display.set_mode(res)
win = pygame.Surface((400, 400))
# clock = pygame.time.Clock()


maze = Maze(40, 40, 0)

while True:

    #allow pygame window to be exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    #run create_maze function until maze is created
    if maze.created == False:
        create_maze(maze)

    #draw maze in it's current state
    maze.draw(win)

    #scale to resolution and display
    scaled_win = pygame.transform.scale(win, res)
    display_win.blit(scaled_win, (0, 0))
    pygame.display.flip()
