#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela
from errors.response_msg import ResponeMsg
from models.message import Message
from rules.check_response import CheckResponse
from service.client import ClientService


class InfoName:
    _message: Message
    _check_response: CheckResponse
    _client_service: ClientService = ClientService()

    def __init__(self, message: Message):
        self._message = message
        self._check_response = CheckResponse(self._message)

    def check(self) -> bool:
        return self._client_service.exist(device_id=self._message.device)

    def new(self) -> str:
        return self._client_service.new(self._message)