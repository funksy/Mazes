import pygame
from pygame.locals import *
import random
from maze import Maze
from search import Search
from random_prim import create_maze, starting_cell
from bfs import search_maze, backtrack

res = [1000, 1000]

pygame.init()
display_win = pygame.display.set_mode(res)
# win = pygame.Surface((400, 400))
clock = pygame.time.Clock()

size = 500
block = 28

maze = Maze(size)
search = Search(maze)

while True:

    win = pygame.Surface((size * block, size * block))

    #allow pygame window to be exited
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # run create_maze function until maze is created
    if maze.created == False:
        create_maze(maze)
    elif maze.created == True and search.started == False:
        search.initialize(maze)
        search.started = True
    elif search.finished == False:
        search_maze(search, maze)
    else:
        backtrack(search)


    #draw maze in it's current state
    maze.draw(win)
    search.draw(maze, win)

    #scale to resolution and display
    scaled_win = pygame.transform.scale(win, (res))
    display_win.blit(scaled_win, (0, 0))
    pygame.display.flip()
