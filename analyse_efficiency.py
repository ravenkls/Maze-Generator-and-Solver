"""
This file analyses the efficiency of the MAZE GENERATION algorithm.
"""

import time
import matplotlib.pyplot as plt

from maze_generator import generate_maze

sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400]
times = []

for size in sizes:
    start_time = time.time()

    generate_maze(size, size)
    end_time = time.time() - start_time
    times.append(end_time)

plt.xlabel('Maze Size')
plt.ylabel('Time Taken')
plt.title('Time Taken to Generate Mazes')
plt.plot(sizes, times)
plt.show()