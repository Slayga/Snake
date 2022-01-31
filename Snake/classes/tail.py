"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Tail Module
"""
from tkinter import Tk, Label
from typing import Tuple


class Tail:
    def __init__(self, window, color):
        self.window = window
        self.color = color
        self.length = 0

        self.update_speed = 250

    def run(self):
        ...

    # def grow(self, window: Tk, score: int, label: Tuple):
    #     self.old_color = label.cget("bg")
    #     print(self.old_color)
    #     window.after(self.__update_speed, lambda: label.config(bg=self.color))
    #     window.after((self.__update_speed * score),
    #                  lambda: label.config(bg=self.old_color))
