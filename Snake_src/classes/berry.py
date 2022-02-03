"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Berry Module
"""
from tkinter import Label, N, S, W, E
from .head import Head
from .board import GameBoard
from random import randint


class Berry:
    def __init__(self, window, appearance):
        self.window = window
        self.appearance = appearance
        self.x = None
        self.y = None

        self.lbl_berry = Label(self.window, bg=f"{self.appearance}")

    def run(self):
        ...

    def grid(self, board: GameBoard, snake: Head):
        lbl = board.get_lbls()
        tail = snake.tail
        # Will regrid the berry until it is in a valid position.
        # Not on tail or head...
        while True:
            self.x, self.y = randint(board.x_min, board.x_max - 1), randint(
                board.y_min, board.y_max - 1)

            if lbl[self.y][self.x].cget("bg") != tail.color and (
                    self.x, self.y) != (snake.x, snake.y):
                self.lbl_berry.grid(column=self.x,
                                    row=self.y,
                                    sticky=N + S + W + E)
                return
            else:
                self.x, self.y = randint(board.x_min,
                                         board.x_max - 1), randint(
                                             board.y_min, board.y_max - 1)
