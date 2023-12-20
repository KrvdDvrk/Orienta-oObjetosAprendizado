class Person:
    """Represents a person."""

    company_name = "KrvdDvrk-Corp."
    work_address = "NOM Street, Multipolar World"
    balance = 0
    prefered_colors = []  # Classe mutável
    # Dica: Nunca definir um valor mutável como atributo de classe.
    # Dica: É bom usar, quando é algo que se aplica para todos e não será alterado.
    # Exemplo: Cor do uniforme dos funcionários, de todos são da cor azul.

    def add_points(person, value):
        if person.role == "Boss":
            value *= 2
        if person.role == "Iluminnated":
            value *= 1000
        person.balance += value


# Python segue a seguinte filosofia:
# Consent Adults - Somos adultos e sabemos o que fazemos

van = Person()
van.name = "Van Damme"
van.role = "Mercenary"
van.add_points(100)
# -> van.prefered_colors.append("Blue")
# Com o append, adiciona-se a variável "Blue" no atributo da classe, pois ela é mutável e se
# aplicará a todas instâncias, inclusive se aplicará para nico e sam. Ficando:
# Van Damme 100 ['Blue']
# ----------------------------------------------------------------------
# Nicolas Cage 200 ['Blue']
# ----------------------------------------------------------------------
# Sam Esmail 100000 ['Blue']
#
# Para resolver isso, basta retribuir da maneira correta:
van.prefered_colors = ["Blue"]
print(van.name, van.balance, van.prefered_colors, van.work_address)

print("-------" * 10)

nico = Person()
nico.name = "Nicolas Cage"
nico.role = "Boss"
nico.add_points(100)
# -> nico.prefered_colors.append("Red")
# Fazendo isso, serão cumulados se aplicando as próximas instâncias a partir daqui, ficando:
# Van Damme 100 ['Blue']
# ----------------------------------------------------------------------
# Nicolas Cage 200 ['Blue', 'Red']
# ----------------------------------------------------------------------
# Sam Esmail 100000 ['Blue', 'Red']
#
# Para resolver isso, basta retribuir da maneira correta:
nico.prefered_colors = ["Red"]
nico.work_address = "Home"
# Definindo o work_address só para nico desta forma, para van e sam que não foi denfinido,
# Continuará o work_adress definido inicialmente. Ficando:
# Van Damme 100 ['Blue'] NOM Street, Multipolar World
# ----------------------------------------------------------------------
# Nicolas Cage 200 ['Blue', 'Red'] Home
# ----------------------------------------------------------------------
# Sam Esmail 100000 ['Blue', 'Red'] NOM Street, Multipolar World
print(nico.name, nico.balance, nico.prefered_colors, nico.work_address)

print("-------" * 10)

sam = Person()
sam.name = "Sam Esmail"
sam.role = "Iluminnated"
sam.add_points(100)
sam.prefered_colors = ["Black"]
print(sam.name, sam.balance, sam.prefered_colors, sam.work_address)
