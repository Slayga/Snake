"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
Snake Module
"""
from tkinter import Tk, Label, N, S, W, E
from boardModule import GameBoard
from tailModule import Tail

class Snake:
    def __init__(self, window: Tk, apperance: str, head_color: str, tail_color: str, start_pos:int, audio:bool=False):
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
        
        self.lbl_snake = Label(self.window, bg=self.head_color)
        
        self.lbl_snake.grid(column=self.start_pos,
                            row=self.start_pos, sticky=N + S + W+ E)
        
        self.tail = Tail(self.window, self.tail_color)
        
    def opposite_dir(self, dir)->str:
        match dir:
            case "Right":
                return "Left"
            case "Left":
                return "Right"
            case "Up":
                return "Down"
            case "Down":
                return "Up"
            case "d":
                return "a"
            case "a":
                return "d"
            case "w":
                return "s"
            case "s":
                return "w"
    
    def change_direction(self, value=None):
        if value is not None:
            self.old_direction = self.direction
            self.direction = value
        
    def update(self):
        match self.direction:
            case "Right":
                self.x += 1
            case "Left":
                self.x -= 1
            case "Up":
                self.y -= 1
            case "Down":
                self.y += 1
            case "d":
                self.x += 1
            case "a":
                self.x -= 1
            case "w":
                self.y -= 1
            case "s":
                self.y += 1

    
    def check_collision(self, board: GameBoard, tail: Tail, spike:object=None):
        lbl = board.get_lbls()
        # Check if snake is out of bounds
        if (self.x >= board.x_max or
            self.x < board.x_min or
            self.y >= board.y_max or
            self.y < board.y_min):
            self.alive = None
            return False
        # Check if snake is turning in to itself when it has a tail
        elif self.old_direction == self.opposite_dir(self.direction) and board.score > 1:
            self.alive = None
            return False
        # Check if snake collides with the tail
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
        self.lbl_snake.grid(row=self.y, column=self.x)
    
    def kill(self):
        self.alive = None
        self.direction = ""
        self.lbl_snake.config(bg="black")