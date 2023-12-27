# ---------------- Type Annotations ----------------
print("--------" * 10)
print("TYPE ANNOTATIONS")
print("--------" * 10)


from decimal import Decimal

# É fundamental utilizar o decimal ao invés do float em finanças no python.
# Pois o float pode dar resultados com pequenas variações de centavos.
# O que resultará em um resultado não preciso do desejado.

print("Welcome to Black Market \n")

armas = ["Ak-47", "Famas", "BarretM82", "QBZ191", "AKM"]
valorak47 = Decimal(56000.00)
valorfamas = Decimal(43000.00)
valorm82 = Decimal(345000.00)
valorqbz = Decimal(46000.00)
valorakm = Decimal(58000.00)

qntak47 = 38
qntfamas = 12
qntm82 = 4
qntqbz = 56
qntakm = 12

special_client = True


def calcula_totalak47(valorak47: Decimal, qntak47: int) -> Decimal:
    return valorak47 * qntak47


if special_client:
    valorak47 = 40000.00  # BUG // float

total = calcula_totalak47(valorak47, qntak47)


print("Tipo:", type(total))
print(f"O total é R${total:.2f}")

# Primeiramente aqui vemos um erro, um BUG, pois o resultado final será um float.
# Aqui que entra o porque de usar o Type Annotations.
# Fique claro, que ele não é um elemento que alterará nada no código, pois o python
# Obedece a filosofia "duck typing", ou seja, mesmo que você defina:
# valorak47: Decimal e qntak47: int
# Se eu quiser colocar uma str na valorak47, o python aceitará e imprimirá o str.
# Então para o que serviria o Type Annotations?
# Por mera convenção, de uso exclusivo do programador, é como se fosse uma
# Anotação ou instrução. Em casos de bugs como o visto acima, seria preciso apenas
# Ler as Type Annotations da função calcula_totalak47, e veria que o valorak47 recebeu
# Recebeu uma instrução e precisa ser um Decimal e não um float, concertando apenas isso,
# Resolveria o BUG.
# Type Annotations, vêm também da filosofia do python "Somos adultos e sabemos o que
# Estamos fazendo."
# ---------------------------------------------------------------------------
# Modo mais simples de entender a Type Annotations:
#
# def soma(a: int, b: int) -> int:
#    return a + b
#
# print(soma(1, 2))
# print(soma("Krvd", "Dvrk"))
# print(soma([1, 2, 3], [4, 5, 6]))
#
# O python imprimirá todos normalmente, tanto o str como a lista.
# O que importa aqui é que o programador que estiver fazendo isso com uma str ou lista
# Está fazendo isso errado, vindo a ocasionar erros no código futuramente.
# ---------------------------------------------------------------------------
# Através de uma ferramenta externa do python é possível verificar esses erros
# De acordo com as Type Annotations, o que torna essa ferramenta ainda mais útil.
# Instale:
# -> pip install mypy
# E para executar e ver o erro dentro do seu arquivo no terminal, use:
# -> mypy typeAnnotationEDataclasses.py
# Verá que ele lhe mostrará exatamente o erro, na linha 36.
# Com essa ferramenta você pode verificar se há erros no código baseado no que
# Recomendava as Type Annotations.
# Fica claro que no código quando executado o programa, ele irá imprimir normalmente,
# Sem erros, graças ao "Duck Typing". No entanto, é uma ferramente externa para
# Verificar erros baseados nos seus Type Annotations, apenas.
# ----------------------------------------------------------------------------
# Corrigindo o problema. Ao chegar aqui marque com # as linhas:
# 35 a 42.
# E desmarque todas abaixo.
#
# if special_client:
#     valorak47 = Decimal(40000.00)
#
# total = calcula_totalak47(valorak47, qntak47)
#
# print("Tipo:", type(total))
# print(f"O total é R${total:.2f}")
#
# No terminal, confirme que não haverá erros:
# -> mypy typeAnnotationEDataclasses.py

# ---------------- Dataclasses ----------------
print("--------" * 10)
print("DATACLASSES")
print("--------" * 10)

# Função sem dataclass seria:
# class Monster:
#     def __init__(self, race: str, name: str, power: int):
#         self.race = race
#         self.name = name
#         self.power = power

# Com a dataclass:

from dataclasses import dataclass


@dataclass
class Monster:
    race: str
    name: str
    power: int


# Poderia colocar um valor default também, como exemplo:
# power: int = 100


def funcao(dados: Monster):
    ...


dados = Monster(race="Dragon", name="Cronith", power="35000")

print(dados.name)

funcao(dados)
