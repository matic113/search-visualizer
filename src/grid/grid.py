import pygame

from node.node import Node


class Grid:

    cellsUpdated = 0

    def __init__(self, gridWidth, gridHeight, cellSize):
        self.rows = gridHeight // cellSize
        self.cols = gridWidth // cellSize
        self.width = gridWidth
        self.heigt = gridHeight
        self.cellSize = cellSize
        self.cells = list()

        for row in range(self.rows):
            self.cells.append([])  # Append an empty list for each row
            for col in range(0, self.cols):
                self.cells[row].append(Node(row, col))

        # self.cells[0][0].set_color(pygame.Color("red"))
        # self.cells[-1][-1].set_color(pygame.Color("red"))

    def print(self):
        print(self.cells)

    def updateCell(self, mouseX, mouseY):

        clickedCellCol = mouseX // self.cellSize
        clickedCellRow = mouseY // self.cellSize

        clickedCell = self.cells[clickedCellRow][clickedCellCol]

        if clickedCell.get_state() in ["start", "end"]:
            return

        print(f"updating cell in [{clickedCellRow}, {clickedCellCol}]")

        if self.cellsUpdated == 0:
            clickedCell.set_state("start")
        elif self.cellsUpdated == 1:
            clickedCell.set_state("end")
        else:
            clickedCell.set_state("obstacle")

        self.cellsUpdated += 1

    def reset(self):
        self.cellsUpdated = 0
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].set_state("unvisited")
        print("map reset")
