import pygame

from grid.grid import Grid
from algorithms.dfs import dfs
from algorithms.bfs import bfs

# CONSTS
CELL_SIZE = 20
PADDING = 20

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800 + PADDING, 600 + PADDING))
pygame.display.set_caption("Search Visualizer")
clock = pygame.time.Clock()
running = True
grid = Grid(800, 600, CELL_SIZE)
dt = 0

def draw():
    screen.fill("black")
    for row in range(grid.rows):
        for col in range(grid.cols):
            currCell = grid.cells[row][col]
            currRect = pygame.Rect(
                col * CELL_SIZE + (PADDING / 2),
                row * CELL_SIZE + (PADDING / 2),
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, currCell.color, currRect)
            pygame.draw.rect(screen, "grey", currRect, 1)
    pygame.display.flip()

while running:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                mouseX = mouse_pos[0] - (PADDING // 2)
                mouseY = mouse_pos[1] - (PADDING // 2)
                grid.update_cell(mouseX, mouseY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_r:
                grid.reset()
            if event.key == pygame.K_d:
                start_node = grid.get_start_node()
                end_node = grid.get_end_node()

                if start_node and end_node:
                    path_found = dfs(draw, grid, start_node, end_node)
                    if path_found:
                        print("Path found using DFS!")
                    else:
                        print("Path not found using DFS.")
                else:
                    print("Please select a start and an end node.")
            if event.key == pygame.K_b:
                start_node = grid.get_start_node()
                end_node = grid.get_end_node()

                if start_node and end_node:
                    path_found = bfs(draw, grid, start_node, end_node)
                    if path_found:
                        print("Path found using BFS!")
                    else:
                        print("Path not found using BFS.")
                else:
                    print("Please select a start and an end node.")

    dt = clock.tick(30) / 1000

pygame.quit()
