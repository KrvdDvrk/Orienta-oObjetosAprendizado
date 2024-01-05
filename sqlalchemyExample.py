from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()  #  factory


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))

    def __str__(self):
        return self.name.upper()


class Balance(Base):
    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)
    person_id = Column(Integer, ForeignKey(Person.id))
    person = relationship("Person", foreign_keys="Balance.person_id")


engine = create_engine("sqlite:////tmp/database.db")

Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionLocal()

# person = Person(name="Krvd")
# session.add(person)  # INSET INTO PERSON (NAME) values ()

# person = Person(name="Dvrk")
# session.add(person)

# session.commit()

# OPTIONAL: Person.name == "Krvd"  # WHERE person.name = 'Krvd'

# results = session.query(Person).filter(Person.name == "Krvd")
# for result in results:
#     print(result)  # ou print(result.name, result.id)


# results = session.query(Person).filter(Person.name == "Krvd")
# for result in results:
#     print(result.name, result.id)  # Está com o filter !!!!


# results = session.query(Person)
# for result in results:
#     print(result.name, result.id)


# results = session.query(Person)
# for result in results:
#     balance = Balance(value=40, person_id=result.id)
#     session.add(balance)

# session.commit()


# results = session.query(Person)
# for result in results:
#     print(result)


# MODO SEM O RELATIONSHIP
# results = session.query(Person.name, Balance.value).join(Balance, isouter=True)
# for result in results:
#     print(result)    -> Resultado vem como um tupla.


results = session.query(Balance)
for result in results:
    print(result.value, result.person.name)
