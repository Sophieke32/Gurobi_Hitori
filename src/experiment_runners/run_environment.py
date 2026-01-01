from abc import ABC, abstractmethod

from src.solvers.solver import Solver


class RunEnvironment(ABC):
    solver: Solver = None
    time_out = 10
    writer = None

    @abstractmethod
    def run_puzzle(self, n, board, file):
        pass
