# Solving Hitori
_This repo is currently still under development._ 

The code in this repository is made for a Bachelor thesis. It investigates different ways of modeling the Hitori problem as
an Integer Linear Programming problem.

## Hitori
Hitori is a logic puzzle in which the player is given an `n` by `n` grid filled with numbers ranging from 
`1` to `n` (inclusive). The goal is to black out squares such that three conditions hold:
1. For each white square, the value it has is unique in its row and its column.
2. No two black squares are orthogonally adjacent
3. All the white squares are connected through one orthogonal path

## Running the solver
The solver runs through the commandline. You can use 
```commandline
python main.py -d name_of_directory
```
and it will run all .singles files in that directory (and any sub+directories). Note that for each directory with a given name xyz
that contains singles files the programme expects another directory xyz_solutions where it can put solutions to the puzzles. 

There are another two optional flags: 
-m allows you to specify a model. Currently, 'duplicates' and 'naive' are available. Default is 'duplicates'.
-t gives you the option to track the time the model took for all solutions in a csv file. Can be True or False. Default is 'False'

## Dependencies
This project's dependencies are detailed in the `requirements.txt` file. Downloading the following using pip should cover them as well:
- numpy
- gurobipy (version 12.0.3)
- networkx
- colorama (only for pretty printing)
- matplotlib (only for visualising the graphs built in the duplicates_constraint solver)
- pandas (only for the solution checker)
