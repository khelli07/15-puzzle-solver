import time
import os

EMPTY = 16
INF = 999
UP = "UP"
RIGHT = "RIGHT"
DOWN = "DOWN"
LEFT = "LEFT"


def find_empty(array):
    for i in array:
        if array[i - 1] == EMPTY:
            return i - 1


def is_solvable(matrix):
    total = 0
    X = -1

    passed = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            passed.append(matrix[i][j])
            if matrix[i][j] == EMPTY:
                X = int((i % 2) + (j % 2) == 1)

            total += matrix[i][j] - 1 - \
                sum([1 for el in passed if el < matrix[i][j]])
    return (total + X) % 2 == 0


def print_steps(root, nodes):
    root.print_node()
    time.sleep(0.5)
    os.system('cls')
    for node in nodes:
        node.print_node()
        time.sleep(0.5)
        os.system('cls')

    return
