#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
from abc import ABC, abstractmethod

from models import Cart, Client


class AbstractProvider(ABC):
    @abstractmethod
    def suggested_products(self):
        return None

    @abstractmethod
    def read_products(self, name: str):
        return None

    @abstractmethod
    def read_brands(self, name: str):
        return None

    @abstractmethod
    def create_cart(self, cart: Cart):
        return cart

    @abstractmethod
    def save_client(self, client: Client):
        return client
