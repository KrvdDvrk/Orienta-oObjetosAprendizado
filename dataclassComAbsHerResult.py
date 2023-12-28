# ABSTRAÇÃO E HERANÇA COM DATACLASS
# RESULTADO

from dataclassComAbstraçãoHerança import Acid, Poison, Toxine

print("-----" * 10)
print("ABSTRAÇÃO E HERANÇA COM DATACLASS")
print("-----" * 10)


komododragon = Acid()
print(komododragon.play())


blackmamba = Poison()
print(blackmamba.play())

monarchbutterfly = Toxine()
print(monarchbutterfly.play())
