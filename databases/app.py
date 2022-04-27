from peewee import *

# db = SqliteDatabase(":memory:")
db = SqliteDatabase("app.db")


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db


def create_tables():
    with db:
        db.create_tables([Person])
