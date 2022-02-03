"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
snake 3.0 converted to OOP
"""
from tkinter import *

# // TODO Fix the imports for following: Gameboard, Head, Berry, (Tail) & (Spike)
from classes.board import GameBoard
from classes.head import Head
from classes.berry import Berry


class Snake3:
    """
    Main handler of all the modules. Main running code
    """

    def __init__(self):
        """
        Constructor and initialize all the modules.
        """
        # TopLevel Tk widget window
        self.game_tk = Tk()
        # The update speed in milliseconds, lower values mean faster movements
        self.update_speed = 150
        # Board manages the main playable area, which is a grid of labels
        self.board = GameBoard(self.game_tk, 12, ["#d8de81", "#ffde88"])
        # The head of the snake, is the "character" you control
        self.head = Head(
            self.game_tk,
            self.board,
            self.update_speed,
            "🐍",
            "red",
            "green",
            int(self.board.x_max / 2),
        )

        #
        self.board._callable_ = self.head.change_direction
        self.berry = Berry(self.game_tk, "blue")

    def run(self):
        if self.board.run():
            self.berry.grid(self.board, self.head, self.head.tail)
            # self.tail.run()
            self.update()

        # END OF FUNCTION Tk().mainloop() executed last#
        self.game_tk.mainloop()

    def update(self):
        if self.head.alive:
            # !Always update head first! #
            # What the update does is moving the heads coordinates onto next
            # square, to be checked if a move is possible.
            self.head.update()

            # The move check is called here .
            if self.head.check_collision(self.head.tail):
                # When the check returns true regrids the head
                self.head.move()
                # If a berry is consumed
                if (self.berry.x, self.berry.y) == (self.head.x, self.head.y):
                    self.board.update_score()
                    self.head.tail.length += 1
                    # Regrids the berry
                    self.berry.grid(self.board, self.head, self.head.tail)

                # // #TODO Implement tail drawing in tail module...
                # Draws the tail when one or more berry have been consumed
                if self.board.score > 1:
                    self.head.tail.update()
            # When all checks and updates are done,
            # queues next update after x ms time.
            self.game_tk.after(self.update_speed, self.update)

        else:
            # Stops the snake & change to its death color.
            self.head.kill()


# ======= Runner Code ======= #


def main():
    Snake3().run()


if __name__ == "__main__":
    main()
