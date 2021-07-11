#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
from abc import abstractmethod, ABCMeta


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass
