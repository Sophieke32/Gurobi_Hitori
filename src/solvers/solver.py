from abc import ABC, abstractmethod


class Solver(ABC):
    name: str = None
    redundant_constraints: list = None

    @abstractmethod
    def solve(self, n, m):
        pass
