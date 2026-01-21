from src.heuristics.heuristic import Heuristic


class VarScipOptMinHeuristic():

    def apply(self, n, is_covered, m, that_one_var):
        expr = is_covered[0][0]

        for i in range(n):
            for j in range(n):
                if i == 0 and j == 0: expr += that_one_var
                else: expr += is_covered[i][j]

        expr -= is_covered[0][0]
        m.setObjective(expr, sense="minimize")
