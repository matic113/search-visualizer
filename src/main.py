import pygame

from grid.grid import Grid

# CONSTS
CELL_SIZE = 40
PADDING = 20

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800 + PADDING, 600 + PADDING))
pygame.display.set_caption("Search Visualizer")
clock = pygame.time.Clock()
running = True
grid = Grid(800, 600, CELL_SIZE)
dt = 0

while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            mouseX = mouse_pos[0] - (PADDING // 2)
            mouseY = mouse_pos[1] - (PADDING // 2)
            print("Left click at:", mouse_pos)
            grid.update_cell(mouseX, mouseY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_r:
                grid.reset()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # draw grid
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

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(30) / 1000

pygame.quit()
