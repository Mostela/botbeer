#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela
from models.message import Message
from service.new_client import ClientServiceName


class ClientService:

    def new(self, message: Message):
        return ClientServiceName.process_message(message=message)

    def exist(self, device_id: str):
        # TODO: Mockado para testes
        return False
