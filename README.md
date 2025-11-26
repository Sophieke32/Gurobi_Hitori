# Solving Hitori
_This repo is currently still under development._ 

The code in this repository is made for a BSc thesis. It investigates different ways of modeling the Hitori problem when
using Integer Linear Programming to solve it.

## Hitori
Hitori is a logic puzzle in which the player is given an $n$ x $n$ grid filled with numbers ranging from 1 to $n$ (inclusive).
The goal is to black out squares such that three conditions hold:
1. For each white square, the value it has is unique in its row and its column.
2. No two black squares are orthogonally adjacent
3. All the white squares are connected through one orthogonal path

## Running the solver
Running main.py in the root folder will run the solver. In src/main.py there is an open() statement which determines what
.singles file to run. 

## Dependencies
Currently this repository uses the following dependencies:
- numpy
- gurobipy (version 12.0.3)
- networkx
- colorama (only for pretty printing)
- matplotlib (only for visualising the graphs built in the duplicates_constraint solver)
- panda (only for the solution checker)
