"""
Name: Gabriel Engberg
Date: 22-11-2021
Info:
snake 3.0 converted to OOP
"""
from tkinter import *
#TODO Fix the imports for following: Gameboard, Snake, Berry, (Tail) & (Spike)

class Snake3:
    def __init__(self):
        self.game_tk = Tk()
        self.board = GameBoard(self.game_tk, 12, ["#d8de81", "#ffde88"])
        self.snake = Snake(self.game_tk, "🐍", "red", "green", int(self.board.x_max / 2))
        self.board._callable_ = self.snake.change_direction

        self.berry = Berry(self.game_tk, "blue")

    def run(self):
        if self.board.run():
            self.berry.grid(self.board, self.snake, self.snake.tail)
            # self.tail.run()
            self.update()

        # END OF FUNCTION #
        self.game_tk.mainloop()

    def update(self):
        if self.snake.alive:
            # !Always update snake first! #
            self.snake.update()
            # !=========================! #
            if self.snake.check_collision(self.board, self.snake.tail):
                self.snake.move()
                if (self.berry.x, self.berry.y) == (self.snake.x, self.snake.y):
                    self.board.update_score()
                    self.snake.tail.length += 1
                    self.berry.grid(self.board, self.snake, self.snake.tail)

                # Tail drawing should go here..... #TODO Implement tail drawing in tail module... @Slayga
                # ? Currently moving tail module to be called inside snake module...move this @Slayga
                if self.board.score > 1:
                    labels = self.board.get_lbls()
                    newTail = labels[self.snake.y][self.snake.x]
                    old_color = newTail.cget("bg")
                    self.game_tk.after(
                        (250 * self.board.score),
                        lambda newTail=newTail, old_color=old_color: newTail.config(
                            bg=old_color
                        ),
                    )
                    self.game_tk.after(
                        250,
                        lambda newTail=newTail, tail_color=self.snake.tail_color: newTail.config(
                            bg=tail_color
                        ),
                    )

            self.game_tk.after(250, self.update)

        else:
            self.snake.kill()


# ======= Runner Code ======= #


def main():
    Snake3().run()


if __name__ == "__main__":
    main()
