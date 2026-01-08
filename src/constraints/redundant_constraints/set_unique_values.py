from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint


class SetUniqueValuesConstraint(RedundantConstraint):
    def apply(self, board, is_covered, duplicates, n, m, has_duplicates=False):
        for i in range(n):
            for j in range(n):
                if duplicates[i][j] == 0:
                    m.addConstr(is_covered[i][j] == 0)