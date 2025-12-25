from abc import ABC, abstractmethod


class RedundantConstraint(ABC):
    @abstractmethod
    def apply(self):
        pass
