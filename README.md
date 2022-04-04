# 15-Puzzle-Solver

This project is to fulfill Minor Assignment for IF2211 Algorithm Strategies in Bandung Institute of Technology

created with :D by Maria Khelli - 13520115

## How the program solves the puzzle

This program uses branch and bound algorithm with bound or cost function as
```c(i) = f(i) + g(i)``` where f(i) is the level of the node and g(i) is the count of puzzle blocks that are not in the right places.

While the node has not reached 0 cost, the program will push the child of the node onto the priority queue with the head as the node with lowest cost. It will keep repeating to pop and process the node until an answer is found.

When the node has reached 0 cost, it means it has finished. The program will stop and print the result.

## How to run the program

Just do ```py main.py``` and input your filename (with its extension) :)

!! Reminder: if you want to test the program, make sure to change the empty block with the number 16.
