import time

import pygame as pg
from pygame.locals import *
import random


class Cell:
    x: int
    y: int
    alive: int

    def __init__(self, i, j, _alive=None):
        self.x = i
        self.y = j
        if _alive is None:
            self.alive = random.choice([0, 1])
        else:
            self.alive = _alive

    def count_neighbours(self, moves=None):
        if moves is None:
            moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        for i in moves:
            if field.cells[(self.x + i[0]) % len(field.cells)][(self.y + i[1]) % len(field.cells[0])].alive:
                count += 1
        return count


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
root = pg.display.set_mode((2000, 2000))
pg.display.set_caption('Conways game of Life')


class Field:
    width = root.get_width() // 20
    height = root.get_height() // 20
    cells = [[]]

    def __init__(self, cells_alive=None):
        self.cells = [[Cell(i, j, cells_alive) for j in range(self.width)] for i in range(self.height)]

    def draw(self):
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[i])):
                if self.cells[i][j].alive:
                    pg.draw.rect(root, WHITE, [i * 20, j * 20, 20, 20])
                else:
                    pg.draw.rect(root, (0, 0, 0), [i * 20, j * 20, 20, 20])

    def update(self):
        field2 = Field(0)
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j].alive:
                    if self.cells[i][j].count_neighbours() not in (2, 3):
                        field2.cells[i][j] = Cell(i, j, 0)
                        continue
                    field2.cells[i][j] = Cell(i, j, 1)
                    continue
                if self.cells[i][j].count_neighbours() == 3:
                    field2.cells[i][j] = Cell(i, j, 1)
                    continue
                field2.cells[i][j] = Cell(i, j, 0)
        self.cells = field2.cells


field = Field()


def main():
    while 1:
        time.sleep(0.5)
        for event in pg.event.get():
            if event.type == QUIT:
                quit(0)
        field.draw()
        pg.display.update()
        field.update()


main()
