import time

import pygame as pg
from pygame.locals import *
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
root = pg.display.set_mode((2000, 2000))
pg.display.set_caption('Conways game of Life')
cells = [[random.choice([0, 1]) for j in range(root.get_width() // 20)] for i in range(root.get_height() // 20)]


def count_neighbours(pos: list, moves=None):
    if moves is None:
        moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    count = 0
    for i in moves:
        if cells[(pos[0] + i[0]) % len(cells)][(pos[1] + i[1]) % len(cells[0])]:
            count += 1
    return count


while 1:
    time.sleep(0.5)
    root.fill(WHITE)
    for i in range(0, root.get_height() // 20):
        pg.draw.line(root, BLACK, (0, i * 20), (root.get_width(), i * 20))
    for j in range(0, root.get_width() // 20):
        pg.draw.line(root, BLACK, (j * 20, 0), (j * 20, root.get_height()))
    for i in pg.event.get():
        if i.type == QUIT:
            quit(0)
    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            print(cells[i][j], i, j)
            pg.draw.rect(root, (255 * cells[i][j] % 256, 0, 0), [i * 20, j * 20, 20, 20])
    pg.display.update()
    cells2 = [[0 for _ in range(len(cells[0]))] for __ in range(len(cells))]
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]:
                if count_neighbours([i, j]) not in (2, 3):
                    cells2[i][j] = 0
                    continue
                cells2[i][j] = 1
                continue
            if count_neighbours([i, j]) == 3:
                cells2[i][j] = 1
                continue
            cells2[i][j] = 0
    cells = cells2
