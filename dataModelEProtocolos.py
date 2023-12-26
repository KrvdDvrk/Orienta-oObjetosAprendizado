# Protocolos / Data vim:set et sw=4 ts=4:

# -------------------------- 0.0 Introdução ----------------------------
print("----" * 10)
print(" INTRODUÇÃO ")
print("----" * 10)

# Independente de qual tipo de objeto estamos imprimindo.
# O python consegue imprimir a represetnação desse objeto na tela:


# obj = 1
# obj = "KrvdDvrk"
# obj = (1, 2, 3)
# obj = [(1, 2, 3), 1, {"a": "b"}]
# obj = int
obj = "Hello World!!"

print(obj)  # Printable -> __str__

# Printable: É o protocolo que vai estar ligado a todos os objetos que
# Implementam o módulo chamado __str__.
# Para vizualizar os módulos contidos no "obj", desmarque o comando abaixo
# print(dir(obj))
print()

# ------------------- 1.0 Printable Protocol -------------------------
print("----" * 10)
print(" PRINTABLE PROTOCOL ")
print("----" * 10)

# Cria-se primeiro a:
# Base Class
# Ou seja, a classe de base.


class Mage:  # Base Class
    power = "magic"
    name = "unknown"

    def dead(self):
        return "DEAD"

    def alive(self):
        return "ALIVE"

    def __str__(self):
        return f"{self.power} - {self.name}"


# FUNÇÃO DE REPRESENTAÇÃO:
#
#    def __repr__(self):  # Função de representação
#        return f"'<Power object ar memory position {id(self)}'"
# Também poderia ser:
#       return "'123'"
#       return"'Pode ser o que você quiser colocar aqui'"
# Sem essa função, ao imprimir:
# -> print(Mage())
# Imprimiria:
# <__main__.Mage object at 0x7f7847832870>

# FUNÇÃO DE SUBSTITUIÇÃO COM O __str__
# Aqui ocorrerá a substituição da impressão do objeto puro:
# <__main__.Mage object at 0x7f7847832870>
# Pelo objeto desejado
# Ou seja ao imprimir:
# -> print(Fire())
# Não mais imprimirá:
# <__main__.Fire object at 0x7f87627367b0>
# E  sim:
# Fire

# Em seguida as sub-classes.


class Water(Mage):
    power = "Water"
    name = "Zynet Sparks", "Bradly Line", "Colterlyn Yamark"

    def __len__(self):
        return 250


class Fire(Mage):
    power = "Fire"
    name = "The Unnamed"

    def __len__(self):
        return 1000


class Air(Mage):
    power = "Air"
    name = "Cetroly Limyard"

    def __len__(self):
        return 500


print("Magos residentes em Dynafall: ")
print()
print(Water())
print(Fire())
print(Air())
print()

# ------------------- 2.0 Addible Protocol ---------------------
print("----" * 10)
print(" ADDIBLE PROTOCOL ")
print("----" * 10)

# Modo mais simples de entender o addible:
# -> print(1 + 2)
# -> print("Krvd" + "Dvrk")
# -> print([1, 2, 3] + [4, 5, 6])

# O addible tem dois módulos principais:
# O __add__ e o __radd__.
# O primeiro atua no objeto que está na esquerda e o segundo no da direita.
# Exemplo:
# -> print(1 .__add__(2)), é a mesma coisa que print(1 + 2).


