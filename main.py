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
            self.alive = random.choice([0, 1]) # изначальный шанс появления клетки - 50%
        else:
            self.alive = _alive

    def count_neighbours(self, moves=None):
        if moves is None:
            moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        count = 0
        for i in moves: # считаем, что поверхность замкнута со всех сторон
            if field.cells[(self.x + i[0]) % len(field.cells)][(self.y + i[1]) % len(field.cells[0])].alive:
                count += 1
        return count


BLACK = (0, 0, 0) # цвет поля
WHITE = (255, 255, 255) # цвет клеток
root = pg.display.set_mode((2000, 2000))
pg.display.set_caption('Conways game of Life')


class Field:
    width = root.get_width() // 20
    height = root.get_height() // 20
    cells = [[]]

    def __init__(self, cells_alive=None): # при создании поля можно указать, живые клетки будут или нет
        self.cells = [[Cell(i, j, cells_alive) for j in range(self.width)] for i in range(self.height)]

    def draw(self): # отрисовка поля
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells[i])):
                if self.cells[i][j].alive:
                    pg.draw.rect(root, WHITE, [i * 20, j * 20, 20, 20])
                else:
                    pg.draw.rect(root, (0, 0, 0), [i * 20, j * 20, 20, 20])

    def update(self): # обновление поля
        field2 = Field(0)
        for i in range(len(self.cells)):
            for j in range(len(self.cells[0])):
                if self.cells[i][j].alive:
                    if self.cells[i][j].count_neighbours() not in (2, 3): # клетка умирает
                        field2.cells[i][j] = Cell(i, j, 0)
                        continue
                    field2.cells[i][j] = Cell(i, j, 1) # клетка выживает
                    continue
                if self.cells[i][j].count_neighbours() == 3: # рождается новая клетка
                    field2.cells[i][j] = Cell(i, j, 1)
                    continue
                field2.cells[i][j] = Cell(i, j, 0) # не рождается
        self.cells = field2.cells


field = Field() # создаём основное поле


def main():
    sleep_time = int(input("Какой временной промежуток вы хотите между итерациями? (Целое число, >= 0)))
    while 1:
        time.sleep(sleep_time)
        for event in pg.event.get(): # чтобы ОС не думала, что программа "зависла"
            if event.type == QUIT:
                quit(0)
        field.draw()
        pg.display.update()
        field.update()


main()
