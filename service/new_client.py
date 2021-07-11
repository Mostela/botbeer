#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
import uuid

from errors.client_name import ClientNameDeviceIdNoSending
from models import Client
from models.message import Message
from provider.mysql import MysqlProvider
from service import ServiceABS
from utils.random_device import random_device


class ClientServiceName(ServiceABS):
    
    @staticmethod
    def process_message(message: Message) -> Client:
        database = MysqlProvider()
        client = Client()
        client.name = message.text
        client.guid = uuid.uuid4().hex
        if not message.mobile:
            client.mobile = message.mobile
        if not message.device:
            raise ClientNameDeviceIdNoSending()
        client.device = message.device
        database.save_client(client)
        return client
