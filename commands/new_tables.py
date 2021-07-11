#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
import models
from commands import Command


class NewTables(Command):
    def execute(self):
        for clas in models.__all__:
            clas().create_table()
            clas()
