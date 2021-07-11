#  Copyright (c) 2021.
#  Date: 2021 / 6 / 19
#  Github: https://github.com/mostela
from commands import Command
from commands.new_tables import NewTables


class CommandsList:
    def __init__(self):
        self.__commands = list()

    def new_command(self, command: Command):
        self.__commands.append(command)

    def execute_all(self):
        for call in self.__commands:
            call.execute()


class Commands:
    @staticmethod
    def start(new_tables=True):
        commands = CommandsList()
        if new_tables:
            commands.new_command(NewTables())

        commands.execute_all()
