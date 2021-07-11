#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
from provider import AbstractProvider
from models import Client, Cart


class MysqlProvider(AbstractProvider):
    def suggested_products(self):
        pass

    def read_products(self, name: str):
        pass

    def read_brands(self, name: str):
        pass

    def create_cart(self, cart: Cart):
        pass

    def save_client(self, client: Client):
        return client.save()
