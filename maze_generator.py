# Maze generation using recursive backtracker algorithm
# https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker

from queue import LifoQueue
from PIL import Image
import numpy as np
from random import choice

def generate_maze(width, height):
    maze = Image.new('RGB', (2*width + 1, 2*height + 1), 'black')
    pixels = maze.load()

    # Create a path on the very top and bottom so that it has an entrance/exit
    pixels[1, 0] = (255, 255, 255)
    pixels[-2, -1] = (255, 255, 255)
    
    stack = LifoQueue()
    cells = np.zeros((width, height))
    cells[0, 0] = 1
    stack.put((0, 0))

    while not stack.empty():
        x, y = stack.get()

        adjacents = []
        if x > 0 and cells[x - 1, y] == 0:
            adjacents.append((x - 1, y))
        if x < width - 1 and cells[x + 1, y] == 0:
            adjacents.append((x + 1, y))
        if y > 0 and cells[x, y - 1] == 0:
            adjacents.append((x, y - 1))
        if y < height - 1 and cells[x, y + 1] == 0:
            adjacents.append((x, y + 1))

        if adjacents:
            stack.put((x, y))

            neighbour = choice(adjacents)
            neighbour_on_img = (neighbour[0]*2 + 1, neighbour[1]*2 + 1)
            current_on_img = (x*2 + 1, y*2 + 1)
            wall_to_remove = (neighbour[0] + x + 1, neighbour[1] + y + 1)

            pixels[neighbour_on_img] = (255, 255, 255)
            pixels[current_on_img] = (255, 255, 255)
            pixels[wall_to_remove] = (255, 255, 255)

            cells[neighbour] = 1
            stack.put(neighbour)

    return maze


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("width", nargs="?", type=int, default=32)
    parser.add_argument("height", nargs="?", type=int, default=None)
    parser.add_argument('--output', '-o', nargs='?', type=str, default='generated_maze.png')
    args = parser.parse_args()

    size = (args.width, args.height) if args.height else (args.width, args.width)

    maze = generate_maze(*size)
    maze.save(args.output)