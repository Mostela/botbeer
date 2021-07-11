#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela
from errors.general_errors import GeneralErrors


class ClientNameDeviceIdNoSending(GeneralErrors):
    def __init__(self, message="Device id not sending"):
        super().__init__(message)


class ClientNameNotFound(GeneralErrors):
    def __init__(self, message="Client not found"):
        super().__init__(message)
