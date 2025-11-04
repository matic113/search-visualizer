import pygame
from collections import deque

def reconstruct_path(came_from, current, draw):
    """
    Reconstructs the path from the end node back to the start node
    and draws it on the grid.
    """
    while current in came_from:
        current = came_from[current]
        if current.get_state() == "start":
            break
        current.set_state("path")
        draw()
        pygame.time.delay(20)

def bfs(draw, grid, start, end):
    """
    Performs the Breadth-First Search algorithm.
    Returns True if a path is found, False otherwise.
    """
    queue = deque([start])
    came_from = {}
    visited = {start}

    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                import sys
                sys.exit()

        current = queue.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw)
            start.set_state("start") # Ensure start/end colors are correct
            end.set_state("end")
            return True

        if current != start:
            current.set_state("closed")

        for neighbor in grid.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                queue.append(neighbor)
                if neighbor != end:
                    neighbor.set_state("open")

        draw()
        pygame.time.delay(20)

    return False
