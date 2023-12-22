# OS 4 PILARES DA ORIENTAÇÃO A OBJETOS PYTHON

# --------------- 1º PILAR = ABSTRAÇÃO -----------------------
print("----" * 10)
print("ABSTRAÇÃO")
print("----" * 10)


class Person:
    kingdom = "animalia"


class Fruta:
    kingdom = "vegetalia"


class Animal:
    kingdom = "animalia"


print("What is the kingdom of a fruit? a animal? a person?")
print("Fruit is:")
print(Fruta.kingdom)
print("Animal is:")
print(Animal.kingdom)
print("Person is:")
print(Person.kingdom)
print()

# Capacidade de abstrair implementações e trazer sentido para o mundo real.


# ---------------- 2º PILAR = HERANÇA --------------------
print("----" * 10)
print("HERANÇA")
print("----" * 10)

# Super Classe


class Fruit:  # Classe abstrata / base
    kingdom = "vegetalia"


# 1º Método, muitas instâncias e não recomendado.
print("----- 1º Método -------")


# Derivadas (sub classe)
class Apple(Fruit):  # Herança em uma classe material
    internal_color = "white"


class RedApple(Apple):
    external_color = "red"


class GreenApple(Apple):
    external_color = "green"


class Rotten(GreenApple):
    internal_color = "yellow and brown"


class Ripe(GreenApple):
    ...


class MinhaMacaQueEstaEmCimaDaMesa(Rotten):
    name = "Green Apple Rotten"


class MinhaMacaMadura(Ripe):
    name = "Green Apple Ripe"


minha_maca = MinhaMacaQueEstaEmCimaDaMesa()
minha_macaM = MinhaMacaMadura()
print("A minha maça que está em cima da mesa é a: ")
print(minha_maca.name)
print("E sua cor externa é: ")
print(minha_maca.external_color)
print("Mas por dentro está: ")
print(minha_maca.internal_color)
print("Ela pertence ao reino: ")
print(minha_maca.kingdom)
print("Por isso preciso ir a feira comprar: ")
print(minha_macaM.name)
print("Pois por fora ela é: ")
print(minha_macaM.external_color)
print("E por dentro: ")
print(minha_macaM.internal_color)
print("Ela pertence ao reino: ")
print(minha_macaM.kingdom)
print()


# 2º Método, mais enxuto e recomendado
print("----- 2º Método -------")


class Apple(Fruit):  # Herança em uma classe material
    def __init__(self, name, internalcolor, externalcolor):
        self.name = name
        self.internalcolor = internalcolor
        self.externalcolor = externalcolor


my_apple = Apple(
    name="Rotten Green Apple", internalcolor=["yellow", "brown"], externalcolor=["green", "black"]
)
tobuy_apple = Apple(name="Ripe Green Apple", internalcolor="white", externalcolor="green")
print("A minha maça que está em cima da mesa é a: ")
print(my_apple.name)
print("E sua cor externa é: ")
print(my_apple.externalcolor)
print("E por dentro está: ")
print(my_apple.internalcolor)
print("Ela pertence ao reino: ")
print(my_apple.kingdom)
print("Por isso preciso ir a feira comprar: ")
print(tobuy_apple.name)
print("Pois por fora ela é: ")
print(tobuy_apple.externalcolor)
print("E por dentro: ")
print(tobuy_apple.internalcolor)
print("Ela pertence ao reino: ")
print(tobuy_apple.kingdom)
print()


# 3º Método, função na super classe que se aplicará a todas as subclasses.
print("----- 3º Método -------")


class Knight:  # Classe abstrata / base
    Function = "War Soldier"

    def __init__(self, name, position, weapon):
        self.name = name
        self.position = position
        self.weapon = weapon


class Swordman(Knight):
    ...


class Axeman(Knight):
    ...


o_sword = Swordman("Julius", "Front", "Long Sword")
o_axe = Axeman("Marcius", "Middle", "Axe")

print("In the battle, the Swordman, called: ")
print(o_sword.name)
print("Fighting in the position: ")
print(o_sword.position)
print("Using a: ")
print(o_sword.weapon)
print("AND")
print("In the battle, the Axeman, called: ")
print(o_axe.name)
print("Fighting in the position: ")
print(o_axe.position)
print("Using a: ")
print(o_axe.weapon)

# ---------------- 3º PILAR = POLIMORFISMO --------------------
print("----" * 10)
print("POLIMORFISMO")
print("----" * 10)

# 00.Introdução

nome = "KrvdDvrk"
print("K" in nome)  # Container -  __contains__

cores = ["red", "green", "blue"]
print("purple" in cores)
print()

# 01.Iniciando


