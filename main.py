#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
from models.message import Message

# Commands.start()
from rules.hello_client import HelloClient
from rules.info_name import InfoName
from rules.response_text import ResponseText
from service.machine import StateInfos
from utils.list_response import ListResponse
from utils.random_device import random_device


def process_quest(state_machine: StateInfos, message: Message) -> str:
    print(_state_machine.current_state)
    list_response = ListResponse()
    _responses = ResponseText()

    print(_state_machine.states)

    try:
        if _state_machine.is_start_talk:
            hello_client = HelloClient(message)
            if hello_client.hello():
                _state_machine.run('start')
                list_response.add(_responses.hello())
            else:
                list_response.add("Sorry no understand :(")
        elif _state_machine.is_info_name:
            info_name = InfoName(message)
            _state_machine.run('what_name')
            if info_name.check():
                list_response.add(_responses.welcome_back(message.text))
                list_response.add(_responses.list_options_advanced())
            else:
                info_name.new()
                list_response.add(_responses.whats_your_name(message.text))
                list_response.add(_responses.list_options_basic())
        else:
            list_response.add("Sorry no understand :(")

    except Exception as ex:
        return str(ex)

    return list_response.read()


_state_machine = StateInfos()
device = random_device()
while True:
    ask = input("INPUT >>>\n")
    _message: Message = Message(text=ask, device=device, mobile=None)
    print(process_quest(_state_machine, _message))
