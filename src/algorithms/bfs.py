import pygame
from collections import deque

def reconstruct_path(came_from, current, draw, speed):
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
        pygame.time.delay(int(100 / speed))

def bfs(draw, grid, start, end, cancel_flag, speed):
    """
    Performs the Breadth-First Search algorithm.
    Returns True if a path is found, False otherwise.
    """
    queue = deque([start])
    came_from = {}
    visited = {start}

    while queue:
        if cancel_flag[0]:
            return False

        current = queue.popleft()

        if current == end:
            reconstruct_path(came_from, end, draw, speed)
            start.set_state("start") # Ensure start/end colors are correct
            end.set_state("end")
            return True

        if current != start:
            current.set_state("closed")

        for neighbor in grid.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current

                if neighbor == end:
                    reconstruct_path(came_from, end, draw, speed)
                    start.set_state("start")
                    end.set_state("end")
                    return True

                queue.append(neighbor)
                neighbor.set_state("open")

        draw()
        pygame.time.delay(int(100 / speed))

    return False