class Chaos:
    def promote(self):
        return "Insanity"


nuclearattack = Chaos()
print(nuclearattack.promote())
print()


# 0.2.Um outro modo de alcançar o mesmo resultado


def print_promote(obj):  # What promove?
    print(obj.promote())  # Implementa promote


print_promote(nuclearattack)
print()

# 03.Outra classe


class Darkness:
    def promote(self):
        return "Fear"


blackout = Darkness()
print_promote(blackout)
print()


# 04.Mensagens de erro


def start_promote(obj):
    if not hasattr(obj, "print_promote"):
        raise TypeError(f"{obj} is not part of the chaos.")
    print(obj.print_promote())


# Take off the "#" bellow, for see error msg on program.
# start_promote(42)


# 05.Duck Typing
# "Se o objeto anda como um pato, parece um pato, faz quack como um pato"
# "Então é um pato!!!"


class DeathOnYourDoor:
    def promote(self):
        return "Din-don!"


print_promote(DeathOnYourDoor())
print()


# Polimorfismo é a capacidade de objetos independente da sua forma, se comportarem de
# maneira igual.


# 06. Modo simplista, estritamente definida e Modo polimófico


def funcao(a, b, c):
    return a + b + c


print(funcao(1, 2, 3))
print(funcao(3, 8, 9))
print(funcao(999, 876, 150))
# -> print(funcao(999, 876, 150, 7239))    / Daria erro, pois não está polimórfico


def funcaopoli(*args):
    ret = 0
    for arg in args:
        ret += arg
    return ret


print(funcaopoli(1, 2, 3))
print(funcaopoli(3, 8, 9))
print(funcaopoli(999, 876, 150))
print(funcaopoli(999, 876, 150, 7239))
print()


# ---------------- 4º PILAR = ENCAPSULAMENTO --------------------
print("----" * 10)
print("ENCAPSULAMENTO")
print("----" * 10)

# É a capacidade de um objeto esconder a sua implementação interna e expor apenas
# o que for conveniente

# 01.Introdução


class Bunker:
    def __init__(self, survivor):
        self.survivor = survivor


bunker = Bunker(survivor="Krvd")

# Atributos em formato de dicionário:
# Para consultar o diretório com os atributos, desmarque o comando abaixo:
# print(dir(bunker))

# O único atributo público é o survivor, e podemos usá-lo da seguinte forma:
print(bunker.survivor)
# Pode através dele trocar o atributo dentro dele:
bunker.survivor = "Dvrk"
print(bunker.survivor)
# Pode trocar também os atributos do __ ... __, utilizando o mesmo esquema.
print()


# 02.Convenção de nomes   / Proteção via encapsulamento


class Shelter:
    _typeOfShelter = "Underground"  # protegido / protected
    __EntryPassword = 842937283  # Privado / private

    def __init__(self, survivor):
        self.survivor = survivor
        self._health = 90  # protegido
        if self._typeOfShelter == "Underground":
            self.percentOfProtection = 100

    def yourhealth(self):
        if self._health < 30:
            print("AVISO: Você está morrendo...")
        return self._health

    def healthupdate(self, value):
        self._health = value

    def remedy(self, value):
        self._health += value


shelter = Shelter(survivor="Krvd")


# É possível observar o "_typeOfShelter" como o único com apenas um undeline.
# Isso significa que ele é um atributo protegido.
# Ele só pode ser usado dentro da sua classe.
# Para consultar o diretório com os atributos, desmarque o comando abaixo:
# print(dir(shelter))

# Fora dela, exemplo:
# shelter._typeOfShelter = 500
# Dessa forma o python aceitará o código, mas nada acontecerá no programa.
# Quem cria o atributo com um underline no início, está deixando uma clara mensagem
# De que esse atributo não deve ser usado, modificado ou substituído por nada.
# Caso queira muito utilizar tal atributo protegido, utilize-o sempre dentro de
# Um método:

# Usando dentro da sua classe:
print("Sobrevivente, seu estado de proteção atual é: ")
print(shelter.percentOfProtection)


# Agora, partindo para o "__EntryPassword".   / Dois underlines apenas no início.
# É um atributo PRIVADO. É um atributo que não será utilizado e também não deve
# Ser acessado de forma alguma, é um nível a mais de proteção.
# Não pode ser acessado, exemplo:
# -> print(shelter.__EntryPassword)     /  Ocorrerá erro.
# Também não é possível atribuir outro valor, exemplo:
# shelter.__EntryPassword = 874813744
# Agora, caso necessário, e se queira forçar e modificar tal atributo, será
# Necessário, utilizar a forma que está no diretório. Ou seja:
# Modo normal que não funcionará:
# shelter.__EntryPassword = 874813744
# Modo que funcionará:
shelter._Shelter__EntryPassword = 743828828348
# Assim alterando
print("Sua nova senha de acesso ao abrigo subterrâneo é: ")
print(shelter._Shelter__EntryPassword)
# O método privado, caiu em desuso.


