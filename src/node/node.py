import random

import pygame


class Node:

    COLOR_MAPPING = {
        "unvisited": pygame.Color("white"),
        "open": pygame.Color("green"),
        "closed": pygame.Color("red"),
        "start": pygame.Color("blue"),
        "end": pygame.Color("yellow"),
        "obstacle": pygame.Color("black"),
        "path": pygame.Color("purple"),
    }

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.state = "unvisited"
        self.color = self.COLOR_MAPPING.get("unvisited")

    def set_state(self, newState):
        self.state = newState
        newColor = self.COLOR_MAPPING.get(newState)
        self.set_color(newColor)

    def get_state(self):
        return self.state

    def set_color(self, newColor):
        self.color = newColor

    def get_color(self):
        return self.COLOR_MAPPING.get(self.state)
