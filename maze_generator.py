# Maze generation using recursive backtracker algorithm
# https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker

from queue import LifoQueue
from PIL import Image
import numpy as np
import random


def generate_maze(rows, columns):
    maze = Image.new('RGB', (2*columns+1, 2*rows+1), 'black')
    pixels = maze.load()

    # Create a path on the very top and bottom so that it has an entrance/exit
    pixels[1, 0] = (255, 255, 255)
    pixels[-2, -1] = (255, 255, 255)

    stack = LifoQueue()
    cells = np.zeros(rows*columns).reshape(rows, columns)
    cells[0, 0] = 1
    stack.put((0, 0))

    while not stack.empty():
        x, y = stack.get()
        
        left = (x-1, y) if x > 0 and cells[x-1, y] == 0 else None
        right = (x+1, y) if x < cells.shape[0]-1 and cells[x+1, y] == 0 else None
        top = (x, y-1) if y > 0 and cells[x, y-1] == 0 else None
        bottom = (x, y+1) if y < cells.shape[1]-1 and cells[x, y+1] == 0 else None
        
        adjacents = np.array([left, right, top, bottom])
        unvisited_adjacents = adjacents[adjacents != None]
        if unvisited_adjacents.size:
            stack.put((x, y))

            neighbour = random.choice(unvisited_adjacents)
            neighbour_on_img = np.array(neighbour) * 2 + 1
            current_on_img = np.array((x, y)) * 2 + 1
            wall_to_remove = np.mean((neighbour_on_img, current_on_img), axis=0)
            
            pixels[tuple(current_on_img.tolist())] = (255, 255, 255)
            pixels[tuple(wall_to_remove.tolist())] = (255, 255, 255)
            pixels[tuple(neighbour_on_img.tolist())] = (255, 255, 255)

            cells[neighbour] = 1
            stack.put(neighbour)

    return maze

