#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela

import peewee

from config.peewee import BaseModel
from models import Client, Product


class Cart(BaseModel):
    client: peewee.ForeignKeyField(Client)
    products: peewee.ManyToManyField(Product)

