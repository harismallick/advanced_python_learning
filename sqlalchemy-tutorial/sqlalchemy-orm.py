from sqlalchemy import create_engine, Integer, String, Float, Column, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import pandas as pd # type: ignore

engine = create_engine("sqlite:///mydatabase.db", echo=True)

Base = declarative_base() 

class Person(Base): # type: ignore
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)

    things = relationship('Thing', back_populates='person')

class Thing(Base): # type: ignore
    __tablename__ = 'things'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    value = Column(Float)
    owner = Column(Integer, ForeignKey('people.id'))

    person = relationship('Person', back_populates='things')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# new_person = Person(name='Charlie', age=60)
# session.add(new_person)

# session.flush() # Perform updates to the database without committing the changes
# # This is useful if changes need to be made a one table, before dependent changes can be made to another table

# new_thing = Thing(description="Camera", value=500, owner=new_person.id)
# session.add(new_thing)

# session.commit()

# print([thing.description for thing in new_person.things])
# print(new_thing.person.name)

# This way, a relational database can be queried without having to use SQL syntax


# CRUD operations using ORM:

# Read operation:

result = session.query(Person).all()
print([(p.name, p.age) for p in result])

# Applying filters:

result = session.query(Person).filter(Person.age > 50).all()
print([(p.name, p.age) for p in result])


# # Update operation:

# update_query = session.query(Person).filter(Person.name == "Charlie").update({'name': "Charles"})
# # ALWAYS REMEMBER TO COMMIT
# session.commit()

# result = session.query(Person).all()
# print([p.name for p in result])

# # Delete operation

# delete_query = session.query(Person).filter(Person.age == 30).delete()
# session.commit()
# # Mike should be deleted from the table

# result = session.query(Person).all()
# print([p.name for p in result])


# Join operation

join_result= session.query(Person.name, Thing.description).join(Thing).all()

print(join_result)

# Aggregation using func

reduce_query = session.query(Thing.owner, func.sum(Thing.value)).group_by(Thing.owner).all()
print(reduce_query)


# Supplementing sqlalchemy with pandas


df = pd.read_sql("SELECT * FROM people", con=engine)
print(df)

new_data = pd.DataFrame({
    'name': ['Dorian', 'Turk'],
    'age': [34, 35]
})

# write the dataframe to the db table:

new_data.to_sql('people', con=engine, if_exists='append', index=False)

df = pd.read_sql("SELECT * FROM people", con=engine)
print(df)
