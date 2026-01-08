import os

from src.experiment_runners.run_environment import RunEnvironment


class PreprocessRunEnvironment(RunEnvironment):
    solver = None
    time_out = 10
    path = None

    def __init__(self, solver, time_out=10, root=""):
        self.solver = solver
        self.time_out = time_out
        self.path = os.path.join(root)


    def run_puzzle(self, n, board, file, **kwargs):

        data = self.solver.solve(n, board)
        # number_of_cycles, number_of_covered_tiles, number_of_non_uniques = self.solver.solve(n, board)

        # Rewrite the file
        lines = []

        with open(os.path.join(self.path, file), "r") as f:
            n = int(f.readline())
            f.readline()

            for i in range(n):
                lines.append(f.readline())

            f.readline()
            lines.append("\n")
            lines.append(f.readline())
        with open(os.path.join(self.path, file), "w") as f:
            f.write(str(n) + "\n\n")

            for line in lines:
                f.write(line)

            f.write("# Number of covered tiles: " + str(data["number_of_covered_tiles"]))
            f.write("\n# Number of duplicates: " + str(data["number_of_duplicates"]))
            f.write("\n# Number of cycles: " + str(data["number_of_cycles"]))
            f.write("\n# Corner-checks hits: " + str(data["corner_check_hits"]))
            f.write("\n# Edge-pairs hits: " + str(data["edge_pairs_hits"]))
            f.write("\n# Pair-isolation hits: " + str(data["pairs_isolation_hits"]))
            f.write("\n# Sandwich-pair hits: " + str(data["sandwich_pairs_hits"]))
            f.write("\n# Sandwich-triple hits: " + str(data["sandwich_triple_hits"]))

        return 0
