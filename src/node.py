from src.utils import UP, RIGHT, DOWN, LEFT


class Node:
    """
        Node class is used to generate state space tree.
        It stores its parent's node and how many steps or level 
        it has gone through (important to find the total cost).
    """

    def __init__(self, board, before, steps, move):
        self.board = board
        self.before = before

        self.steps = steps
        self.move = move

    def cost(self):
        """
            Cost function g(i) + f(i)
        """
        return self.board.calc_cost() + self.steps

    def __lt__(self, other):
        """
            Overriding comparison for the heap to work.
        """
        return self.cost() <= other.cost()

    def key(self):
        """
            Convert node to string (raw) to be used in dictionary key.
        """
        return self.board.array.tobytes()

    def expand(self):
        """
            Generating valid child nodes.
        """
        all_possible_children = [
            (self.board.from_up(), UP),
            (self.board.from_right(), RIGHT),
            (self.board.from_down(), DOWN),
            (self.board.from_left(), LEFT),
        ]

        return [Node(child, self, self.steps + 1, move)
                for child, move in all_possible_children if child]

    def print_node(self):
        print("MOVE = " + self.move + ", COST = " + str(self.steps))
        print("==================")
        self.board.print_board()
        print("==================")