# Agora dentro de uma função, utilizando o método protegido.
# Da seguinte forma:
# -> print(shelter._health)
# Traria algo, popularmente conhecido como #code smell
# Já que como é uma instância protegida, não deveria ser utilizada como atributo.
# Dessa forma, o mais correto seria criar uma outra função e nessa função trazê-la.
# Que será:

print("Seu estado de saúde atual é: ")
print(shelter.yourhealth())

# E qual seria a vantagem de usar o método protegido e ter todo esse trabalho?
# Quando fazemos o encapsulamento criamos uma camada de controle e de acesso
# Aos nossos atributos. E esse controle permite que façamos algumas coisas como:
#
# def yourhealth(self):      # getter
#   if self._health < 30:
#       print("AVISO: Você está morrendo...")
#   return self._health
#
# É fundamental para fazer validações e verificações.


# E como atualizar os valores dentro de um atributo protegido?
# Da mesma forma acima, uma função.

shelter.healthupdate(25)

print("Atualizando sua saúde, após sua saída a procura de recursos: ")
print("Seu estado de saúde atual é: ")
print(shelter.yourhealth())

# Com outra função de adição é possível adicionar valores ao atributo protegido.

shelter.remedy(50)

print("Vejo que você utilizou o remédio. Atualizando sua saúde.")
print("Seu estado de saúde atual é: ")
print(shelter.yourhealth())
print()


# 03. Propriedades


class SafeHouse:
    _typeOfSafeHouse = "Armored"
    __EntryPassword = 48374738

    def __init__(self, survivor):
        self.survivor = survivor
        self.__food = 5  # privado

    @property  # getter
    def food(self):
        if self.__food < 10 and self.__food > 0:
            print("ALERTA!!! Seu estoque de comida está se esgotando, saia em busca de mais.")
        if self.__food == 0:
            print("EMERGÊNCIA!!! Seu estoque de comida está egostado, saia agora em busca de mais.")
        return self.__food

    @food.setter
    def food(self, value):
        self.__food += value

    @food.deleter
    def food(self):
        self.__food = 0


safeHouse = SafeHouse("Dvrk")

# Para consultar o diretório com os atributos, desmarque o comando abaixo:
# print(dir(safeHouse))

print("Status atual da sua casa: ")
print("Ocupante: ")
print(safeHouse.survivor)
print("Quantidade de comida: ")
# Sem o "@property", o correto seria usar:
# -> print(safeHouse.food())
# No entanto com o "@property", pode usar direto sem os parenteses.
print(safeHouse.food)

# E qual seria a vantagem de usar o @property
# Nesse caso você não conseguiria setar valor algum para o atributo
# Usando por exemplo:
# safeHouse.food = 15
# ou até mesmo forçando:
# safe.House.__food = 15
# Está com um nível a mais de proteção.
# Caso queira setar um valor ao atributo, será necessário:
# Criar um setter.
# Agora sim será possível setar, tanto para adiconar como para diminuir.

# Operações de adição:
safeHouse.food = 25
print("Bem vindo de volta! Como foi lá fora?")
print("Atualizando o seu estoque de comida: ")
print(safeHouse.food)

safeHouse.food = 13
print("Bem vindo de volta! Havia mesmo necessidade de voltar lá fora?")
print("Atualizando o seu estoque de comida: ")
print(safeHouse.food)

# Operações de diminuição:
safeHouse.food = -20
print("Já se passou uma semana, vou verificar o seu estoque de comida.")
print("Atualizando o seu estoque de comida: ")
print(safeHouse.food)

# Para deletar todo o conteúdo do atributo usa-se o @deleter

del safeHouse.food
print("Já faz um bom tempo que você não se alimenta, vou verificar seu estoque.")
print("Atualizando o seu estoque de comida: ")
print(safeHouse.food)


# --------------- RESUMO -------------------------------
print("----" * 10)
print("RESUMO")
print("----" * 10)
print("Abstração: Capacidade de abstrair implementações.")
print("Herança: Capacidade de herdar de outras classes.")
print(
    "Polimorfismo: Capacidade de uma implementação se comportar de maneira similar,"
    "independente da forma do objeto."
)
print(
    "Encapsulamento: É a capacidade de um objeto esconder a sua implementação"
    " interna e expor apenas o que for conveniente. Ou proteger esse objeto"
)
