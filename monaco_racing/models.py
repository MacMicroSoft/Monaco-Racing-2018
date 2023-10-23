from peewee import SqliteDatabase, CharField, DateTimeField, Model

db = SqliteDatabase('database.db', pragmas={'journal_mode': 'wal'})


class BaseModel(Model):
    class Meta:
        database = db


class Start(BaseModel):
    name_id = CharField(unique=True)
    date = CharField()
    time = DateTimeField()


class End(BaseModel):
    name_id = CharField(unique=True)
    date = CharField()
    time = DateTimeField()


class Abbr(BaseModel):
    name_id = CharField(unique=True)
    person = CharField()
    car = CharField()


def create_tables():
    db.connect()
    db.create_tables([Start, End, Abbr])
    db.close()


if __name__ == '__main__':
    create_tables()
