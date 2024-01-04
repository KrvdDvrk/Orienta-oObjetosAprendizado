# ESTRUTURA BÁSICA

"""
import sqlite3

con = sqlite3.connect("sql_example.db")

con.execute("CREATE TABLE ...")

con.commit()

con.close()
"""

import sqlite3

con = sqlite3.connect("sql_example.db")
con.execute("PRAGMA foreign_keys = ON;")  # só o sqlite precisa disso

# INSTRUCTIONS

instructions = """\
CREATE TABLE if not exists person (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar NOT NULL,
    email varchar UNIQUE NOT NULL,
    dept varchar NOT NULL,
    role varchar NOT NULL
);
---
CREATE TABLE if not exists balance (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer UNIQUE NOT NULL,
    value integer NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists movement (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer NOT NULL,
    value integer NOT NULL,
    date datetime NOT NULL,
    actor varchar NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
---
CREATE TABLE if not exists user (
    id integer PRIMARY KEY AUTOINCREMENT,
    person integer UNIQUE NOT NULL,
    password varchar NOT NULL,
    FOREIGN KEY(person) REFERENCES person(id)
);
"""
for instruction in instructions.split("---"):
    con.execute(instruction)

# INTRODUCING INSERT IN PYTHON

# instruction = """\
# INSERT INTO person (name, email, dept, role)
# VALUES ('Kyrthon', 'lordoftheshadowisland@dvrk.com', 'Sales', 'Manager');
# """

# con.execute(instruction)
# con.commit()

# Toda vez que roda um comando que está dentro da categoria DML, devemos fazer commit.

# INTRODUCING SELECT IN PYTHON

instruction = """\
SELECT id, 500
FROM person
WHERE dept = 'Sales';
"""

# JOIN NO PYTHON
# """\
# SELECT person.name, person.email, balance.value
# FROM person
# LEFT JOIN balance
# WHERE person.id = balance.person;
# """

cur = con.cursor()
result = cur.execute(instruction)
for row in result:
    instruction = "INSERT INTO balance (person, value) VALUES (?, ?)"
    con.execute(instruction, row)

con.commit()
#    print(row)  # tupla

print(result)

# con.commit()

con.close()
