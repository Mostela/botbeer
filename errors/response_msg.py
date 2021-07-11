#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela
from errors.general_errors import GeneralErrors


class ResponeMsg(GeneralErrors):
    def __init__(self, message: str):
        super().__init__(message)
