# from sqlalchemy import create_engine, text

# engine = create_engine("sqlite:///mydatabase.db", echo=True)
# # The echo parameter is to see in the terminal the commands being executed by the engine.

# # Example of how to manually create a DB connection an to execute + commit db operations:
# conn = engine.connect()

# conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int);"))

# conn.commit()

# # sqlalchemy simplifies the above by using Session

# from sqlalchemy.orm import Session

# session = Session(engine)

# session.execute(text('INSERT INTO people (name, age) VALUES ("Mike", 30);'))

# session.commit()


## The above two examples is not the most efficient way to use sqlalchemy
# The main purpose of this toolkit is to interact with databases in a pythonic way using python syntax
# The other purpose of sqlalchemy is to map relational dabatase tables to classes in Python.

# Using classes and data models to interact with DBs:

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, Float, func

engine = create_engine("sqlite:///mydatabase.db", echo=True)

# Instantiate a MetaData object for the db
meta = MetaData()

# Create a table using the Table class
people = Table(
    "people",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)

meta.create_all(engine)

conn = engine.connect()

# Example insert into table query:

# insert_query = people.insert().values(name="Mike", age=30)
# result = conn.execute(insert_query)
# conn.commit()

# insert_query = people.insert().values(name="Jane", age=40)
# result = conn.execute(insert_query)
# conn.commit()

# Example read query

# select_query = people.select().where(people.c.age > 20)
# result = conn.execute(select_query)

# for row in result.fetchall():
#     print(row)


# # Example update query:

# update_query = people.update().where(people.c.name == "Mike").values(age=50)
# result = conn.execute(update_query)
# conn.commit()

# # Read the update:
# select_query = people.select().where(people.c.age > 20)
# result = conn.execute(select_query)

# for row in result.fetchall():
#     print(row)

# # Example delete query:

# delete_query = people.delete().where(people.c.name == "Mike")
# conn.execute(delete_query)
# conn.commit()

# # Read after delete operation:
# select_query = people.select() # This is how to do SELECT * FROM people
# result = conn.execute(select_query)

# for row in result.fetchall():
#     print(row)


# Establishing relationships between tables:

things_table = Table(
    "things",
    meta,
    Column('id', Integer, primary_key=True),
    Column('description', String, nullable=False),
    Column('value', Float),
    Column('owner', Integer, ForeignKey('people.id'))
)

meta.create_all(engine)

# Insert rows into things table and people table

insert_people = people.insert().values([
    {'name': 'Mike', 'age': 30},
    {'name': 'Bob', 'age': 35},
    {'name': 'Anna', 'age': 38},
    {'name': 'John', 'age': 50},
    {'name': 'Clara', 'age': 42}
])

insert_things = things_table.insert().values([
    {'owner': 2, 'description': 'Laptop', 'value': 800},
    {'owner': 2, 'description': 'Mouse', 'value': 50},
    {'owner': 2, 'description': 'Keyboard', 'value': 100},
    {'owner': 3, 'description': 'Book', 'value': 30},
    {'owner': 4, 'description': 'Bottle', 'value': 10},
    {'owner': 5, 'description': 'Speakers', 'value': 80},
])

# # The order of db operations is important

# # Need to add rows to the people table first

# result = conn.execute(insert_people)
# conn.commit()

# # Now that the foreign key values for things table exists, now we can add to the things table

# result = conn.execute(insert_things)
# conn.commit()


# Doing join statements in sqlalchemy

join_statement = people.join(things_table, people.c.id == things_table.c.owner)
select_statement = people.select().with_only_columns(people.c.name, things_table.c.description).select_from(join_statement)

result = conn.execute(select_statement)

for row in result.fetchall():
    print(row)


# Aggregating values from multiple rows into one value, like a reduce function
# this requires the 'func' method

group_by_statement = things_table.select().with_only_columns(things_table.c.owner, func.sum(things_table.c.value)).group_by(things_table.c.owner)
result = conn.execute(group_by_statement)

for row in result.fetchall():
    print(row)

