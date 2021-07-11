#  Copyright (c) 2021.
#  Date: 2021 / 6 / 21
#  Github: https://github.com/mostela

class Message:
    text: str = None
    device: str = None
    mobile: str = None

    def __init__(self, text, device='1', mobile='0'):
        self.text = text
        self.mobile = mobile
        self.device = device

    def __str__(self):
        return self.text
