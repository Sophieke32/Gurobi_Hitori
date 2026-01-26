# Solving Hitori with Gurobi

The code in this repository is made for a Bachelor thesis. This thesis was done in requirements of the Research Project of 
Computer Science and Engineering at the faculty of Electrical Engineering, Computer Science and mathematics, TU Delft. The paper 
investigates different ways of modelling the Hitori puzzle as an Integer Linear Programming problem, and 
can be found in the TU Delft repository at: https://repository.tudelft.nl/record/uuid:f4abd9b2-904e-49d4-9da5-1304254a3555


## Hitori
Hitori is a logic puzzle in which the player is given an `n` by `n` grid filled with numbers ranging from 
`1` to `n` (inclusive). The goal is to mark tiles such that three conditions hold:
1. Uniqueness: For each unmarked, the value it has is unique in its row and its column.
2. Adjacency: No two marked tiles are orthogonally adjacent
3. Connectivity: All the unmarked tiles are orthogonally connected

## Running the solver
The solver runs through the commandline. You can use 
```commandline
python main.py -d name_of_directory
```
and it will run all .singles files in that directory (and any sub+directories) using the optimised naive model.

There are optional flags to specify what behaviour you want:   
-m allows you to specify a model. Currently, 'duplicates' and 'naive' are available. Default is 'duplicates'.  
-t gives you the option to track the time the model took for all solutions in a csv file. Can be True or False. Default is 'False'  
-a will run all the variations of different solvers, different heuristics, and different redundant constraints. It will always time this.  
-p preprocesses the Hitori files in the directory. This means that it will collect data on the instances and put that in the 
.singles files. If other run environments (such as with the -t flag) do not work, consider first preprocessing the data.  
-c allows you to easily define a custom job to run, but it requires you to write the code for it.   
-n runs and times the three base models on the files in the given directory.   

## Dependencies
This project's dependencies are detailed in the `requirements.txt` file.
