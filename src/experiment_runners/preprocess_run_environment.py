import os

from src.experiment_runners.run_environment import RunEnvironment

class PreprocessRunEnvironment(RunEnvironment):
    solver = None
    time_out = 10
    path = None
    number_of_runs = 100

    def __init__(self, solver, time_out=10, root="", number_of_runs=100):
        self.solver = solver
        self.time_out = time_out
        self.path = os.path.join(root)
        self.number_of_runs = number_of_runs


    def run_puzzle(self, n, board, file, **kwargs):
        aggregate = []

        for i in range(self.number_of_runs):
            aggregate.append(self.solver.solve(n, board))

        means = {}
        for i in range(len(aggregate)):
            for key, value in aggregate[i].items():
                if key in means:
                    means[key] += value
                else:
                    means[key] = value

        for key, value in means.items():
            means[key] /= self.number_of_runs

        # with open(os.path.join(self.path, file), "a") as f:
            # f.write("\n# Number of iterations: " + str(int(means["iterations"])))
            # f.write("\n# Time spent on illegal solutions (s): " + str(means["time spent on iterations"]))

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
            for i in range(11):
                lines.append(f.readline())
        with open(os.path.join(self.path, file), "w") as f:
            f.write(str(n) + "\n\n")

            for line in lines:
                f.write(line)

            f.write("# Number of iterations: " + str(int(means["iterations"])))
            f.write("\n# Time spent on illegal solutions (s): " + str(means["time spent on iterations"]))

            # f.write("# Number of covered tiles: " + str(int(means["number_of_covered_tiles"])))
            # f.write("\n# Number of duplicates: " + str(int(means["number_of_duplicates"])))
            # f.write("\n# Number of cycles: " + str(int(means["number_of_cycles"])))
            # f.write("\n# Corner-checks hits: " + str(int(means["corner_check_hits"])))
            # f.write("\n# Edge-pairs hits: " + str(int(means["edge_pairs_hits"])))
            # f.write("\n# Pair-isolation hits: " + str(int(means["pairs_isolation_hits"])))
            # f.write("\n# Sandwich-pair hits: " + str(int(means["sandwich_pairs_hits"])))
            # f.write("\n# Sandwich-triple hits: " + str(int(means["sandwich_triple_hits"])))
            # f.write("\n# Time spent making duplicates array (s): " + str(means["duplicates_time"]))
            # f.write("\n# Time spent making graph (s): " + str(means["graph_time"]))
            # f.write("\n# Number of runs to collect time data: " + str(self.number_of_runs))

        return 0
