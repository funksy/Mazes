from maze import Maze, Cell
from search import Search


def add_adjacent_cells(search, maze):
    cell = maze.grid[search.current[0]][search.current[1]]
    if not cell.walls['top'] and search.explored[(cell.x, cell.y - 1)] == False:
        search.backtrack[cell.x, cell.y - 1] = [cell.x, cell.y]
        search.frontier.append([cell.x, cell.y - 1])
    if not cell.walls['right'] and search.explored[(cell.x + 1, cell.y)] == False:
        search.backtrack[cell.x + 1, cell.y] = [cell.x, cell.y]
        search.frontier.append([cell.x + 1, cell.y])
    if not cell.walls['bottom'] and search.explored[(cell.x, cell.y + 1)] == False:
        search.backtrack[cell.x, cell.y + 1] = [cell.x, cell.y]
        search.frontier.append([cell.x, cell.y + 1])
    if not cell.walls['left'] and search.explored[(cell.x - 1, cell.y)] == False:
        search.backtrack[cell.x - 1, cell.y] = [cell.x, cell.y]
        search.frontier.append([cell.x - 1, cell.y])
    return search


def search_maze(search, maze):
    if search.frontier and search.current != search.finish:
        search = add_adjacent_cells(search, maze)
        search.current = search.frontier.pop()
        search.explored[(search.current[0], search.current[1])] = True

    else:
        search.finished = True


def backtrack(search):
    if search.current != search.start:
        search.solution.append(search.backtrack[(search.current[0], search.current[1])])
        search.current = search.backtrack[(search.current[0], search.current[1])]
