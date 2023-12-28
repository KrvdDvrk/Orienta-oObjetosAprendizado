# ABSTRAÇÃO E HERANÇA COM DATACLASS
# BASE

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Effects(ABC):
    @abstractmethod
    def play(self):
        ...


@dataclass
class Acid(Effects):
    inflict: str = "Corrosion"

    def play(self):
        return self.inflict


@dataclass
class Poison(Effects):
    inflict: str = "Internal hemorragy"

    def play(self):
        return self.inflict


@dataclass
class Toxine(Effects):
    inflict: str = "Heart Attack"

    def play(self):
        return self.inflict
