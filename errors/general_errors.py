#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela
from typing import Tuple


def _lstrip_str(in_s: str, lstr: str) -> str:
    """
    Args:
        in_s (:obj:`str`): in string
        lstr (:obj:`str`): substr to strip from left side
    Returns:
        :obj:`str`: The stripped string.
    """
    if in_s.startswith(lstr):
        res = in_s[len(lstr) :]
    else:
        res = in_s
    return res


class GeneralErrors(Exception):
    __slots__ = ('message',)

    def __init__(self, message: str):
        super().__init__()

        msg = _lstrip_str(message, 'Error: ')
        msg = _lstrip_str(msg, '[Error]: ')
        if msg != message:
            msg = msg.capitalize()
        self.message = msg

    def __str__(self) -> str:
        return '%s' % self.message

    def __reduce__(self) -> Tuple[type, Tuple[str]]:
        return self.__class__, (self.message,)
