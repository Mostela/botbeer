#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
import abc

from models.message import Message


class ServiceABS(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def process_message(message: Message):
        pass
