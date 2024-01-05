from typing import Optional

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select

# We have to monkey patch this attributes
# https://github.com/tiangolo/sqlmodel/issues/189
from sqlmodel.sql.expression import Select, SelectOfScalar

SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore


# Base (declarative_base)
# BaseModel (pydantic)


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    balance: "Balance" = Relationship(back_populates="person")


# table=True, substitui o __tablename__


class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    person_id: int = Field(foreign_key="person.id")

    person: Person = Relationship(back_populates="balance")


engine = create_engine("sqlite:////tmp/sqlmodel.db", echo=False)
SQLModel.metadata.create_all(bind=engine)


with Session(engine) as session:
    ...
    # person = Person(name="Krvd")
    # session.add(person)

    # person = Person(name="Dvrk")
    # session.add(person)

    # session.commit()

    # SELECT FROM PERSON WHERE person.name = "Krvd";
    # sql = select(Person).where(Person.name == "Krvd")

    # sql = select(Person)
    # results = session.exec(sql)
    # for person in results:
    #     balance = Balance(value=60, person=person)
    #     session.add(balance)
    # session.commit()

    sql = select(Person)
    results = session.exec(sql)
    for person in results:
        print(person.name, person.balance)

    # sql = select(Balance).where(Balance.value > 3)
    # results = session.exec(sql)
    # for balance in results:
    #     print(balance) # ou (balance.person) ou (balance.person.name)

    # sql = select(Person, Balance).where(Balance.person_id == Person.id)
    # results = session.exec(sql)
    # for person, balance in results:
    #     print(person.name, balance.value)

    # sql = select(Person, Balance).join(Balance, isouter=True)
    # results = session.exec(sql)
    # for person, balance in results:
    #     print(person.name, balance.value)
