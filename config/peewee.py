#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
import peewee


class BaseModel(peewee.Model):

    def create_table(self, safe=True, **options):
        if not super().table_exists():
            print("New table created")
            super().create_table(safe, **options)
        else:
            super().drop_table(safe=False, drop_sequences=True)
            print(f"Table {self.__class__.__name__} update")
            super().create_table(safe, **options)

    class Meta:
        database = peewee.SqliteDatabase('botbber.db')
