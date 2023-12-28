# ENUMERAÇÃO

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum

# Enumeração / Enumerador

# O primeiro modo pode ser como números:
# class EffectKind(Enum):
#     acid = 0
#     posion = 1
#     toxine = 2


# Mas o melhor modo, quando se tratar de strings é com as próprias strings:
class EffectKind(str, Enum):
    string = "string"
    acid = "acid"
    poison = "poison"
    toxine = "toxine"


@dataclass
class ABSEffect(ABC):
    @abstractmethod
    def play(self):
        ...


@dataclass
class DataEffectMixin:
    inflict: str
    kind: EffectKind


class Effect(DataEffectMixin, ABSEffect):
    ...


@dataclass
class Acid(Effect):
    inflict: str = "Corrosion"
    kind: EffectKind = EffectKind.string

    def play(self):
        return self.inflict


@dataclass
class Poison(Effect):
    inflict: str = "Internal hemorragy"
    kind: EffectKind = EffectKind.string

    def play(self):
        return self.inflict


@dataclass
class Toxine(Effect):
    inflict: str = "Heart Attack"
    kind: EffectKind = EffectKind.string

    def play(self):
        return self.inflict
