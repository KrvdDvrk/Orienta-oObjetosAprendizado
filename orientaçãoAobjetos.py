# Componentes - 0.0

# Classe `class` - MaterialDeEscritório, Eletrônico, Gadget, Fruta
# Objetos - Instâncias criadas a partir da classe - caneta, relogio, banana
# Atributos - Valores definidos nas classes e nos Objetos
# Método - Funão definida no escopo da classe


# PascalCasem UpperCamelCase
# Red Apple, Green Apple
# -> class red_apple: , o python aceita, mas não é recomendado pela pep8. O certo é:
class RedApple:
    ...


class GreenApple:
    """Green Apple"""


# Ou seja, classe sempre terá seu início com letra maíuscula, e suas seprações também.
# Quando são siglas, todas as letras serão maíusculas, segue exemplo:
class SMTP:
    ...


# Não poderia ser "Smtp"

# Uma classe, nada mais é que um dicionário
# Verificar com -> print(Person.__dict__)


class Person:  # pascalCase, UpperCamelCase
    """Represents a person."""

    company_name = "KrvdDvrk-Corp."  # snake_case
    work_address = "NOM Street, Multipolar World"
    balance = 0

    # snake_case
    def add_points(person, value):  # MÉTODO
        if person.role == "Boss":
            value *= 2
        if person.role == "Iluminnated":
            value *= 1000
        person.balance += value


van = Person()
van.name = "Van Damme"
van.role = "Mercenary"

van.add_points(100)
# Após usar do modo acima, não será mais possível usar o add_pints como:
# add_points(van, 100)
# Vai dar erro, pois agora ela está dentro de um namespace diferente, que é o namespace do objeto.

print(id(van))
print(van.company_name)
print(van.name)
print(van.balance)

print("-------" * 10)

nico = Person()
nico.name = "Nicolas Cage"
nico.role = "Boss"
nico.add_points(100)
print(id(nico))
print(nico.company_name)
print(nico.name)
print(nico.balance)

print("-------" * 10)

sam = Person()
sam.name = "Sam Esmail"
sam.role = "Iluminnated"
sam.add_points(100)
print(id(sam))
print(sam.company_name)
print(sam.name)
print(sam.balance)
