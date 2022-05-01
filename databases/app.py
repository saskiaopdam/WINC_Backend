from peewee import *

# db = SqliteDatabase(":memory:")
db = SqliteDatabase("app.db")


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db


# add a table to the database
def create_tables():
    with db:
        db.create_tables([Person])


# remove a table from the database
def drop_tables():
    with db:
        db.drop_tables([Person])
