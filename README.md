# 8-Puzzle-solver-A-star-algorithm
# 8 Puzzle problem
The goal of this project is to code a solution to the N-puzzle problem by applying the A* search algorithm.
The puzzle consists of N tiles and one blank space where the tiles can be moved. Start and Goal  stateof the puzzle are provided. The puzzle can be solved by moving the tiles  in the single blank space and thus achieving the Goal state.
The empty space can only move in four directions viz.,
1. Up
2. Down
3. Right or
4. Left
# A star algorithm and Heuristic design
A* is a computer algorithm that is widely used in pathfinding and graph traversal, the process of plotting an efficiently traversable path between multiple points, called nodes.
The key feature of the A* algorithm is that it keeps a track of each visited node which helps in ignoring the nodes that are already visited, saving a huge amount of time. The search for an goal node can often be speeded by using a cost function to avoid searching in sub-trees that do not contain an goal node.<br />

Here, the function used is,<br />
F(n) = g(n) + h(n) where<br />
g(n) is the depth of current node and<br />
h(n) is the number of non-blank tiles not in their goal position.
