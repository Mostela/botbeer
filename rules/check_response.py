#  Copyright (c) 2021.
#  Date: 2021 / 6 / 23
#  Github: https://github.com/mostela
import re

from models.message import Message


class CheckResponse:
    _message: Message

    def __init__(self, message: Message):
        self._message = message

    def hello(self) -> bool:
        if re.match("oi", self._message.text):
            return True

    def name(self) -> bool:
        # TODO: Verifica se são caracteres validos
        return True
