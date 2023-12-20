people = [
    {"name": "Van Damme", "balance": 500, "role": "Mercenary"},
    {"name": "Nicolas Cage", "balance": 100, "role": "Boss"},
]


def add_points(person, value):
    # são puras, ou seja - no side effects
    data = person.copy()
    if data["role"] == "Boss":
        value *= 3
    data["balance"] += value
    return data


result = map(lambda person: add_points(person, 100), people)
# funcional
# declarativo
# lazy evaluation

print("Exemplo com a função lambda: \n")
print(list(result))

print("----" * 8)

print("Exemplo com o people: \n")
print(people)
