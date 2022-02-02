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
    """
    Class GameBoard creates and handles a grid of labels that represents a
    playable area. Which then is used to draw an object on.
    Example a snake or berry.
    \n
    .
    The board consist of the bounds surrounding the playable area: [...]
    And a Label listening for keyboard events.
    \n
    .
    For more in-depth read the board.md in the docs folder (https://github.com/Slayga/Snake/tree/main/docs)
    """

    def __init__(
        self, window: Tk, size: int, colors: list, callable_: Callable = None
    ):
        """Constructor for class... Configures the main playable grid of the game.
        Create bounds for the grid and calls for generations of grid(Labels).

        Args:
            window (Tk): TopLevel Widget
            size (int): How big the playable area will be, note the total
                        playable area is size - x_min. If its less than or
                        equal to 2 it defaults to 8 + x_min
            colors (list): list of str values in hex color-code.
                            This is to color each Label.
                            (Picks randomly from the list each Label)
            callable_ (Callable, optional): The keyboard event listener calls
                                            this value and passes the keysym
                                            as argument. Defaults to None.
        """
        self.window = window
        # Borders of the game board
        self.x_min = self.y_min = 1
        # Makes sure the board is at least 2 in width, sets x_max and y_max to same value
        self.x_max = self.y_max = (
            size if (size - self.x_min) > 2 else self.x_min + 8
        )

        self.colors = colors

        self.score = 0

        # /-------- Tk() | Change at own risk ---------/ #
        # Scaler is to get the screen to fit the size of the playarea.
        self.__scaler = 45.8 + (1 / 3)  # => (46.1333333)
        self.__tk_x = int((self.x_max + 1) * self.__scaler)
        self.window.resizable(0, 0)
        self.window.geometry(
            f"{self.__tk_x}x{int(self.__tk_x+(2*self.__scaler))}"
        )
        self.window.title("Snake3.1")
        self.window.configure(bg="white")
        # /-------------- End of Tk() --------------/ #

        # Placeholder for the callable function outside of this class
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
        """Overrides the text in scoreboard.
        Resets automatically with update_score()

        Args:
            text (Any, optional): What will be displayed instead of score
             until score update. Defaults to None.
        """
        self.scoreboard.config(text=text)

    def update_score(self):
        """Updates score and updates scoreboard Label"""
        self.score += 1
        self.scoreboard.config(text=self.score - 1)

    def run(self):
        """When ready to start call run() to "focus" on controls

        Returns:
            bool: Always returns True
        """
        # Make sure the control is listening for keyboard events
        self.control.focus()
        return True

    def get_lbls(self) -> dict[list[Label]]:
        """Gets the board (All Labels) see docs for more details
        (https://github.com/Slayga/Snake/tree/main/docs)

        Returns:
            dict[list[Label]]: dict with list of labels
        """
        return self.__lbls

    def get_dir(self, event) -> str:
        """Event listener for keyboard events calls the callable:_
        Also awaits for start in beginning (when score less than 1).
        Args:
            event (str): Where keyboard stroke gets passed

        Returns:
            Void
        """
        # keysym is the key name that is pressed
        if self.score < 1 and event.keysym in self.possible_dir:
            self.update_score()
        if event.keysym in self.possible_dir:
            self.callable_(event.keysym)
        return

    def __create_board_grid(self) -> dict:
        """Constructs the grid for the whole board."""
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
            for i in range(0, self.y_min):
                self.__lbls[i] = None

            for _ in range(0, self.x_min):
                self.__lbls[y].append(None)

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

        # Deleting temporary variables from memory
        del self.__rbg, self.__xlbl

    def __create_ui(self):
        """Constructs the Ui on the board"""
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
    # # Testing size detecting small size value
    # board = GameBoard(window, 2, ["#d8de81", "#ffde88"])

    lbls = board.get_lbls()
    print(lbls[1])
    input(">>")
    print(lbls)

    window.mainloop()
