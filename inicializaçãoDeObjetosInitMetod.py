class Person:
    """Represents a person."""

    company_name = "KrvdDvrk-Corp."
    work_address = "NOM Street, Multipolar World"
    balance = 0

    # Injeção de argumento - 1º arg metodo = a própria instancia

    # 1.0 - print("Inicializando o objeto")
    # 1.0 - Método de primeiro argumento em cada objeto
    # 2.0 - self.name = name / self.role = role
    # 2.0 - Pode-se usar agora no próprio () do person o name e o role, pois seguirá
    # 2.0 - A seguinte estrutura:
    # 2.0 - -> van = Person()  -> __init__ (inicializador da classe)
    # 2.0 - Não necessitando mais de "van.name", isso pode se aplicar a todos os outros.
    # 2.0 - Pode ser usado como nomeado:
    # 2.0 - -> van = Person(name="Van Damme", role="Mercenary")
    # 2.0 - Ou usado pela ordem: (visto a ordem 1º self, 2º name, 3º role)
    # 2.0 - -> van = Person("Van Damme", "Mercenary")
    def __init__(self, name, role="Undefined", prefered_colors=None):
        print("Inicializando o objeto")
        self.name = name
        self.role = role
        self.prefered_colors = prefered_colors or []
        # É uma forma resumida e será o mesmo que a seguinte função:
        # -> if prefered_colors:
        # ->    self.prefered_colors = prefered_colors
        # -> else:
        # ->    self.prefered_colors = []

    def add_points(self, value):
        if self.role == "Boss":
            value *= 2
        if self.role == "Iluminnated":
            value *= 1000
        self.balance += value


van = Person(name="Van Damme", role="Mercenary", prefered_colors=["Blue"])
van.add_points(100)
print(van.name, van.balance, van.prefered_colors, van.work_address, van.role)

print("-------" * 10)

nico = Person("Nicolas Cage", "Boss", ["Red"])
nico.add_points(100)
nico.work_address = "Home"
print(nico.name, nico.balance, nico.prefered_colors, nico.work_address, nico.role)

print("-------" * 10)

sam = Person(name="Sam Esmail", prefered_colors=["Black", "Red"])
sam.add_points(100)
print(sam.name, sam.balance, sam.prefered_colors, sam.work_address, sam.role)
