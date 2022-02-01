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
    def __init__(self):
        self.game_tk = Tk()
        self.board = GameBoard(self.game_tk, 12, ["#d8de81", "#ffde88"])
        self.head = Head(
            self.game_tk, "🐍", "red", "green", int(self.board.x_max / 2)
        )
        self.board._callable_ = self.head.change_direction

        self.berry = Berry(self.game_tk, "blue")

    def run(self):
        if self.board.run():
            self.berry.grid(self.board, self.head, self.head.tail)
            # self.tail.run()
            self.update()

        # END OF FUNCTION #
        self.game_tk.mainloop()

    def update(self):
        if self.head.alive:
            # !Always update head first! #
            self.head.update()
            # !=========================! #
            if self.head.check_collision(self.board, self.head.tail):
                self.head.move()
                if (self.berry.x, self.berry.y) == (self.head.x, self.head.y):
                    self.board.update_score()
                    self.head.tail.length += 1
                    self.berry.grid(self.board, self.head, self.head.tail)

                # Tail drawing should go here..... #TODO Implement tail drawing in tail module... @Slayga
                # ? Currently moving tail module to be called inside head module...move this @Slayga
                if self.board.score > 1:
                    labels = self.board.get_lbls()
                    newTail = labels[self.head.y][self.head.x]
                    old_color = newTail.cget("bg")
                    self.game_tk.after(
                        (250 * self.board.score),
                        lambda newTail=newTail, old_color=old_color: newTail.config(
                            bg=old_color
                        ),
                    )
                    self.game_tk.after(
                        250,
                        lambda newTail=newTail, tail_color=self.head.tail_color: newTail.config(
                            bg=tail_color
                        ),
                    )

            self.game_tk.after(250, self.update)

        else:
            self.head.kill()


# ======= Runner Code ======= #


def main():
    Snake3().run()


if __name__ == "__main__":
    main()
