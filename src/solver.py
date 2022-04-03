import numpy as np
from heapq import heappop, heappush
from src.board import Board
from src.node import Node
from src.utils import *


def solve(filename):
    f = open("test/" + filename, "r")
    array = [int(i) for i in f.read().strip().split()]
    matrix = np.reshape(array, (4, 4))
    f.close()

    if not (is_solvable(matrix)):
        print("Board can not be solved.")
    else:
        root = Node(
            Board(np.array(array), find_empty(array), None),
            None, 0, "INITIAL"
        )
        heap = []
        heappush(heap, root)

        visited = {}

        answer = None
        node_counter = 1  # ROOT
        processed_counter = 1

        start_time = time.time()
        while not(answer):
            current_node = heappop(heap)
            processed_counter += 1
            visited[current_node.key()] = True

            if current_node.board.is_finish():
                answer = root
                break

            for child in current_node.expand():
                if child.board.is_finish():
                    node_counter += 1
                    answer = child
                    break

                elif child.key() not in visited:
                    node_counter += 1
                    heappush(heap, child)

        total_exec = time.time() - start_time

        # Compute paths and nodes
        paths = []
        nodes = []
        cn = answer
        while cn.steps != 0:
            paths.insert(0, cn.move)
            nodes.insert(0, cn)
            cn = cn.before

        print_steps(root, nodes)

        print("Path:", " -> ".join(paths))
        answer.print_node()
        print("Total node generated:", node_counter)
        print("Total node processed:", processed_counter)
        print("Total solve time: {:.2f} seconds".format(total_exec))
