from src.utils import EMPTY
import numpy as np


class Board:
    """
        This class is the representation of the puzzle.
        The class stores the array (board) and the block index
        which is empty. Hence, the program need not to iterate
        everytime it need to know where is the empty block.
    """

    def __init__(self, array, empty, cost):
        self.array = array
        self.empty = empty
        self.cost = cost
        if not (cost):
            _ = self.calc_cost()

        self.str = ""

    def is_index_valid(self, i, j):
        """
            Returns true if index is not out of bound.
        """
        return (0 <= i < 4) and (0 <= j < 4)

    def to_xy(self, i):
        """
            Convert array index to matrix index.
        """
        return (i // 4, i % 4)

    def wrong_pos(self, array, i):
        return array[i] != i + 1

    def calc_cost(self):
        """
            Count the blocks that are not in position.
        """

        if not (self.cost):
            total = 0
            for i in range(len(self.array)):
                if self.array[i] != EMPTY and (self.wrong_pos(self.array, i)):
                    total += 1

                self.cost = total

        return self.cost

    def move(self, to):
        """
            Generating a child class if the direction is valid.
            Returns None if direction is not valid.
        """

        i = self.empty
        x, y = self.to_xy(to)

        if self.is_index_valid(x, y):
            acopy = np.copy(self.array)
            acopy[i], acopy[to] = acopy[to], EMPTY
            cost = self.cost

            if self.wrong_pos(self.array, to) and not(self.wrong_pos(acopy, i)):
                cost -= 1
            elif not(self.wrong_pos(self.array, to)) and self.wrong_pos(acopy, i):
                cost += 1

            return Board(acopy, to, cost)
        else:
            return None

    def from_right(self):
        return self.move(self.empty + 1)

    def from_left(self):
        return self.move(self.empty - 1)

    def from_up(self):
        return self.move(self.empty - 4)

    def from_down(self):
        return self.move(self.empty + 4)

    def to_string(self):
        """
            Converting the array to string (matrix-like shape).
        """

        if self.str == "":
            self.str = "  "
            for i in range(len(self.array)):
                num = self.array[i]
                if num == EMPTY:
                    self.str += "   "
                else:
                    self.str += str(num).ljust(3, " ")
                self.str += " "

                if (i + 1) % 4 == 0 and i != (len(self.array) - 1):
                    self.str += "\n  "

        return self.str

    def print_board(self):
        print(self.to_string())

    def is_finish(self):
        return self.cost == 0
