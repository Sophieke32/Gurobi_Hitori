from abc import ABC, abstractmethod

class ConnectedChecker(ABC):
    @abstractmethod
    def check(self, n, grid):
        pass