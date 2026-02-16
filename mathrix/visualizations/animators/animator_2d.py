from abc import ABC, abstractmethod

from mathrix import Vector, Matrix


class BaseAnimator2D(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def plot_vectors(self, )
