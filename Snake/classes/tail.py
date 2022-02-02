"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Tail Module
"""
from tkinter import Tk, Label
from typing import Tuple
from .board import GameBoard


class Tail:
    def __init__(self, window: Tk, head: object, board: GameBoard, color: str):
        self.window = window
        self.head = head
        self.board = board
        self.color = color
        self.length = 0

        self.update_speed = 250

    def run(self):
        ...

    def update(self):
        self.__labels = self.board.get_lbls()
        self.__newTail = self.__labels[self.head.y][self.head.x]
        self.__old_color = self.__newTail.cget("bg")
        self.window.after(
            (250 * self.board.score),
            lambda newTail=self.__newTail, old_color=self.__old_color: newTail.config(
                bg=old_color
            ),
        )
        self.window.after(
            250,
            lambda newTail=self.__newTail, tail_color=self.head.tail_color: newTail.config(
                bg=tail_color
            ),
        )
