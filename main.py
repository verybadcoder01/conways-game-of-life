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
            if cells[(self.x + i[0]) % len(cells)][(self.y + i[1]) % len(cells[0])].alive:
                count += 1
        return count


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
root = pg.display.set_mode((2000, 2000))
pg.display.set_caption('Conways game of Life')
cells = [[Cell(i, j) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]


while 1:
    time.sleep(0.5)
    # root.fill(WHITE)
    # for i in range(0, root.get_height() // 20):
    #     pg.draw.line(root, WHITE, (0, i * 20), (root.get_width(), i * 20))
    # for j in range(0, root.get_width() // 20):
    #     pg.draw.line(root, WHITE, (j * 20, 0), (j * 20, root.get_height()))
    for i in pg.event.get():
        if i.type == QUIT:
            quit(0)
    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            print(cells[i][j].alive, i, j)
            if cells[i][j].alive:
                pg.draw.rect(root, WHITE, [i * 20, j * 20, 20, 20])
            else:
                pg.draw.rect(root, (0, 0, 0), [i * 20, j * 20, 20, 20])
    pg.display.update()
    cells2 = [[Cell(_, __, 0) for _ in range(len(cells[0]))] for __ in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j].alive:
                if cells[i][j].count_neighbours() not in (2, 3):
                    cells2[i][j] = Cell(i, j, 0)
                    continue
                cells2[i][j] = Cell(i, j, 1)
                continue
            if cells[i][j].count_neighbours() == 3:
                cells2[i][j] = Cell(i, j, 1)
                continue
            cells2[i][j] = Cell(i, j, 0)
    cells = cells2
