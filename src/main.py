import pygame

from grid.grid import Grid
from algorithms.dfs import dfs
from algorithms.bfs import bfs
from ui.controls import Controls

# CONSTS
CELL_SIZE = 20
PADDING = 20
CONTROL_PANEL_WIDTH = 200

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800 + PADDING + CONTROL_PANEL_WIDTH, 600 + PADDING))
pygame.display.set_caption("Search Visualizer")
clock = pygame.time.Clock()
running = True
grid = Grid(800, 600, CELL_SIZE)
dt = 0
searching = False
cancel_search = [False]
controls = Controls(0, 0, CONTROL_PANEL_WIDTH, 600 + PADDING)
controls.add_button("cancel", 25, 50, 150, 50, "Cancel", (200, 0, 0), (255, 0, 0))
controls.add_button("start", 25, 120, 150, 50, "Start", (0, 200, 0), (0, 255, 0))
controls.add_dropdown("algo", 25, 200, 150, 50, "DFS", ["DFS", "BFS"])
controls.add_slider("speed", 25, 280, 150, 20, 1, 100, 20)


def draw():
    screen.fill("black")
    # Draw control panel background
    pygame.draw.rect(screen, (50, 50, 50), (0, 0, CONTROL_PANEL_WIDTH, 600 + PADDING))
    # Draw grid on the right side
    for row in range(grid.rows):
        for col in range(grid.cols):
            currCell = grid.cells[row][col]
            currRect = pygame.Rect(
                col * CELL_SIZE + (PADDING / 2) + CONTROL_PANEL_WIDTH,
                row * CELL_SIZE + (PADDING / 2),
                CELL_SIZE,
                CELL_SIZE,
            )
            pygame.draw.rect(screen, currCell.color, currRect)
            pygame.draw.rect(screen, "grey", currRect, 1)
    controls.draw(screen)
    pygame.display.flip()


while running:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        controls.handle_event(event)

        if controls.buttons["cancel"].is_clicked(event):
            if searching:
                cancel_search[0] = True
                print("Search cancelled.")

        if controls.buttons["start"].is_clicked(event):
            if not searching:
                start_node = grid.get_start_node()
                end_node = grid.get_end_node()
                if start_node and end_node:
                    searching = True
                    cancel_search[0] = False
                    algo = controls.dropdowns["algo"].main
                    speed = controls.sliders["speed"].val
                    if algo == "DFS":
                        path_found = dfs(draw, grid, start_node, end_node, cancel_search, speed)
                    else:
                        path_found = bfs(draw, grid, start_node, end_node, cancel_search, speed)
                    searching = False
                    if path_found:
                        print(f"Path found using {algo}!")
                    else:
                        print(f"Path not found using {algo}.")
                else:
                    print("Please select a start and an end node.")

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = event.pos
                mouseX = mouse_pos[0] - (PADDING // 2) - CONTROL_PANEL_WIDTH
                mouseY = mouse_pos[1] - (PADDING // 2)
                if mouseX >= 0:
                    grid.update_cell(mouseX, mouseY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_r:
                grid.reset()
                searching = False
                cancel_search[0] = False

    dt = clock.tick(30) / 1000

pygame.quit()
