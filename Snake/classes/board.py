"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Gameboard class
"""

from tkinter import Tk, Label, Grid, N, S, W, E
from random import choice as r_choice
from typing import Callable


class GameBoard:
    def __init__(self, window: Tk, size: int, colors: list, callable_: Callable = None):

        self.window = window
        # Borders of the game board
        self.x_min = 1
        self.y_min = 1
        # Makes sure the board is at least 2 in width, sets x_max and y_max to same value
        self.x_max = self.y_max = size if size > 2 else 12

        self.colors = colors

        self.score = 0

        # Tk() ... CHANGE AT OWN RISK
        # Scaler is to get the screen to fit the size of the playarea.
        self.__scaler = 45.8 + (1 / 3)  # => (46.1333333)
        self.__tk_x = int((self.x_max + 1) * self.__scaler)
        self.window.resizable(0, 0)
        self.window.geometry(f"{self.__tk_x}x{int(self.__tk_x+(2*45.8+(1/3)))}")
        self.window.title("Snake3.1")
        self.window.configure(bg="white")
        # /-------------- End of Tk() --------------/ #

        self._callable_ = callable_ if callable(callable_) else None

        # Allowed keypresses for changing direction
        self.possible_dir = ["Up", "Down", "Left", "Right", "d", "a", "w", "s"]
        # Creating the "play area" for the game aka bounds & ui after
        self.__create_board_grid()
        self.__create_ui()

    @property
    def callable_(self):
        return self._callable_

    @callable_.setter
    def callable(self, value):
        if callable(value):
            self._callable_ = value
        else:
            raise TypeError("Non callable value")

    def display_text(self, text=None):
        self.scoreboard.config(text=(None if text is None else text))

    def update_score(self):
        self.score += 1
        self.scoreboard.config(text=self.score - 1)

    def run(self):
        # Make sure the control is listening for keyboard events
        self.control.focus()
        return True

    def get_lbls(self) -> dict[list[Label]]:
        return self.__lbls

    def get_dir(self, event) -> str:
        if self.score < 1 and event.keysym in self.possible_dir:
            self.update_score()
        if event.keysym in self.possible_dir:
            self.callable_(event.keysym)
        return

    def __create_board_grid(self) -> dict:
        self.__lbls = dict()

        # // TODO
        # Creates game bounds...
        # Starts with looping over every y-row
        for y in range(self.y_min, self.y_max):
            # self.__lbls => {1:[], 2:[], 3:[] ... y:[]}
            self.__lbls[y] = list()
            # The key is the y coordinate, and the value is a list of all x
            # coordinates as Labels

            # Scales the label to fit window size
            Grid.rowconfigure(self.window, y, weight=1)

            # Adds empty values to the void of the "world" or you can call it a border
            for _ in range(0, self.x_min):
                self.__lbls[y].append(None)

            for i in range(0, self.y_min):
                self.__lbls[i] = None

            # Create every label
            for x in range(self.x_min, self.x_max):
                # Scales the label to fit window size
                Grid.columnconfigure(self.window, x, weight=1)
                self.__rbg = r_choice(self.colors)
                self.__xlbl = Label(
                    self.window,
                    bg=self.__rbg,
                )
                self.__xlbl.grid(row=y, column=x, sticky=N + S + E + W)
                self.__lbls[y].append(self.__xlbl)

    def __create_ui(self):
        # // TODO
        # Create scorebar & controller-bar at the top
        self.scoreboard = Label(
            self.window,
            text=f"Press {', '.join(i for i in self.possible_dir)} to start",
            bg="white",
        )
        self.scoreboard.grid(column=1, row=0, columnspan=self.x_max)

        self.control = Label(self.window, bg="white")
        self.control.grid(column=1, row=0)
        self.control.bind("<KeyPress>", self.get_dir)


if __name__ == "__main__":
    window = Tk()
    board = GameBoard(window, 12, ["#d8de81", "#ffde88"])

    board.get_lbls()

    window.mainloop()
