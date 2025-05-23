import pygame

from node.node import Node


class Grid:
    cells_updated = 0

    def __init__(self, gridWidth, gridHeight, cellSize):
        self.rows = gridHeight // cellSize
        self.cols = gridWidth // cellSize
        self.width = gridWidth
        self.heigt = gridHeight
        self.cell_size = cellSize
        self.cells = list()

        for row in range(self.rows):
            self.cells.append([])  # Append an empty list for each row
            for col in range(0, self.cols):
                self.cells[row].append(Node(row, col))

    def print(self):
        print(self.cells)

    def update_cell(self, mouseX, mouseY):

        clicked_cell_col = mouseX // self.cell_size
        clicked_cell_row = mouseY // self.cell_size

        clicked_cell = self.cells[clicked_cell_row][clicked_cell_col]

        if clicked_cell.get_state() in ["start", "end"]:
            return

        print(f"updating cell in [{clicked_cell_row}, {clicked_cell_col}]")

        if self.cells_updated == 0:
            clicked_cell.set_state("start")
        elif self.cells_updated == 1:
            clicked_cell.set_state("end")
        else:
            clicked_cell.set_state("obstacle")

        self.cells_updated += 1

    def get_start_node(self):
        for row in range(self.rows):
            for col in range(self.cols):
                curr_cell = self.cells[row][col]
                if curr_cell.state == "start":
                    return curr_cell

    def get_end_node(self):
        for row in range(self.rows):
            for col in range(self.cols):
                curr_cell = self.cells[row][col]
                if curr_cell.state == "end":
                    return curr_cell

    def get_neighbors(self, node):
        # search order down, right, left, up
        potential_neighbors_offsets = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        neighbors = []
        for offset in potential_neighbors_offsets:
            neighbor_row = node.row + offset[0]
            neighbor_col = node.col + offset[1]

            if not (0 <= neighbor_row < self.rows):
                continue

            if not (0 <= neighbor_col < self.cols):
                continue

            neighbor_cell = self.cells[neighbor_row][neighbor_col]
            if neighbor_cell.state == "obstacle":
                continue

            neighbors.append(neighbor_cell)

        return neighbors

    def reset(self):
        self.cells_updated = 0
        for row in range(self.rows):
            for col in range(self.cols):
                self.cells[row][col].set_state("unvisited")
        print("map reset")
