from enum import Acid, EffectKind, Poison, Toxine

monarchbutterfly = Toxine("Monarch Butterfly", kind=EffectKind.poison)
print(monarchbutterfly.play())
