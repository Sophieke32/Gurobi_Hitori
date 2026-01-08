from src.constraints.redundant_constraints.redundant_constraint import RedundantConstraint

class CornerCloseConstraint(RedundantConstraint):

    # Ensures that the corner tiles are never surrounded by two covered tiles
    # This constraint is already encapsulated in the Duplicates model
    def apply(self, board, is_covered, duplicates, n, m, has_duplicates=False):
        m.addConstr(is_covered[0][1] + is_covered[1][0] <= 1)
        m.addConstr(is_covered[-1][1] + is_covered[-2][0] <= 1)
        m.addConstr(is_covered[0][-2] + is_covered[1][-1] <= 1)
        m.addConstr(is_covered[-1][-2] + is_covered[-2][-1] <= 1)
