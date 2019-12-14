# Maze Creator / Solver

## Maze Creation Algorithm
To create the mazes, I used the [backtracker algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Recursive_backtracker), this algorithm
utilises a stack data structure and is a depth-first search algorithm.

### It can be described with following steps

1. Choose the initial cell, mark it as visited and push it to the stack
2. While the stack is not empty
    1. Pop a cell from the stack and make it a current cell
    2. If the current cell has any neighbours which have not been visited
        1. Push the current cell to the stack
        2. Choose one of the unvisited neighbours
        3. Remove the wall between the current cell and the chosen cell
        4. Mark the chosen cell as visited and push it to the stack

### Visualised

<img src="https://i.imgur.com/lK2jY41.gif">

### Analysis of Algorithm
This algorithm has a time efficiency of O(n^2)

<img src="https://i.imgur.com/cnYmRiC.png" height="300">

## Maze Solver Algorithm
To solve the mazes, I used [Dijkstra's shortest path algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm), this algorithm utilises a priority queue data structure.

### It can be described with the following steps
1. Choose a start and end node, all nodes other than start node have a distance of **infinity**
2. Consider each adjacent node to the current node, and update the distance of the node 
    - The new distance is the distance of the current node + distance from current node to new node
    - If the new distance is smaller the node's distance already, don't update
3. The priority queue shifts all the nodes into order based on their distance values
4. Dequeue a node from the queue and start again from step 2

### Example
Here is a 500x500 maze generated (Image size is 1001x1001) using the maze generation algorithm as described further above. And it has been solved using the Dijkstra's algorithm implemented in this project.

<img src="https://i.imgur.com/9UdY6ho.png">
