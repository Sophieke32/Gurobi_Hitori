# Ensures that the corner tiles are never surrounded by two covered tiles
# This constraint is already encapsulated in the Duplicates model
def corner_close(is_black, n, m):
    m.addConstr(is_black[0][1] + is_black[1][0] <= 1)
    m.addConstr(is_black[-1][1] + is_black[-2][0] <= 1)
    m.addConstr(is_black[0][-2] + is_black[1][-1] <= 1)
    m.addConstr(is_black[-1][-2] + is_black[-2][-1] <= 1)
