#  Copyright (c) 2021.
#  Date: 2021 / 7 / 11
#  Github: https://github.com/mostela

class ListResponse:
    _responses = ()

    def add(self, text: str):
        self._responses = self._responses + (text, )

    def read(self):
        resp = ""
        for t in self._responses:
            resp += str(f"{t}. ")
        return resp

    def __str__(self):
        return self.read()
