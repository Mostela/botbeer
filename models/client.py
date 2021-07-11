#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
import peewee
from config.peewee import BaseModel


class Client(BaseModel):
    name = peewee.TextField(null=False, index=True)
    device = peewee.CharField()
    mobile = peewee.CharField(null=True)
    guid = peewee.UUIDField()