class Hunters:
    def dead(self):
        return "DEAD"

    def alive(self):
        return "ALIVE"

    def __str__(self):
        return self.role

    def __add__(self, other):
        mixtable = [
            ((Monster, Peoples), Killer),
            ((Peoples, Treasures), Elitekiller),
            ((Monster, Treasures), Pirate),
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Monster(Hunters):
    role = "Heavy"

    def __len__(self):
        return 80


class Peoples(Hunters):
    role = "Assassin"

    def __len__(self):
        return 50


class Treasures(Hunters):
    role = "Bounty"

    def __len__(self):
        return 40


class Killer(Hunters):
    role = "Killer of any living being"

    def __len__(self):
        return 880


class Elitekiller(Hunters):
    role = "Politician and richies killer"

    def __len__(self):
        return 230


class Pirate(Hunters):
    role = "Pirate of earth and sea"

    def __len__(self):
        return 300


print("Os caçadores disponíveis para contratação são: ")
# print(Monster())
# print(Peoples())
# print(Treasures())

# Outra forma de imprimir:
heavy = Monster()
assassin = Peoples()
bounty = Treasures()
print()
print(heavy, assassin, bounty)
print()
print("Esses que vou apresentar agora são especiais e atendem a duas funções: ")
# -> print(heavy + assassin)    # python tem a TIPAGEM FORTE o que dará erro.
# Ou seja é necessário fazer a função "def __add__ ..."
#     def __add__(self, other):
#        return Killer()
# Com a função definida, será possível então imprimir:
# -> print("Heavy + Assassin:", heavy + assassin)
# -> print("Assassin + Bounty:", assassin + bounty)
# -> print("Heavy + Bounty:", heavy + bounty)
# Porém todas darão o mesmo resultado:
# Heavy + Assassin: Killer of any living being
# Assassin + Bounty: Killer of any living being
# Heavy + Bounty: Killer of any living being
# Por isso será necessário fazer a função com o MIXTABLE.
print()
print("Heavy + Assassin:", heavy + assassin)
print("Assassin + Bounty:", assassin + bounty)
print("Heavy + Bounty:", heavy + bounty)
print()

# ---------------------- 3.0 Iterable Protocol --------------------
print("----" * 10)
print(" ITERABLE PROTOCOL ")
print("----" * 10)

# Iterable - __iter__i
# Exemplo mais simples:
#
# nome = "Krvd"
# for letra in nome:
#   print(letra)
#
# print(list(nome))


class Clan:
    def __init__(self, *members):
        self._members = members

    def __len__(self):
        return len(self._members)

    def __iter__(self):
        return iter([hunters for hunters in self._members])

    def __contains__(self, check):
        return check in [hunters.role for hunters in self._members]

    def __getitem__(self, check):
        return self._members[check]


sonsofapocalypse = Clan(Monster(), Killer(), Elitekiller(), Pirate(), Treasures())
# -> print(sonsofapocalypse._members)
# Mostrará apenas as classes.
# Para imprimir corretamente será necessário criar a função __iter__.

print(
    "Kyrthon, o senhor das ilhas das sombras, então contratou cinco caçadores",
    "e formou o clã Sons of Apocalypse, com o objetivo de destruir Dynafall.",
)
print("Dentre os membros do clã além de Kyrthon estão: ")
print()
for hunters in sonsofapocalypse:
    print(hunters)
print()

# ----------------- 4.0 Container Protocol --------------------------
print("----" * 10)
print(" CONTAINER PROTOCOL ")
print("----" * 10)

# Container -> __contains__ -> Retorna bool

# O que seria um container?
# Eu gostaria de ser capaz de verificar se existe um hunter dentro do clã.
# Modo mais simples de entender:
# -> print("Heavy" in sonsofapocalypse)
# True, Heavy está dentro do clã.

# iniciando, função com __contains__ na linha 201

print(
    "The unnamed, não só um grande mago, mas também um grande investigador, "
    "ao ouvir rumores sobre o surgimento do clã Sons of Apocalypse, decidiu "
    "ir atrás de informações. Chegando em Gudar, o homem que tudo sabia e seu "
    "principal informante. Perguntou."
)
print("Há algum Heavy nesse clã? E Gudar respondeu:")
print("Heavy" in sonsofapocalypse)

print("Há algum Assassin nesse clã? E Gudar respondeu:")
print("Assassin" in sonsofapocalypse)

print("Há algum Killer of any living being nesse clã? E Gudar respondeu:")
print("Killer of any living being" in sonsofapocalypse)

print("Há algum Bounty nesse clã? E Gudar respondeu:")
print("Bounty" in sonsofapocalypse)
print()

# ----------------- 5.0 Sized Protocol --------------------------
print("----" * 10)
print(" SIZED PROTOCOL ")
print("----" * 10)

# Sized

# Simplesmente retorna o tamanho de alguma variável, conjunto, atributo, etc.

clanchief = "Kyrthon"

print(
    "Gudar então indagou The Unnamed, perguntando se ele estava afim de uma "
    "informação quente, o número de letras que continha o nome do líder do "
    "clã."
)
print("The unnamed, retirou cem moedas de prata e entregou a Gudar, que disse: ")
print()
print(len(clanchief))
print()

# É possível também quebrar a estrutura de contagem de caracteres por exemplo
# Para atribuir um valor manual e usá-lo para outra finalidade
# Que será através de uma função, como:
#    def __len__(self):
#       return ...

print(
    "The unnamed, então só precisava de mais uma informação, saber qual era "
    "o nível de poder de cada integrante do clã. No entanto, Gudar disse que "
    "só poderia informar o nível de poder de cada membro, se não informasse "
    "o nome do hunter a quem pertencia tal nível, e claro, sem informar também"
    " o nível de poder do líder deles. "
    "The unnamed concordou e ouviu atentamente Gudar dizer:"
)
print()
for hunters in sonsofapocalypse:
    print(len(hunters))

print()

# ----------------- 6.0 Collections Protocol --------------------------
print("----" * 10)
print(" COLLECTIONS PROTOCOL ")
print("----" * 10)

# Super Protocolo
# Collection - Sized + Container + Iterable

# Um exemplo mostrado anteriormente no código de uma collection é o Clan:
# class Clan:
#     def __init__(self, *members):
#         self._members = members
#
#     def __len__(self):
#         return len(self._members)
#
#     def __iter__(self):
#         return iter([hunters for hunters in self._members])
#
#     def __contains__(self, check):
#         return check in [hunters.role for hunters in self._members]


print(
    "The Unnamed então com as informações que tinha a respeito do clã, foi ao "
    "encontro do grande Oráculo. E para ele disse as seguintes informações: "
)
print("'O número de membros no clã com exceção do líder é: '")
print()
print(len(sonsofapocalypse))
print()
print("'Os hunters que descobri até agora são: '")
print()
print(Monster(), ",", Killer(), "and", Treasures())
print()
print("O Oráculo o interrompeu, dizendo que são: ")
print()
for hunters in sonsofapocalypse:
    print(hunters)
print()
print("The unnamed, continuou dizendo:")
print("'Não conseguirei definir a quem exatamente pertence, mas o nível de poder deles são: '")
print()
for hunters in sonsofapocalypse:
    print(len(hunters))
print()
print("O Oráculo então disse:")
print()
for hunters in sonsofapocalypse:
    print(hunters, len(hunters))
print()
print("The Unnamed finalizou dizendo sua última informação:")
print("'E a quantidade de letras que possui o nome do líder deles é:'")
print()
print(len(clanchief))
print()
print("E mais um vez o Oráculo completou dizendo: ")
print()
print(clanchief)
print()

# ----------------- 7.0 Subscriptable Protocol --------------------------
print("----" * 10)
print(" SUBSCRIPTABLE PROTOCOL ")
print("----" * 10)

# Subscriptable - __getitem__
# Subscrever para pegar um item

# Modo mais simples é através das listas.
# Exemplo:
# name = ["Krvd", "Dvrk"]
# print(name[0]) -> Imprimirá "Krvd"
# print(name[1]) -> Imprimirá "Dvrk"
# Com dicionários também:
# nome = {"id": "Krvd", "last_id": "Dvrk"}
# print(nome["id"]) -> Imprimirá "Krvd"

# No exemplo em questão o método Subscriptable será utilizado com a
# Função:
# def __getitem__


class Dynafallclan:
    def __init__(self, *members):
        self._members = members

    def __len__(self):
        return len(self._members)

    def __iter__(self):
        return iter([mage for mage in self._members])

    def __contains__(self, check):
        return check in [mage.name for mage in self._members]

    def __getitem__(self, check):
        return self._members[check]


dynafallheroes = Dynafallclan(Water(), Air(), Fire())

print(
    "O Oráculo perguntou a The Unnamed, quem iria confrontar os Sons of Apocalypse, "
    "e The Unnamed respondeu que seria o seu clã, The Dynafall Heroes. Então o Oráculo "
    "perguntou a classe, o nome e o nível de poder de cada um do clã. The Unnamed respondeu:"
)
print()
for mage in dynafallheroes:
    print(mage, len(mage))

print()
print("O Oráculo então disse: ")
print("'A vitória de vocês é impossível já que o nível do poder de Kyrthon é 1845.'")
print("The Unnamed responde: ")
print("'Deve haver um jeito e se não houver, ainda assim, lutaremos até a morte'")
print("O Oráculo diz: ")
print("'Sim, há um jeito mas o preço é alto'")
print("'Estou disposto a qualquer coisa' responde, The Unnamed.")
print("O Oráculo então lhe diz: ")
print(
    "'Eu consigo através de um sacrifício de carne, sangue e alma, destruir o líder "
    "Kyrthon e mais um dos hunters, sobrando apenas três dos membros do Sons of "
    "Apocalypse para enfrentar a batalha.'"
)
print("'Entendi', responde The unnamed surpreso e em choque.")
print("'Qual a sua resposta?' Pergunta o Oráculo.")
print("'Aceito', exclama The Unnamed.")
print(
    "O Oráculo então, pede qual dos hunters do Sons of Apocalypse será destruído junto a Kyrthon."
)
print("The Unnamed responde:")
print()
print(sonsofapocalypse[1])
print()
print("O Oráculo agora pergunta: ")
print("'E o sacrifício do seu clã, quem será?'")
print("The Unnamed engole seco, e responde firmemente:")
print()
print(dynafallheroes[2])
print()


# ----------------- 8.0 Creating protocols --------------------------
print("----" * 10)
print(" CREATING PROTOCOLS ")
print("----" * 10)


# É possível também criar seu próprio protocolo e implementá-lo.


def dead(person):  # Deadble?
    if not hasattr(person, "dead"):
        raise TypeError("Is alive")
    print(person.dead())


def alive(person):  # Aliveble?
    if not hasattr(person, "alive"):
        raise TypeError("Is dead")
    print(person.alive())


print(
    "Após intensas batalhas e o honroso sacrifício de The Unnamed, Kyrthon e seu ",
    "clã Sons of Apocalypse, foram completamente derrotados. A cidade de Dynafall ",
    "agora precisa de tempo para se estabilizar e reconstruir tudo o que foi destruído.",
)
print(
    "O mensageiro da cidade, no meio do povo reunido, começa a dizer em voz alta, a "
    "situação em que se encontram os heróis de Dynafall e seus inimigos:"
)

print()
print("'Do clã Sons of Apocalypse:'")
print("'Heavy:'")
dead(Monster())
print("'Killer of any living being:'")
dead(Killer())
print("'Politician and richies killer:'")
dead(Elitekiller())
print("'Pirate of the earth and sea:'")
dead(Pirate())
print("'Bounty:'")
dead(Treasures())
print("'And The Lord of the Shadow Island:'")
print("DEAD")
print()
print("'Do clã The Dynafall Heroes:'")
print("'Water - Zynet Sparks:'")
dead(Water())
print("'Water - Bradly Line:'")
alive(Water())
print("'Water - Colterlyn Yamark:'")
alive(Water())
print("'Air - Cetroly Limyard:'")
alive(Air())
print("'Fire - The Unnamed:'")
dead(Fire())


# ----------------- END --------------------------
print("----" * 10)
print(" END ")
print("----" * 10)

# Esses são apenas os principais protocolos utilizados
# Há muitos outros
# Para aprofundar melhor no estudo, consultar:
# https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes

# Outros atributos:

# __new__    :  Construtor chamado antes de criar a instância
# __init__   :  Inicializador chamado após a instância ser criada
# __init_subclass__  :  Inicializador de subclasses
# __repr__  :  Imprime uma representação em string
# __str__  :  Chama __repr__ por padrão
# __setattr__  :  Executando sempre que atribuimos com obj.name
# __getattr__  :  Executado quando acessamos obj.name
# __delattr__  :  Executado quando apagamos como "del obj.name"
# __getattribute__  :  Executado quando um atributo não é encontrado
# __dir__  :  Lista todos os atributos e métodos
