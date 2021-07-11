#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela
from models.message import Message
from rules.check_response import CheckResponse


class HelloClient:
    _message: Message
    _check_response: CheckResponse

    def __init__(self, message: Message):
        self._message = message
        self._check_response = CheckResponse(self._message)

    def hello(self):
        return self._check_response.hello()
