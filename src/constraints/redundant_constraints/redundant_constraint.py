from abc import ABC, abstractmethod


class RedundantConstraint(ABC):
    @abstractmethod
    def apply(self, board, is_covered, duplicates, n, m, has_duplicates=False):
        pass
