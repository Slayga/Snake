"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Berry Module
"""
from tkinter import Label, N, S, W, E
from .head import Head
from .board import GameBoard
from .tail import Tail
from random import randint


class Berry:
    def __init__(self, window, apperance):
        self.window = window
        self.apperance = apperance
        self.x = None
        self.y = None

        self.lbl_berry = Label(self.window, bg=f"{self.apperance}")

    def run(self):
        ...

    def grid(self, board: GameBoard, snake: Head, tail: Tail):
        lbl = board.get_lbls()
        while True:
            self.x, self.y = randint(board.x_min, board.x_max - 1), randint(
                board.y_min, board.y_max - 1
            )

            if lbl.get(self.y)[self.x].cget("bg") != tail.color and (
                self.x,
                self.y,
            ) != (snake.x, snake.y):
                self.lbl_berry.grid(
                    column=self.x, row=self.y, sticky=N + S + W + E
                )
                return
            else:
                self.x, self.y = randint(
                    board.x_min, board.x_max - 1
                ), randint(board.y_min, board.y_max - 1)
