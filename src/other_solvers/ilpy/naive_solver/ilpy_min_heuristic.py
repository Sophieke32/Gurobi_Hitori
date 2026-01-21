from src.heuristics.heuristic import Heuristic


class IlpyMinHeuristic(Heuristic):

    def apply(self, n, is_covered, m):
        expr = is_covered[0][0]

        for i in range(n):
            for j in range(n):
                expr += is_covered[i][j]

        expr -= is_covered[0][0]
        m.minimize(expr)
