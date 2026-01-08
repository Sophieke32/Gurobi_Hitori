from abc import ABC, abstractmethod

class Heuristic(ABC):
    @abstractmethod
    def apply(self, n, is_covered, m):
        pass
