from peewee import Model, DateTimeField, CharField, BooleanField, TextField, PostgresqlDatabase

DATABASE = 'poshquiz'
HOST = 'localhost'
PORT = '5432'
USER = 'poshquiz'
PASSWORD = 'poshquiz'

database = PostgresqlDatabase(host=HOST, port=PORT, database=DATABASE, user=USER, password=PASSWORD)


class BaseModel(Model):
    class Meta:
        database = database


class Message(BaseModel):
    datetime = DateTimeField()
    sender = CharField(max_length=255)
    text = TextField()
    messenger = CharField(max_length=50)


# simple utility function to create tables
def create_tables():
    database.connect()
    Message.create_table()
    database.close()
