#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
import peewee

from config.peewee import BaseModel


class Product(BaseModel):
    title = peewee.TextField(null=False)
    brand = peewee.TextField(null=False, index=True)
    model = peewee.TextField(null=False)
    status = peewee.BooleanField(default=False)
    code = peewee.TextField(null=False)
    price = peewee.FloatField(null=False, default=0)
