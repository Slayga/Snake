"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Head Module
"""
from tkinter import Tk, Label, N, S, W, E
from .board import GameBoard
from .tail import Tail


class Head:
    def __init__(
        self,
        window: Tk,
        apperance: str,
        head_color: str,
        tail_color: str,
        start_pos: int,
        audio: bool = False,
    ):
        self.window = window
        self.apperance = apperance
        self.head_color = head_color
        self.tail_color = tail_color
        self.start_pos = start_pos

        self.x = start_pos
        self.y = start_pos

        self.alive = True

        self.direction = str()
        self.old_direction = str()

        self.audio = audio

        self.lbl_head = Label(self.window, bg=self.head_color)

        self.lbl_head.grid(
            column=self.start_pos, row=self.start_pos, sticky=N + S + W + E
        )

        self.tail = Tail(self.window, self.tail_color)

    def opposite_dir(self, dir) -> str:
        if dir == "Right":
            return "Left"

        elif dir == "Left":
            return "Right"

        elif dir == "Up":
            return "Down"

        elif dir == "Down":
            return "Up"

        elif dir == "d":
            return "a"

        elif dir == "a":
            return "d"

        elif dir == "w":
            return "s"

    def change_direction(self, value=None):
        if value is not None:
            self.old_direction = self.direction
            self.direction = value

    def update(self):
        if self.direction == "Right":
            self.x += 1

        elif self.direction == "Left":
            self.x -= 1

        elif self.direction == "Up":
            self.y -= 1

        elif self.direction == "Down":
            self.y += 1

        elif self.direction == "d":
            self.x += 1

        elif self.direction == "a":
            self.x -= 1

        elif self.direction == "w":
            self.y -= 1

        elif self.direction == "s":
            self.y += 1

    def check_collision(
        self, board: GameBoard, tail: Tail, spike: object = None
    ):
        lbl = board.get_lbls()
        # Check if head is out of bounds
        if (
            self.x >= board.x_max
            or self.x < board.x_min
            or self.y >= board.y_max
            or self.y < board.y_min
        ):
            self.alive = None
            return False
        # Check if head is turning in to itself when it has a tail
        elif (
            self.old_direction == self.opposite_dir(self.direction)
            and board.score > 1
        ):
            self.alive = None
            return False
        # Check if head collides with the tail
        elif lbl[self.y][self.x].cget("bg") == tail.color and board.score > 1:
            self.alive = None
            return False
        # If spike is in the game, checks collision for that...
        if spike is not None:
            if lbl[self.y][self.x].cget("text") == spike.apperance:
                self.alive = None
                return False
        return True

    def move(self):
        self.lbl_head.grid(row=self.y, column=self.x)

    def kill(self):
        self.alive = None
        self.direction = ""
        self.lbl_head.config(bg="black")
