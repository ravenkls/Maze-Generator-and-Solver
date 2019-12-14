from typing import List

PATH = (255, 255, 255)
WALL = (0, 0, 0)


class Node:
    """Represents a node on a weighted graph for a maze."""

    def __init__(self, coords):
        self.coords = coords
        self.previous = None
        self.distance = None
        self.adjacency_list = {}
    
    def link(self, node, weight=1):
        """Links 2 nodes together with a weight."""
        self.adjacency_list[node] = weight
        node.adjacency_list[self] = weight

    def __repr__(self):
        return f'Node({self.coords!r})'


def nodes_from_maze(image) -> (Node, Node, List[Node]):
    """Generate a list of Nodes for a maze for navigation
    so that they are linked up width weighted edges based
    on the distance from one another in the maze.
    
    The maze must be made up of black (#000000) and white (#FFFFFF) pixels, 
    The start point must be either on the left or top side,
    The end point must be either on the bottom or right side.

    Returns the start node, the finish node, and an array of all the nodes."""

    nodes = {}
    start_node = None
    finish_node = None
    maze = image.convert('RGB')
    pixels = maze.load()

    # Identify all nodes in the maze, and also create all the edges for
    # horizontal paths in the graph

    for y in range(maze.height):

        last_node = None
        weight_counter = 0

        for x in range(maze.width):
            if pixels[x, y] == PATH:
                left = pixels[x-1, y] if x > 0 else None
                right = pixels[x+1, y] if x < maze.width-1 else None
                top = pixels[x, y-1] if y > 0 else None
                bottom = pixels[x, y+1] if y < maze.height-1 else None

                horizontal_paths = (left == PATH or right == PATH)
                vertical_paths = (top == PATH or bottom == PATH)
                turning_point = horizontal_paths and vertical_paths
                dead_end = [left, right, top, bottom].count(PATH) == 1

                if turning_point or dead_end:
                    node = Node((x, y))

                    if not start_node and (x == 0 or y == 0):
                        start_node = node
                    elif not finish_node and (x == maze.width-1 or y == maze.width-1):
                        finish_node = node

                    if last_node:
                        node.link(last_node, weight_counter)
                        weight_counter = 0

                    last_node = node
                    nodes[(x, y)] = node

                weight_counter += 1

            else:
                last_node = None
                weight_counter = 0

    # Create all the edges for all vertical paths in the graph

    for x in range(maze.width):

        last_node = None
        weight_counter = 0

        for y in range(maze.height):
            if pixels[x, y] == PATH:
                if node := nodes.get((x, y)):
                    if last_node:
                        node.link(last_node, weight_counter)
                        weight_counter = 0
                    last_node = node
                weight_counter += 1
            else:
                last_node = None
                weight_counter = 0

    # Convert nodes dictionary into a list of nodes
    nodes = list(nodes.values())
    return start_node, finish_node, nodes
